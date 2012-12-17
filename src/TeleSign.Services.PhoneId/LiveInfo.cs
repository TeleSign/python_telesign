//-----------------------------------------------------------------------
// <copyright file="LiveInfo.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    /// <summary>
    /// <para>
    /// Contains information about the status of the subscriber
    /// and device and roaming information.
    /// </para>
    /// </summary>
    public class LiveInfo
    {
        /// <summary>
        /// Initializes a new instance of the LiveInfo class.
        /// </summary>
        public LiveInfo()
        {
            this.SubscriberStatus = string.Empty;
            this.DeviceStatus = string.Empty;
            this.Roaming = string.Empty;
            this.RoamingCountry = string.Empty;
        }

        /// <summary>
        /// Gets or sets the subscriber status. One of ACTIVE, DISCONNECTED.
        /// </summary>
        public string SubscriberStatus { get; set; }

        /// <summary>
        /// Gets or sets the device status. One of REACHABLE,
        /// UNAVAILABLE or UNREACHABLE.
        /// </summary>
        public string DeviceStatus { get; set; }

        /// <summary>
        /// Gets or sets a value indicating whether the device is roaming.
        /// </summary>
        public string Roaming { get; set; }

        /// <summary>
        /// Gets or sets the roaming country. The country name or an empty string.
        /// </summary>
        public string RoamingCountry { get; set; }

        /// <summary>
        /// Gets a value indicating whether SubScriberStatus is active. Returns true if "ACTIVE" 
        /// and false if "DISCONNECTED".
        /// </summary>
        public bool IsSubscriberActive
        {
            get { return this.SubscriberStatus == "ACTIVE"; }
        }

        /// <summary>
        /// Gets a value indicating whether DeviceStatus is active. Returns true if "REACHABLE" 
        /// and false if "UNREACHABLE" or "UNAVAILABLE".
        /// </summary>
        public bool IsDeviceAvailable
        {
            get { return this.DeviceStatus == "REACHABLE"; }
        }

        /// <summary>
        /// Gets a value indicating whether roaming is enabled. Returns true if "YES" 
        /// and false if "NO" or "UNAVAILABLE".
        /// </summary>
        public bool IsRoaming
        {
            get { return this.Roaming == "YES"; }
        }
    }
}
