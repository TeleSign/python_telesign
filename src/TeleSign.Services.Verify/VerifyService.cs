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
        
        /////// <summary>
        /////// The TeleSign Verify Soft Token web service is a server-side component of the TeleSign AuthID application, and it allows you to authenticate your end users when they use the TeleSign AuthID application on their mobile device to generate a Time-based One-time Password (TOTP) verification code
        /////// </summary>
        /////// <param name="phoneNumber">The phone number for the Verify Soft Token request, including country code</param>
        /////// <param name="softTokenId">
        /////// The alphanumeric string that uniquely identifies your TeleSign soft token subscription
        /////// </param>
        /////// <param name="verifyCode">
        /////// The verification code received from the end user
        /////// </param>
        /////// <returns>The raw JSON response from the REST API.</returns>
        ////public VerifyResponse SendSoftToken(
        ////            string phoneNumber,
        ////            string softTokenId = null,
        ////            string verifyCode = null)
        ////{
        ////    phoneNumber = this.CleanupPhoneNumber(phoneNumber);

        ////    string rawResponse = this.SoftTokenRaw(
        ////                phoneNumber,
        ////                softTokenId,
        ////                verifyCode);

        ////    try
        ////    {
        ////        return this.parser.ParseVerifyResponse(rawResponse);
        ////    }
        ////    catch (Exception x)
        ////    {
        ////        throw new ResponseParseException(
        ////                    "Error parsing Verify SoftToken response",
        ////                    rawResponse,
        ////                    x);
        ////    }
        ////}
        
        /// <summary>
        /// The TeleSign Verify 2-Way SMS web service allows you to authenticate your users and verify user transactions via two-way Short Message Service (SMS) wireless communication. Verification requests are sent to user’s in a text message, and users return their verification responses by replying to the text message.
        /// </summary>
        /// <param name="phoneNumber">The phone number for the Verify Soft Token request, including country code</param>
        /// <param name="ucid">
        /// A string specifying one of the Use Case Codes
        /// </param>
        /// <param name="message">
        /// The text to display in the body of the text message. You must include the $$CODE$$ placeholder for the verification code somewhere in your message text. TeleSign automatically replaces it with a randomly-generated verification code
        /// </param>
        /// <param name="validityPeriod">
        /// This parameter allows you to place a time-limit on the verification. This provides an extra level of security by restricting the amount of time your end user has to respond (after which, TeleSign automatically rejects their response). Values are expressed as a natural number followed by a lower-case letter that represents the unit of measure. You can use 's' for seconds, 'm' for minutes, 'h' for hours, and 'd' for days
        /// </param>
        /// <returns>The raw JSON response from the REST API.</returns>
        public VerifyResponse SendTwoWaySms(
        			string phoneNumber,
                    string ucid,
                    string message = null,
            		string validityPeriod = null)
        {
            phoneNumber = this.CleanupPhoneNumber(phoneNumber);

            string rawResponse = this.TwoWaySmsRaw(
                        phoneNumber,
                        ucid,
                        message,
            			validityPeriod);

            try
            {
                return this.parser.ParseVerifyResponse(rawResponse);
            }
            catch (Exception x)
            {
                throw new ResponseParseException(
                            "Error parsing Verify TwoWaySms response",
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
        public VerifyResponse InitiatePush(
                    string phoneNumber,
                    string verifyCode = null)
        {
            string rawResponse = this.PushRaw(
                        phoneNumber,
                        verifyCode);

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
