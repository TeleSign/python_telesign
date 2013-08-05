//-----------------------------------------------------------------------
// <copyright file="RawPhoneIdService.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    using System;
    using System.Collections.Generic;
    using System.Globalization;
    using System.IO;
    using System.Net;

    /// <summary>
    /// <para>
    /// The raw TeleSign PhoneID service. This class builds and makes requests to the
    /// TeleSign service and returns the raw JSON responses that the REST service
    /// returns. 
    /// </para>
    /// <para>
    /// In most cases you should use PhoneIdService class instead which will parse the
    /// JSON responses into .NET objects that you can use. 
    /// </para>
    /// </summary>
    public class RawPhoneIdService : TeleSignService
    {
        /// <summary>
        /// Format string for PhoneId Standard request uri. The phone number is
        /// filled into the format field.
        /// </summary>
        private const string StandardResourceFormatString = "/v1/phoneid/standard/{0}";

        /// <summary>
        /// Format string for PhoneId Contact request uri. The phone number is
        /// filled into the format field.
        /// </summary>
        private const string ContactResourceFormatString = "/v1/phoneid/contact/{0}";

        /// <summary>
        /// Format string for PhoneId Score request uri. The phone number is
        /// filled into the format field.
        /// </summary>
        private const string ScoreResourceFormatString = "/v1/phoneid/score/{0}";

        /// <summary>
        /// Format string for PhoneId Live request uri. The phone number is
        /// filled into the format field.
        /// </summary>
        private const string LiveResourceFormatString = "/v1/phoneid/live/{0}";

        /// <summary>
        /// The default value for a use case id if not specified.
        /// </summary>
        private const string DefaultUseCaseId = "othr";

        /// <summary>
        /// Initializes a new instance of the RawPhoneIdService class with a supplied credential and uri.
        /// </summary>
        /// <param name="configuration">The configuration information for the service.</param>
        public RawPhoneIdService()
            : this("default")
        {
        }

        /// <summary>
        /// Initializes a new instance of the RawPhoneIdService class with a supplied credential and uri.
        /// </summary>
        /// <param name="configuration">The configuration information for the service.</param>
        public RawPhoneIdService(string accountName)
            : base(null, null, accountName)
        {
        }

        /// <summary>
        /// Initializes a new instance of the RawPhoneIdService class with a supplied credential and uri.
        /// </summary>
        /// <param name="configuration">The configuration information for the service.</param>
        public RawPhoneIdService(TeleSignServiceConfiguration configuration)
            : this(configuration, null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the RawPhoneIdService class with a supplied credential and uri and
        /// a web requester. In general you do not need to use this constructor unless you want to intercept
        /// the web requests for logging/debugging/testing purposes.
        /// </summary>
        /// <param name="configuration">The configuration information for the service.</param>
        /// <param name="webRequester">The web requester to use.</param>
        public RawPhoneIdService(
                    TeleSignServiceConfiguration configuration, 
                    IWebRequester webRequester)
            : base(configuration, webRequester)
        {
        }

        /// <summary>
        /// Performs a TeleSign PhoneID Standard lookup. This product provides information
        /// about the location the phone was registered, the type of phone (mobile, fixed,
        /// VOIP, etc).
        /// </summary>
        /// <param name="phoneNumber">The phone number to lookup.</param>
        /// <param name="useCaseId">The use case for the lookup. (Restricted set of values).</param>
        /// <returns>The raw JSON string response.</returns>
        public string StandardLookupRaw(
                    string phoneNumber,
                    string useCaseId = RawPhoneIdService.DefaultUseCaseId)
        {
            phoneNumber = this.CleanupPhoneNumber(phoneNumber);

            string resourceName = string.Format(
                        CultureInfo.InvariantCulture,
                        RawPhoneIdService.StandardResourceFormatString, 
                        phoneNumber);

            // Use Case Id (ucid) is not current required in calls to standard but may be
            // in future.
            Dictionary<string, string> additionalFields = new Dictionary<string, string>() 
            { 
                { "ucid", useCaseId },
            };

            WebRequest request = this.ConstructWebRequest(
                        resourceName,
                        "GET",
                        additionalFields);

            return this.WebRequester.ReadResponseAsString(request);
        }

        /// <summary>
        /// Performs a TeleSign PhoneID Contact lookup. This product provides all the
        /// information that is provided by PhoneID Standard as well as additional
        /// information about the owner of the phone such as name and address.
        /// </summary>
        /// <param name="phoneNumber">The phone number to lookup.</param>
        /// <param name="useCaseId">The use case for the lookup. (Restricted set of values).</param>
        /// <returns>The raw JSON string response.</returns>
        public string ContactLookupRaw(
                    string phoneNumber, 
                    string useCaseId = RawPhoneIdService.DefaultUseCaseId)
        {
            phoneNumber = this.CleanupPhoneNumber(phoneNumber);

            string resourceName = string.Format(
                        CultureInfo.InvariantCulture,
                        RawPhoneIdService.ContactResourceFormatString, 
                        phoneNumber);

            // Use Case Id (ucid) is required in calls to contact.
            Dictionary<string, string> additionalFields = new Dictionary<string, string>() 
            { 
                { "ucid", useCaseId } 
            };

            WebRequest request = this.ConstructWebRequest(
                        resourceName,
                        "GET",
                        additionalFields);

            return this.WebRequester.ReadResponseAsString(request);
        }

        /// <summary>
        /// Performs a TeleSign PhoneID Score lookup. This product provides all the
        /// information that is provided by PhoneID standard as well as a risk
        /// value.
        /// </summary>
        /// <param name="phoneNumber">The phone number to lookup.</param>
        /// <param name="useCaseId">The use case for the lookup. (Restricted set of values).</param>
        /// <returns>The raw JSON string response.</returns>
        public string ScoreLookupRaw(
                    string phoneNumber,
                    string useCaseId = RawPhoneIdService.DefaultUseCaseId)
        {
            phoneNumber = this.CleanupPhoneNumber(phoneNumber);

            string resourceName = string.Format(
                        CultureInfo.InvariantCulture,
                        RawPhoneIdService.ScoreResourceFormatString,
                        phoneNumber);

            // Use Case Id (ucid) is required in calls to score.
            Dictionary<string, string> additionalFields = new Dictionary<string, string>() 
            { 
                { "ucid", useCaseId } 
            };

            WebRequest request = this.ConstructWebRequest(
                        resourceName,
                        "GET",
                        additionalFields);

            return this.WebRequester.ReadResponseAsString(request);
        }

        /// <summary>
        /// Performs a TeleSign PhoneID Live lookup. This product provides all the
        /// information that is provided by PhoneID standard as well as additional
        /// roaming and phone status information.
        /// </summary>
        /// <param name="phoneNumber">The phone number to lookup.</param>
        /// <param name="useCaseId">The use case for the lookup. (Restricted set of values).</param>
        /// <returns>The raw JSON string response.</returns>
        public string LiveLookupRaw(
                    string phoneNumber,
                    string useCaseId = RawPhoneIdService.DefaultUseCaseId)
        {
            phoneNumber = this.CleanupPhoneNumber(phoneNumber);

            string resourceName = string.Format(
                        CultureInfo.InvariantCulture,
                        RawPhoneIdService.LiveResourceFormatString,
                        phoneNumber);

            // Use Case Id (ucid) is required in calls to live.
            Dictionary<string, string> additionalFields = new Dictionary<string, string>() 
            { 
                { "ucid", useCaseId } 
            };

            WebRequest request = this.ConstructWebRequest(
                        resourceName,
                        "GET",
                        additionalFields);

            return this.WebRequester.ReadResponseAsString(request);
        }
    }
}
