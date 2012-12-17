//-----------------------------------------------------------------------
// <copyright file="ResponseParseException.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    using System;

    /// <summary>
    /// Exception for errors that occur while parsing the json response.
    /// The occurence of this exception indicates that the underlying
    /// transaction probably succeeded but that the response could not
    /// be parsed correctly. The raw response will be contained in the
    /// exception along with the original exception in the inner
    /// exception.
    /// </summary>
    public class ResponseParseException : Exception
    {
        /// <summary>
        /// Initializes a new instance of the ResponseParseException class with
        /// an error message and the raw response string.
        /// </summary>
        /// <param name="message">The error message for the exception.</param>
        /// <param name="rawResponse">The raw JSON response string.</param>
        public ResponseParseException(
                    string message, 
                    string rawResponse)
            : this(
                        message, 
                        rawResponse, 
                        null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the ResponseParseException class with
        /// an error message, the raw response string and an inner exception.
        /// </summary>
        /// <param name="message">The error message for the exception.</param>
        /// <param name="rawResponse">The raw JSON response string.</param>
        /// <param name="innerException">The inner exception.</param>
        public ResponseParseException(
                    string message, 
                    string rawResponse, 
                    Exception innerException)
            : base(
                        message, 
                        innerException)
        {
            this.RawResponse = rawResponse;
        }

        /// <summary>
        /// Gets the raw response string that was being parsed which caused this
        /// exception.
        /// </summary>
        public string RawResponse { get; private set; }
    }
}
