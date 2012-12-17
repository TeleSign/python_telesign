//-----------------------------------------------------------------------
// <copyright file="Country.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    /// <summary>
    /// Represents name and identifiers of a country.
    /// </summary>
    public class Country
    {
        /// <summary>
        /// Initializes a new instance of the Country class.
        /// </summary>
        public Country()
        {
            this.Name = string.Empty;
            this.Iso2 = string.Empty;
            this.Iso3 = string.Empty;
        }

        /// <summary>
        /// Gets or sets the name of the country.
        /// </summary>
        public string Name { get; set; }

        /// <summary>
        /// Gets or sets the ISO2 country code.
        /// </summary>
        public string Iso2 { get; set; }

        /// <summary>
        /// Gets or sets the ISO3 country code.
        /// </summary>
        public string Iso3 { get; set; }
    }
}
