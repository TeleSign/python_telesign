//-----------------------------------------------------------------------
// <copyright file="LocationInfo.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    /// <summary>
    /// <para>
    /// The location associated with the registration of the phone number.
    /// This is location information about the phone not the owner of the
    /// phone and is returned as part of all PhoneId products.
    /// </para>
    /// <para>
    /// Note that this is not the same as the Contact class which contains
    /// name and address information about the owner of the phone.
    /// </para>
    /// </summary>
    public class LocationInfo
    {
        /// <summary>
        /// Initializes a new instance of the LocationInfo class.
        /// </summary>
        public LocationInfo()
        {
            this.City = string.Empty;
            this.County = string.Empty;
            this.State = string.Empty;
            this.TimeZoneRange = new TimeZoneRange();
            this.Coordinates = new Coordinates();
            this.Country = new Country();
            this.MetroCode = string.Empty;
            this.Zip = string.Empty;
        }

        /// <summary>
        /// Gets or sets the city associated with this phones registration.
        /// </summary>
        public string City { get; set; }

        /// <summary>
        /// Gets or sets the zip code associated with this phones registration.
        /// </summary>
        public string Zip { get; set; }

        /// <summary>
        /// Gets or sets the country information associated with this phones registration.
        /// </summary>
        public Country Country { get; set; }

        /// <summary>
        /// Gets or sets the time zone range associated with this phones registration.
        /// </summary>
        public TimeZoneRange TimeZoneRange { get; set; }

        /// <summary>
        /// Gets or sets the coordinates associated with this phones registration.
        /// </summary>
        public Coordinates Coordinates { get; set; }

        /// <summary>
        /// Gets or sets the metro-code associated with this phones registration. This
        /// value is only applicable to US numbers.
        /// </summary>
        public string MetroCode { get; set; }

        /// <summary>
        /// Gets or sets the county associated with this phones registration. This
        /// value is only application to US numbers. TODO: True?
        /// </summary>
        public string County { get; set; }

        /// <summary>
        /// Gets or sets the state/province associated with this phones registration.
        /// </summary>
        public string State { get; set; }
    }
}
