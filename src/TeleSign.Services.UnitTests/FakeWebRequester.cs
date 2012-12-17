//-----------------------------------------------------------------------
// <copyright file="FakeWebRequester.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.UnitTests
{
    using System.Net;
    using TeleSign.Services;

    /// <summary>
    /// Implements the most trivial implementation of IWebRequester.
    /// It implements ReadResponseAsString by simply returning
    /// a response string that has been provided by calling SetResponse.
    /// </summary>
    public class FakeWebRequester : IWebRequester
    {
        /// <summary>
        /// The response that will be returned.
        /// </summary>
        private string response;

        public FakeWebRequester()
        {
            this.response = string.Empty;
        }

        /// <summary>
        /// Set the response string. Every call to ReadResponseAsString will
        /// return this string.
        /// </summary>
        /// <param name="response">The response you want from ReadResponseAsString.</param>
        public void SetResponse(string response)
        {
            this.response = response;
        }

        public string ReadResponseAsString(WebRequest request)
        {
            return this.response;
        }
    }
}
