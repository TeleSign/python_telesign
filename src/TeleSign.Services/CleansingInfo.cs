//-----------------------------------------------------------------------
// <copyright file="CleansingInfo.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    /// <summary>
    /// Represents information about a cleansed number.
    /// </summary>
    public class CleansingInfo
    {
        /// <summary>
        /// Initializes a new instance of the CleansingInfo class.
        /// </summary>
        public CleansingInfo()
        {
            this.PhoneNumber = string.Empty;
            this.CountryCode = string.Empty;
            this.MinLength = -1;
            this.MaxLength = -1;
            this.CleanseCode = CleansingCode.None;
        }

        /// <summary>
        /// Gets or sets the phone number without the country code.
        /// </summary>
        public string PhoneNumber { get; set; }

        /// <summary>
        /// Gets or sets the country code of the phone number.
        /// </summary>
        public string CountryCode { get; set; }

        /// <summary>
        /// Gets or sets the minimum valid length of a phone number in this country/area.
        /// </summary>
        public int MinLength { get; set; }

        /// <summary>
        /// Gets or sets the maximum valid length of a phone number in this country/area.
        /// </summary>
        public int MaxLength { get; set; }

        /// <summary>
        /// Gets or sets a code indicating what cleansing action was taken.
        /// TODO: Enum?
        /// </summary>
        public CleansingCode CleanseCode { get; set; }
    }
}
