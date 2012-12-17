//-----------------------------------------------------------------------
// <copyright file="SerializingWebRequester.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.UnitTests
{
    using System.Net;
    using System.Text;

    /// <summary>
    /// <para>
    /// A simple implemenetation of IWebRequester for testing purposes.
    /// It takes a select set of parameters from the web request
    /// and concatenates them into a key-value pair string set. This is
    /// used to validate that relevant inputs to the higher level
    /// API's made their way down to the WebRequest. This class does
    /// not make any network request.
    /// </para>
    /// <para>
    /// Also note - that what it returns is not valid JSON that the
    /// parser will not be able to process so this is only useful
    /// for testing the raw versions of the service.
    /// </para>
    /// </summary>
    public class SerializingWebRequester : IWebRequester
    {
        public string ReadResponseAsString(WebRequest request)
        {
            string queryString = request.RequestUri.Query;

            // Chop the ? off the front if it is there
            if (queryString.StartsWith("?"))
            {
                queryString = queryString.Substring(1);
            }

            return this.ConstructSerializedString(
                        request.Method,
                        request.RequestUri.AbsolutePath,
                        request.ContentType,
                        queryString);
        }

        public string ConstructSerializedString(
                    string method,
                    string localUriPath,
                    string contentType,
                    string queryString)
        {
            StringBuilder builder = new StringBuilder();

            builder.AppendFormat("Method: {0}\r\n", DefaultIfNull(method));
            builder.AppendFormat("LocalUriPath: {0}\r\n", DefaultIfNull(localUriPath));
            builder.AppendFormat("ContentType: {0}\r\n", DefaultIfNull(contentType));
            builder.AppendFormat("QueryString: {0}\r\n", DefaultIfNull(queryString));

            return builder.ToString();
        }

        private static string DefaultIfNull(string value)
        {
            if (value == null)
            {
                return "<null>";
            }

            return value;
        }
    }
}
