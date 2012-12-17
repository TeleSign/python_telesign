//-----------------------------------------------------------------------
// <copyright file="CommonPhoneIdResponse.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    using System;

    /// <summary>
    /// <para>
    /// The common response information for a TeleSign PhoneID API calls.
    /// </para>
    /// <para>
    /// As well as the default status information contained in all
    /// TeleSignResponse derived classes it also contains information 
    /// about the original number which will be returned in both 
    /// a combined and split format with the
    /// country code separated from the rest of the number.
    /// </para>
    /// <para>
    /// Two cleansed fields will be returned. One for voice calls, 
    /// one for sms. These versions of the number have been "cleansed"
    /// and may be different from the original number. TODO: What info
    /// about cleansing should be put here.
    /// </para>
    /// </summary>
    public abstract class CommonPhoneIdResponse : TeleSignResponse
    {
        /// <summary>
        /// Initializes a new instance of the CommonPhoneIdResponse class.
        /// </summary>
        protected CommonPhoneIdResponse()
            : this(null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the CommonPhoneIdResponse class providing
        /// the raw JSON response string.
        /// </summary>
        /// <param name="rawResponse">The raw JSON response string returned from the REST service.</param>
        protected CommonPhoneIdResponse(string rawResponse)
            : base(rawResponse)
        {
        }

        /// <summary>
        /// Gets or sets the original phone number information.
        /// </summary>
        public NumberingInfo OriginalNumber { get; set; }

        /// <summary>
        /// Gets or sets the cleansing information for voice calls.
        /// </summary>
        public CleansingInfo CallCleansedNumber { get; set; }

        /// <summary>
        /// Gets or sets the cleansing information for sms.
        /// </summary>
        public CleansingInfo SmsCleansedNumber { get; set; }
    }
}
