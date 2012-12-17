//-----------------------------------------------------------------------
// <copyright file="IVerifyResponseParser.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.Verify
{
    /// <summary>
    /// Interface for parsing response from the TeleSign REST API. The raw
    /// responses are strings containing JSON formatted data. Each function
    /// parses the response into the relevant response object.
    /// </summary>
    public interface IVerifyResponseParser
    {
        /// <summary>
        /// Parses a TeleSign Verify JSON response into a rich object.
        /// </summary>
        /// <param name="json">The json string containing the response.</param>
        /// <returns>A VerifyResponse object populated with the data from the response.</returns>
        VerifyResponse ParseVerifyResponse(string json);
    }
}
