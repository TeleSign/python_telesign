//-----------------------------------------------------------------------
// <copyright file="VerifyService.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.Verify
{
    using System;

    /// <summary>
    /// The TeleSign Verify service.
    /// </summary>
    public class VerifyService : RawVerifyService
    {
        /// <summary>
        /// The parser used to transform the raw JSON string responses to rich .NET objects.
        /// </summary>
        private IVerifyResponseParser parser;

        /// <summary>
        /// Initializes a new instance of the VerifyService class with a supplied credential and URI.
        /// </summary>
        /// <param name="configuration">The configuration information for the service.</param>
        public VerifyService(TeleSignServiceConfiguration configuration)
            : this(
                        configuration, 
                        null, 
                        new JsonDotNetVerifyResponseParser())
        {
        }

        /// <summary>
        /// Initializes a new instance of the VerifyService class with a supplied credential and uri and
        /// a web requester. In general you do not need to use this constructor unless you want to intercept
        /// the web requests for logging/debugging/testing purposes.
        /// </summary>
        /// <param name="configuration">The configuration information for the service.</param>
        /// <param name="webRequester">The web requester to use.</param>
        /// <param name="responseParser">The parse to use for parsing JSON responses.</param>
        public VerifyService(
                    TeleSignServiceConfiguration configuration, 
                    IWebRequester webRequester,
                    IVerifyResponseParser responseParser)
            : base(configuration, webRequester)
        {
            this.parser = responseParser;
        }

        /// <summary>
        /// Initiates a TeleSign Verify transaction using SMS. The SMS will use the default
        /// US English message template and the API will generate the code for you.
        /// </summary>
        /// <param name="phoneNumber">The phone number to send the sms to.</param>
        /// <returns>
        /// A VerifyResponse object with the status and returned information
        /// for the transaction.
        /// </returns>
        public VerifyResponse SendSms(string phoneNumber)
        {
            return this.SendSms(
                        phoneNumber,
                        null,
                        null,
                        null);
        }

        /// <summary>
        /// Initiates a TeleSign Verify transaction using SMS. The SMS will use the default
        /// US English message template and the code you provide.
        /// </summary>
        /// <param name="phoneNumber">The phone number to send the sms to.</param>
        /// <param name="verifyCode">
        /// The code to send to the user. When null a code will
        /// be generated for you.
        /// </param>
        /// <returns>
        /// A VerifyResponse object with the status and returned information
        /// for the transaction.
        /// </returns>
        public VerifyResponse SendSms(
                    string phoneNumber, 
                    string verifyCode)
        {
            return this.SendSms(
                        phoneNumber, 
                        verifyCode,
                        null,
                        null);
        }

        /// <summary>
        /// Initiates a TeleSign Verify transaction using SMS. The SMS will use the default
        /// message template and the code you provide.
        /// </summary>
        /// <param name="phoneNumber">The phone number to send the sms to.</param>
        /// <param name="verifyCode">
        /// The code to send to the user. When null a code will
        /// be generated for you.
        /// </param>
        /// <param name="language">
        /// The language that the message should be in.
        /// TODO: Details about  language string format.
        /// </param>
        /// <returns>
        /// A VerifyResponse object with the status and returned information
        /// for the transaction.
        /// </returns>
        public VerifyResponse SendSms(
                    string phoneNumber,
                    string verifyCode,
                    string language)
        {
            return this.SendSms(
                        phoneNumber, 
                        verifyCode, 
                        null, 
                        language);
        }

        /// <summary>
        /// Initiates a TeleSign Verify transaction using SMS. The SMS will use the default
        /// message template and the code you provide.
        /// </summary>
        /// <param name="phoneNumber">The phone number to send the sms to.</param>
        /// <param name="verifyCode">
        /// The code to send to the user. When null a code will
        /// be generated for you.
        /// </param>
        /// <param name="messageTemplate">
        /// A template for the message to be sent to the user. This string must be non-empty
        /// and contain the magic string $$CODE$$ which will be replaced by the
        /// verify code in the message.
        /// </param>
        /// <param name="language">
        /// The language that the message should be in. If a message template is specified
        /// language will be ignored.
        /// TODO: Details about  language string format.
        /// </param>
        /// <returns>
        /// A VerifyResponse object with the status and returned information
        /// for the transaction.
        /// </returns>
        public VerifyResponse SendSms(
                    string phoneNumber,
                    string verifyCode,
                    string messageTemplate,
                    string language)
        {
            phoneNumber = this.CleanupPhoneNumber(phoneNumber);
            this.ValidateCodeFormat(verifyCode);

            string rawResponse = this.SmsRaw(
                        phoneNumber,
                        verifyCode,
                        messageTemplate,
                        language);

            try
            {
                return this.parser.ParseVerifyResponse(rawResponse);
            }
            catch (Exception x)
            {
                throw new ResponseParseException(
                            "Error parsing Verify SMS response",
                            rawResponse,
                            x);
            }
        }

        /// <summary>
        /// Initiates a TeleSign Verify transaction via a voice call.
        /// </summary>
        /// <param name="phoneNumber">The phone number to call.</param>
        /// <param name="verifyCode">
        /// The code to send to the user. When null a code will
        /// be generated for you.
        /// </param>
        /// <param name="language">
        /// The language that the message should be in. This parameter is ignored if
        /// you supplied a message template.
        /// TODO: Details about language string format.
        /// </param>
        /// <returns>
        /// A VerifyResponse object with the status and returned information
        /// for the transaction.
        /// </returns>
        public VerifyResponse InitiateCall(
                    string phoneNumber,
                    string verifyCode = null,
                    string language = "en")
        {
            string rawResponse = this.CallRaw(
                        phoneNumber,
                        verifyCode,
                        language);

            try
            {
                return this.parser.ParseVerifyResponse(rawResponse);
            }
            catch (Exception x)
            {
                throw new ResponseParseException(
                            "Error parsing Verify call response",
                            rawResponse,
                            x);
            }
        }

        /// <summary>
        /// Validates the code provided by the user. After the code has been
        /// sent to the user, they enter the code to your website/application
        /// and you pass the code here to verify.
        /// </summary>
        /// <param name="referenceId">
        /// The reference id return in the VerifyResponse from
        /// a call to Sms or Call.
        /// </param>
        /// <param name="verifyCode">The code the user provided you to be verified.</param>
        /// <returns>
        /// A VerifyResponse object containing information about the status
        /// of the transactation and validity of the code.
        /// </returns>
        public VerifyResponse ValidateCode(
                    string referenceId,
                    string verifyCode)
        {
            string rawResponse = this.StatusRaw(
                        referenceId,
                        verifyCode);
            try
            {
                return this.parser.ParseVerifyResponse(rawResponse);
            }
            catch (Exception x)
            {
                throw new ResponseParseException(
                            "Error parsing Verify code validation response",
                            rawResponse,
                            x);
            }
        }

        /// <summary>
        /// Checks the status of TeleSign Verify transaction. At the underlying REST
        /// API layer this is the same call as ValidateCode (to the Status resource)
        /// but without supplying the code. This is useful to check the progress
        /// of the SMS or call prior to the user responding with the code.
        /// </summary>
        /// <param name="referenceId">
        /// The reference id return in the VerifyResponse from
        /// a call to Sms or Call.
        /// </param>
        /// <returns>
        /// A VerifyResponse object containing information about the status
        /// of the transactation
        /// </returns>
        public VerifyResponse CheckStatus(string referenceId)
        {
            CheckArgument.NotNullOrEmpty(referenceId, "referenceId");

            string rawResponse = this.StatusRaw(referenceId);

            try
            {
                return this.parser.ParseVerifyResponse(rawResponse);
            }
            catch (Exception x)
            {
                throw new ResponseParseException(
                            "Error parsing Verify code check status response",
                            rawResponse,
                            x);
            }
        }

        /// <summary>
        /// Validates whether a verifyCode is valid to use with the TeleSign API.
        /// Null is valid and indicates the API should generate the code itself,
        /// empty strings are not valid, any non-digit characters are not valid
        /// and leading zeros are not valid.
        /// </summary>
        /// <param name="verifyCode">The code to verify.</param>
        public virtual void ValidateCodeFormat(string verifyCode)
        {
            if (verifyCode == null)
            {
                // When the code is null we generate it, so this is valid.
                return;
            }

            // Empty code is never valid
            CheckArgument.NotEmpty(verifyCode, "verifyCode");

            // Leading zeros are not allowed.
            if (verifyCode[0] == '0')
            {
                string message = string.Format(
                            "Verify code '{0}' must not have leading zeroes.",
                            verifyCode);

                throw new ArgumentException(message);
            }

            foreach (char c in verifyCode)
            {
                // Only decimal digits are allowed 0-9.
                if (!Char.IsDigit(c))
                {
                    string message = string.Format(
                                "Verify code '{0}' must only contain decimal digits [0-9]",
                                verifyCode);

                    throw new ArgumentException(message);
                }
            }
        }
    }
}
