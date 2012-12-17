//-----------------------------------------------------------------------
// <copyright file="PhoneIdService.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    using System;

    /// <summary>
    /// The TeleSign PhoneID service. This provides 3 services. PhoneID Contact, 
    /// PhoneID Standard and PhoneID Score. TODO: Link to other documentation or more detail here?
    /// </summary>
    public class PhoneIdService : RawPhoneIdService
    {
        /// <summary>
        /// The parser that transforms the raw JSON responses
        /// </summary>
        private IPhoneIdResponseParser responseParser;

        /// <summary>
        /// Initializes a new instance of the PhoneIdService class with
        /// configuration.
        /// </summary>
        /// <param name="configuration">The configuration information for the service.</param>
        public PhoneIdService(TeleSignServiceConfiguration configuration)
            : this(configuration, null, new JsonDotNetPhoneIdResponseParser())
        {
        }

        /// <summary>
        /// Initializes a new instance of the PhoneIdService class with
        /// a configuration and a custom web requester and response parser. 
        /// You generally don't need to use this constructor.
        /// </summary>
        /// <param name="configuration">The configuration information for the service.</param>
        /// <param name="webRequester">The web requester to use.</param>
        /// <param name="responseParser">The response parser to use.</param>
        public PhoneIdService(
                    TeleSignServiceConfiguration configuration, 
                    IWebRequester webRequester,
                    IPhoneIdResponseParser responseParser)
            : base(configuration, webRequester)
        {
            // TODO: null check and possible ifdef for JSON.Net
            this.responseParser = responseParser;
        }

        /// <summary>
        /// Performs a PhoneId Standard lookup on a phone number.
        /// </summary>
        /// <param name="phoneNumber">The phone number to lookup.</param>
        /// <returns>
        /// A StandardPhoneIdResponse object containing both status of the transaction
        /// and the resulting data (if successful).
        /// </returns>
        public PhoneIdStandardResponse StandardLookup(string phoneNumber)
        {
            CheckArgument.NotNullOrEmpty(phoneNumber, "phoneNumber");

            string rawResponse = this.StandardLookupRaw(phoneNumber);

            try
            {
                return this.responseParser.ParsePhoneIdStandardResponse(rawResponse);
            }
            catch (Exception x)
            {
                throw new ResponseParseException(
                            "Error parsing PhoneID Standard response",
                            rawResponse,
                            x);
            }
        }

        /// <summary>
        /// Performs a PhoneID Contact lookup on a phone number.
        /// </summary>
        /// <param name="phoneNumber">The phone number to lookup.</param>
        /// <returns>
        /// A ContactPhoneIdResponse object containing both status of the transaction
        /// and the resulting data (if successful).
        /// </returns>
        public PhoneIdContactResponse ContactLookup(string phoneNumber)
        {
            CheckArgument.NotNullOrEmpty(phoneNumber, "phoneNumber");

            string rawResponse = this.ContactLookupRaw(phoneNumber);

            try
            {
                return this.responseParser.ParsePhoneIdContactResponse(rawResponse);
            }
            catch (Exception x)
            {
                throw new ResponseParseException(
                            "Error parsing PhoneID Contact response",
                            rawResponse,
                            x);
            }
        }

        /// <summary>
        /// Performs a PhoneID Score lookup on a phone number.
        /// </summary>
        /// <param name="phoneNumber">The phone number to lookup.</param>
        /// <returns>
        /// A ScorePhoneIdResponse object containing both status of the transaction
        /// and the resulting data (if successful).
        /// </returns>
        public PhoneIdScoreResponse ScoreLookup(string phoneNumber)
        {
            CheckArgument.NotNullOrEmpty(phoneNumber, "phoneNumber");

            string rawResponse = this.ScoreLookupRaw(phoneNumber);

            try
            {
                return this.responseParser.ParsePhoneIdScoreResponse(rawResponse);
            }
            catch (Exception x)
            {
                throw new ResponseParseException(
                            "Error parsing Phone Id Score",
                            rawResponse,
                            x);
            }
        }

        /// <summary>
        /// Performs a PhoneID Live lookup on a phone number.
        /// </summary>
        /// <param name="phoneNumber">The phone number to lookup.</param>
        /// <returns>
        /// A PhoneIdLiveResponse object containing both status of the transaction
        /// and the resulting data (if successful).
        /// </returns>
        public PhoneIdLiveResponse LiveLookup(string phoneNumber)
        {
            CheckArgument.NotNullOrEmpty(phoneNumber, "phoneNumber");

            string rawResponse = this.LiveLookupRaw(phoneNumber);

            try
            {
                return this.responseParser.ParsePhoneIdLiveResponse(rawResponse);
            }
            catch (Exception x)
            {
                throw new ResponseParseException(
                            "Error parsing Phone Id Live",
                            rawResponse,
                            x);
            }
        }
    }
}
