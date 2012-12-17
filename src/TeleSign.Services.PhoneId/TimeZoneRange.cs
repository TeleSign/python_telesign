//-----------------------------------------------------------------------
// <copyright file="TimeZoneRange.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    /// <summary>
    /// Represents a range of time zones that apply to an area via the minimum and maximum
    /// UTC offset.
    /// </summary>
    public class TimeZoneRange
    {
        /// <summary>
        /// Initializes a new instance of the TimeZoneRange class.
        /// </summary>
        public TimeZoneRange()
        {
            this.UtcOffsetMin = string.Empty;
            this.UtcOffsetMax = string.Empty;
            this.Name = string.Empty;
        }

        /// <summary>
        /// Gets or sets the minimum UTC offset in the range.
        /// </summary>
        /// <value>The minimum UTC offset in the range.</value>
        public string UtcOffsetMin { get; set; }

        /// <summary>
        /// Gets or sets the maximum UtcOffset in the range.
        /// </summary>
        /// <value>The maximum UtcOffset in the range.</value>
        public string UtcOffsetMax { get; set; }

        /// <summary>
        /// Gets or sets the name of the time zone range.
        /// </summary>
        /// <value>The name of the time zone range.</value>
        public string Name { get; set; }
    }
}
