//-----------------------------------------------------------------------
// <copyright file="TeleSignAuthentication.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    using System;
    using System.Globalization;
    using System.Security.Cryptography;
    using System.Text;

    /// <summary>
    /// Encapsulates the construction of the authentication strings and hashing.
    /// </summary>
    public class TeleSignAuthentication
    {
        /// <summary>
        /// The TeleSign credentials for authenticating with the TeleSign services.
        /// This consists of a customer id and a secret key.
        /// </summary>
        private TeleSignCredential credential;

        /// <summary>
        /// Initializes a new instance of the TeleSignAuthentication class with
        /// a credential.
        /// </summary>
        /// <param name="credential">
        /// The TeleSign credentials for authenticating with the TeleSign services.
        /// </param>
        public TeleSignAuthentication(TeleSignCredential credential)
        {
            CheckArgument.NotNull(credential, "credential");

            this.credential = credential;
        }

        /// <summary>
        /// Constructs the authorization string as defined in the TeleSign REST API. First a
        /// "StringToSign" is constructed then this is the string that is hashed
        /// and that hash is used to authenticate the user. Then the authorization string is created
        /// from the customer id and the StringToSign hashed with the secret key.
        /// </summary>
        /// <param name="resourceName">The name of the resource - ie. the relative part of the URL.</param>
        /// <param name="method">The http method - POST, DELETE, GET, PUT.</param>
        /// <param name="timestamp">The timestamp to use.</param>
        /// <param name="nonce">The nonce (used for preventing replay attacks).</param>
        /// <param name="contentType">The mime type content type.</param>
        /// <param name="encodedBody">The body of a POST request.</param>
        /// <param name="authMethod">The authentication method to use.</param>
        /// <returns>The string that will be signed for authentication.</returns>
        public string ConstructAuthorizationString(
                    string resourceName,
                    string method,
                    DateTime timestamp,
                    string nonce,
                    string contentType,
                    string encodedBody,
                    AuthenticationMethod authMethod)
        {
            string stringToSign = this.ConstructStringToSign(
                        resourceName,
                        method,
                        timestamp,
                        nonce,
                        contentType,
                        encodedBody,
                        authMethod);

            return this.ConstructAuthorizationString(
                        stringToSign, 
                        authMethod);
        }

        /// <summary>
        /// Constructs the authorization by combining the customer id
        /// from the credential with the stringToSign hashed with
        /// the secret key.
        /// </summary>
        /// <param name="stringToSign">
        /// The stringToSign that is used for authentication.
        /// </param>
        /// <param name="authMethod">The method used for authentication.</param>
        /// <returns>The authorization string.</returns>
        public string ConstructAuthorizationString(
                    string stringToSign, 
                    AuthenticationMethod authMethod)
        {
            CheckArgument.NotNullOrEmpty(stringToSign, "stringToSign");

            return string.Format(
                        CultureInfo.InvariantCulture,
                        "TSA {0}:{1}",
                        this.credential.CustomerId,
                        this.ComputeHash(stringToSign, authMethod));
        }

        /// <summary>
        /// Constructs the "StringToSign" as defined in the TeleSign REST API. This is the string that is hashed
        /// and that hash is used to authenticate the user. Then the authorization string is created
        /// by from the customer id and the StringToSign hashed with the secret key.
        /// </summary>
        /// <param name="resourceName">The name of the resource - ie. the relative part of the URL.</param>
        /// <param name="method">The http method - POST, DELETE, GET, PUT.</param>
        /// <param name="timestamp">The timestamp to use.</param>
        /// <param name="nonce">The nonce (used for preventing replay attacks).</param>
        /// <param name="contentType">The mime type content type.</param>
        /// <param name="encodedBody">The body of a POST request.</param>
        /// <param name="authMethod">The authentication method to use.</param>
        /// <returns>The string that will be signed for authentication.</returns>
        public string ConstructStringToSign(
                    string resourceName,
                    string method,
                    DateTime timestamp,
                    string nonce,
                    string contentType,
                    string encodedBody,
                    AuthenticationMethod authMethod)
        {
            CheckArgument.NotNullOrEmpty(resourceName, "resourceName");
            CheckArgument.NotNullOrEmpty(method, "method");
            CheckArgument.NotNull(nonce, "nonce");
            CheckArgument.NotNull(contentType, "contentType");
            CheckArgument.NotNull(encodedBody, "encodedBody");

            string authMethodString = this.MapAuthenticationMethodToHeaderString(authMethod);

            return string.Format(
                        CultureInfo.InvariantCulture,
                        "{0}\n{1}\n\nx-ts-auth-method:{2}\nx-ts-date:{3}\nx-ts-nonce:{4}\n{5}{6}",
                        method,
                        contentType,
                        authMethodString,
                        timestamp.ToString("r"),
                        nonce,
                        encodedBody.Length == 0 ? string.Empty : encodedBody + "\n",
                        resourceName);
        }

        /// <summary>
        /// Constructs the "StringToSign" as defined in the TeleSign REST API. This is the string that is hashed
        /// and that hash is used to authenticate the user. Then the authorization string is created
        /// by from the customer id and the StringToSign hashed with the secret key.
        /// </summary>
        /// <param name="resourceName">The name of the resource - ie. the relative part of the URL.</param>
        /// <param name="method">The http method - POST, DELETE, GET, PUT.</param>
        /// <param name="contentType">The mime type content type.</param>
        /// <param name="encodedBody">The body of a POST request.</param>
        /// <returns>The string that will be signed for authentication.</returns>
        public string ConstructStringToSign(
                    string resourceName,
                    string method,
                    string contentType,
                    string encodedBody)
        {
            CheckArgument.NotNullOrEmpty(resourceName, "resourceName");
            CheckArgument.NotNullOrEmpty(method, "method");
            CheckArgument.NotNull(contentType, "contentType");
            CheckArgument.NotNull(encodedBody, "encodedBody");

            DateTime timestamp = DateTime.UtcNow;
            string nonce = Guid.NewGuid().ToString();

            return this.ConstructStringToSign(
                        resourceName,
                        method,
                        timestamp,
                        nonce,
                        contentType,
                        encodedBody,
                        AuthenticationMethod.HmacSha1);
        }

        /// <summary>
        /// Computes the hash of the StringToSign using the secret key.
        /// </summary>
        /// <param name="stringToSign">The StringToSign that will be hashed with the secret key.</param>
        /// <param name="authMethod">The authorization/hash method to be used.</param>
        /// <returns>The hash of the string to sign.</returns>
        public string ComputeHash(
                    string stringToSign, 
                    AuthenticationMethod authMethod)
        {
            CheckArgument.NotNullOrEmpty(stringToSign, "stringToSign");

            byte[] secretKeyBytes = Convert.FromBase64String(this.credential.SecretKey);
            byte[] stringToSignBytes = Encoding.UTF8.GetBytes(stringToSign);

            HMAC hasher = null;

            switch (authMethod)
            {
                case AuthenticationMethod.HmacSha1:
                    hasher = new HMACSHA1(secretKeyBytes);
                    break;
                case AuthenticationMethod.HmacSha256:
                    hasher = new HMACSHA256(secretKeyBytes);
                    break;
                default:
                    throw new NotSupportedException("Only HMAC SHA1 and SHA256 authentication is currently supported");
            }

            return Convert.ToBase64String(hasher.ComputeHash(stringToSignBytes));
        }

        /// <summary>
        /// Maps the AuthenticationMethod enumeration to the string used in headers.
        /// </summary>
        /// <param name="authMethod">The authentication method.</param>
        /// <returns>The header string for the authentication method.</returns>
        public string MapAuthenticationMethodToHeaderString(AuthenticationMethod authMethod)
        {
            switch (authMethod)
            {
                case AuthenticationMethod.HmacSha1:
                    return "hmac-sha1";
                case AuthenticationMethod.HmacSha256:
                    return "hmac-sha256";
                default:
                    throw new NotSupportedException("Only HMAC SHA1 and SHA256 authentication is currently supported");
            }
        }
    }
}
