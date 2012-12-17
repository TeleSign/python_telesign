//-----------------------------------------------------------------------
// <copyright file="NumberingInfo.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    /// <summary>
    /// Contains the whole number and also separates the country code
    /// from the rest of the number. All the values are strings - however
    /// they contain all digits. No other punctuation characters such as dashes,
    /// plus signs or parenthesis are here.
    /// </summary>
    public class NumberingInfo
    {
        /// <summary>
        /// Initializes a new instance of the NumberingInfo class.
        /// </summary>
        public NumberingInfo()
        {
            this.PhoneNumber = string.Empty;
            this.CompletePhoneNumber = string.Empty;
            this.CountryCode = string.Empty;
        }

        /// <summary>
        /// Gets or sets the phone number (not including the country code).
        /// </summary>
        /// <value>The phone number (not including the country code).</value>
        public string PhoneNumber { get; set; }

        /// <summary>
        /// Gets or sets the complete phone number including the country code.
        /// </summary>
        /// <value>The complete phone number including the country code.</value>
        public string CompletePhoneNumber { get; set; }

        /// <summary>
        /// Gets or sets the country code for the phone number.
        /// </summary>
        /// <value>The country code for the phone number.</value>
        public string CountryCode { get; set; }
    }
}
