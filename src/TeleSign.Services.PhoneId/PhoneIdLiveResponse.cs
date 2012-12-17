//-----------------------------------------------------------------------
// <copyright file="PhoneIdLiveResponse.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    /// <summary>
    /// <para>
    /// The response object from a TeleSign PhoneId Live API call.
    /// </para>
    /// <para>
    /// This contains all the same information as a PhoneId standard
    /// response as well as Live information about the device
    /// and subscriber status.
    /// </para>
    /// </summary>
    public class PhoneIdLiveResponse : PhoneIdStandardResponse
    {
        /// <summary>
        /// Initializes a new instance of the PhoneIdLiveResponse class.
        /// </summary>
        public PhoneIdLiveResponse()
            : this(null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the PhoneIdLiveResponse class providing
        /// the raw JSON response string.
        /// </summary>
        /// <param name="rawResponse">The raw JSON response string returned from the REST service.</param>
        public PhoneIdLiveResponse(string rawResponse)
            : base(rawResponse)
        {
            this.Live = new LiveInfo();
        }

        /// <summary>
        /// Gets or sets the live information about the roaming, subscriber and
        /// device status.
        /// </summary>
        public LiveInfo Live { get; set; }
    }
}