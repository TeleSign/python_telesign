//-----------------------------------------------------------------------
// <copyright file="TeleSignService.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Globalization;
    using System.Net;
    using System.Text;
    using System.Web;

    /// <summary>
    /// The base class for TeleSign REST services.
    /// </summary>
    public class TeleSignService
    {
        /// <summary>
        /// The configuration information for the service.
        /// </summary>
        private TeleSignServiceConfiguration configuration;

        /// <summary>
        /// The module used to generate authorization strings.
        /// </summary>
        private TeleSignAuthentication authentication;

        /// <summary>
        /// Gets or sets the object used to perform web requests.
        /// </summary>
        protected IWebRequester WebRequester { get; private set; }

        /// <summary>
        /// Initializes a new instance of the TeleSignService class with the supplied
        /// configuration and webrequester.
        /// </summary>
        /// <param name="configuration">The configuration information for the service. If null will try to read the default configuration file.</param>
        /// <param name="webRequester">The web requester to use to perform web requests. If null will use the default.</param>
        protected TeleSignService(
                    TeleSignServiceConfiguration configuration,
                    IWebRequester webRequester)
        {
            this.configuration = (configuration == null)
                        ? TeleSignServiceConfiguration.ReadConfigurationFile()
                        : configuration;

            this.WebRequester = (webRequester == null)
                        ? new WebRequester()
                        : webRequester;

            this.ValidateConfiguration();

            this.authentication = new TeleSignAuthentication(this.configuration.Credential);
        }

        /// <summary>
        /// Initializes a new instance of the TeleSignService class with the supplied
        /// configuration.
        /// </summary>
        /// <param name="configuration">The configuration information for the service.</param>
        protected TeleSignService(TeleSignServiceConfiguration configuration)
            : this(configuration, null)
        {
        }

        /// <summary>
        /// <para>
        /// Initializes a new instance of the TeleSignService class and reads the
        /// configuration file from a default location in a file called "TeleSign.config.xml"
        /// from the location that the TeleSign.dll is located.
        /// </para>
        /// <para>
        /// To load the configuration from an alternate location call 
        /// TeleSignServiceConfiguration.ReadConfigurationFile(fileName) and pass the
        /// return configuration object to the other constructor of this class.
        /// </para>
        /// </summary>
        protected TeleSignService()
            : this(null, null)
        {
        }

        /// <summary>
        /// Constructs the arguments to the rest service as a string. The key-value pairs are
        /// built into a string of the form key1=value1&amp;key2=value2
        /// </summary>
        /// <param name="fields">The key value pairs of the arguments.</param>
        /// <returns>A string of the form key1=value1&amp;key2=value2</returns>
        public static string ConstructQueryString(Dictionary<string, string> fields)
        {
            if (fields != null && fields.Count > 0)
            {
                StringBuilder builder = new StringBuilder();
                foreach (KeyValuePair<string, string> entry in fields)
                {
                    builder.AppendFormat(
                                CultureInfo.InvariantCulture,
                                "{0}={1}&",
                                HttpUtility.UrlEncode(entry.Key, Encoding.UTF8),
                                HttpUtility.UrlEncode(entry.Value, Encoding.UTF8));
                }

                // Chop off the trailing &
                builder.Length -= 1;

                return builder.ToString();
            }

            return string.Empty;
        }

        /// <summary>
        /// Cleans up phone number strings by removing any non-digit characters from
        /// them. Will throw an exception if the resulting cleaned up string has
        /// no characters.
        /// </summary>
        /// <param name="phoneNumber">The input phone number.</param>
        /// <returns>The input phone number with all non-digit characters removed.</returns>
        public string CleanupPhoneNumber(string phoneNumber)
        {
            CheckArgument.NotNullOrEmpty(phoneNumber, "phoneNumber");

            StringBuilder builder = new StringBuilder(
                        phoneNumber.Length, 
                        phoneNumber.Length);

            // Remove non-digit characters from the phone number.
            foreach (char c in phoneNumber)
            {
                if (Char.IsDigit(c))
                {
                    builder.Append(c);
                }
            }

            // Reject empty strings.
            if (builder.Length == 0)
            {
                string message = string.Format(
                            CultureInfo.InvariantCulture,
                            "Phone Number '{0}' contains no digits", 
                            phoneNumber);

                throw new ArgumentException(
                            message, 
                            "phoneNumber");
            }

            return builder.ToString();
        }

        /// <summary>
        /// Validates the information in the configuration.
        /// </summary>
        protected virtual void ValidateConfiguration()
        {
            if (this.configuration.Credential == null)
            {
                throw new ArgumentNullException(
                            "configuration.Credential", 
                            "The Credential member of the configuration was null");
            }

            if (this.configuration.ServiceAddress == null)
            {
                throw new ArgumentNullException(
                            "configuration.ServiceAddress", 
                            "The ServiceAddress member of the configuration was null");
            }

            if (string.IsNullOrEmpty(this.configuration.Credential.SecretKey))
            {
                throw new ArgumentException("No secret key was provided. Requests to TeleSign services require require a valid customer id and secret key.");
            }
        }

        /// <summary>
        /// Constructs a .NET WebRequest object for the request.
        /// </summary>
        /// <param name="resourceName">The name of the resource - ie. the relative part of the URL.</param>
        /// <param name="method">The http method - POST, DELETE, GET, PUT.</param>
        /// <param name="fields">The fields that are the arguments to the request.</param>
        /// <param name="authMethod">The method of authentication to use.</param>
        /// <returns>A WebRequest object.</returns>
        protected WebRequest ConstructWebRequest(
                    string resourceName,
                    string method,
                    Dictionary<string, string> fields = null,
                    AuthenticationMethod authMethod = AuthenticationMethod.HmacSha1)
        {
            CheckArgument.NotNullOrEmpty(resourceName, "resourceName");
            CheckArgument.NotNullOrEmpty(method, "method");

            DateTime timeStamp = DateTime.UtcNow;
            string nonce = Guid.NewGuid().ToString();

            // When the Uri is constructed. If it is a GET request the fields
            // are put into the Uri's query string eg ?foo=bar. When the 
            // method is POST the fields are not used in constructing the Uri,
            // but below they are placed in the encoded body.
            Uri fullUri = this.ConstructResourceUri(
                        resourceName, 
                        method, 
                        fields);

            HttpWebRequest request = (HttpWebRequest)HttpWebRequest.Create(fullUri);
            request.Method = method;

            string contentType = string.Empty;
            string encodedBody = string.Empty;
            if (method == "POST")
            {
                contentType = "application/x-www-form-urlencoded";
                encodedBody = TeleSignService.ConstructQueryString(fields);
            }

            string authorizationString = this.authentication.ConstructAuthorizationString(
                        resourceName,
                        method,
                        timeStamp,
                        nonce,
                        contentType, 
                        encodedBody,
                        authMethod);

            request.Headers.Add("Authorization", authorizationString);
            request.Headers.Add("x-ts-auth-method", this.authentication.MapAuthenticationMethodToHeaderString(authMethod));
            request.Headers.Add("x-ts-date", timeStamp.ToString("r"));
            request.Headers.Add("x-ts-nonce", nonce);

            if (method == "POST")
            {
                byte[] body = Encoding.UTF8.GetBytes(encodedBody);

                request.Accept = "application/json";
                request.ContentType = contentType;
                request.ContentLength = body.Length;
                using (Stream stream = request.GetRequestStream())
                {
                    stream.Write(body, 0, body.Length);
                }
            }

            return request;
        }

        /// <summary>
        /// Constructs the resource URI to the REST API. For GET
        /// requests the query string is concatenated into the Uri. For
        /// POST requests the fields are ignored here but are later passed
        /// encoded in the request body.
        /// </summary>
        /// <param name="resourceName">The name of the resource (relative part of the URI).</param>
        /// <param name="method">The HTTP method (get or post).</param>
        /// <param name="fields">The additional fields.</param>
        /// <returns>The fully qualified URI to the resource.</returns>
        private Uri ConstructResourceUri(
                    string resourceName, 
                    string method, 
                    Dictionary<string, string> fields)
        {
            string relativePath = resourceName;

            if (method == "GET" && (fields != null && fields.Count != 0))
            {
                relativePath = string.Format(
                            CultureInfo.InvariantCulture,
                            "{0}?{1}",
                            relativePath,
                            TeleSignService.ConstructQueryString(fields));
            }

            return new Uri(
                        this.configuration.ServiceAddress, 
                        relativePath);
        }
    }
}
