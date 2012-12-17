//-----------------------------------------------------------------------
// <copyright file="Coordinates.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    /// <summary>
    /// Represents a location on the earth in longitude and latitude.
    /// </summary>
    public class Coordinates
    {
        /// <summary>
        /// Initializes a new instance of the Coordinates class.
        /// </summary>
        public Coordinates()
        {
            this.Latitude = 0;
            this.Longitude = 0;
        }

        /// <summary>
        /// Gets or sets the latitude coordinate.
        /// </summary>
        public double Latitude { get; set; }

        /// <summary>
        /// Gets or sets the longitude coordinate.
        /// </summary>
        public double Longitude { get; set; }
    }
}
