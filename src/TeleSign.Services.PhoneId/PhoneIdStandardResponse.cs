//-----------------------------------------------------------------------
// <copyright file="PhoneIdStandardResponse.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    using System;

    /// <summary>
    /// <para>
    /// The response information for a TeleSign PhoneID Standard
    /// API call.
    /// </para>
    /// <para>
    /// As well as the default status information contained in all
    /// TeleSignResponse derived classes, a PhoneID Standard response
    /// includes information about the location the phone is registered
    /// (note that this is not the location where the owner of the phone
    /// lives - PhoneID Contact should be used to obtain that information).
    /// </para>
    /// <para>
    /// It also contains information rhe original number which
    /// will be returned in both a combined and split format with the
    /// country code separated from the rest of the number.
    /// </para>
    /// <para>
    /// Two cleansed fields will be returned. One for voice calls, 
    /// one for sms. These versions of the number have been "cleansed"
    /// and may be different from the original number. TODO: What info
    /// about cleansing should be put here.
    /// </para>
    /// <para>
    /// Additionally a phone type is returned. This contains information
    /// about the type of phone - such as mobile, landline, VOIP, etc.
    /// </para>
    /// </summary>
    public class PhoneIdStandardResponse : CommonPhoneIdResponse
    {
        /// <summary>
        /// Initializes a new instance of the PhoneIdStandardResponse class.
        /// </summary>
        public PhoneIdStandardResponse()
            : this(null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the PhoneIdStandardResponse class providing
        /// the raw JSON response string.
        /// </summary>
        /// <param name="rawResponse">The raw JSON response string returned from the REST service.</param>
        public PhoneIdStandardResponse(string rawResponse)
            : base(rawResponse)
        {
            this.Location = new LocationInfo();
            this.PhoneType = new PhoneTypeInfo();
        }

        /// <summary>
        /// Gets or sets location information about the registration of the phone number.
        /// </summary>
        public LocationInfo Location { get; set; }

        /// <summary>
        /// Gets or sets the phone type.
        /// </summary>
        public PhoneTypeInfo PhoneType { get; set; }
    }
}
