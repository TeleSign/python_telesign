//-----------------------------------------------------------------------
// <copyright file="IPhoneIdResponseParser.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    /// <summary>
    /// Interface for parsing response from the TeleSign REST API. The raw
    /// responses are strings containing JSON formatted data. Each function
    /// parses the response into the relevant response object.
    /// </summary>
    public interface IPhoneIdResponseParser
    {
        /// <summary>
        /// Parses a TeleSign PhoneID Standard JSON response into a rich object.
        /// </summary>
        /// <param name="json">The json string containing the response.</param>
        /// <returns>A PhoneIdStandardResponse object populated with the data from the response.</returns>
        PhoneIdStandardResponse ParsePhoneIdStandardResponse(string json);

        /// <summary>
        /// Parses a TeleSign PhoneID Score JSON response into a rich object.
        /// </summary>
        /// <param name="json">The json string containing the response.</param>
        /// <returns>A PhoneIdScoreResponse object populated with the data from the response.</returns>
        PhoneIdScoreResponse ParsePhoneIdScoreResponse(string json);

        /// <summary>
        /// Parses a TeleSign PhoneID Live JSON response into a rich object.
        /// </summary>
        /// <param name="json">The json string containing the response.</param>
        /// <returns>A PhoneIdLiveResponse object populated with the data from the response.</returns>
        PhoneIdLiveResponse ParsePhoneIdLiveResponse(string json);

        /// <summary>
        /// Parses a TeleSign PhoneID Contact JSON response into a rich object.
        /// </summary>
        /// <param name="json">The json string containing the response.</param>
        /// <returns>A PhoneIdContactResponse object populated with the data from the response.</returns>
        PhoneIdContactResponse ParsePhoneIdContactResponse(string json);
    }
}
