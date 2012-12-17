//-----------------------------------------------------------------------
// <copyright file="VerifyResponse.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.Verify
{
    /// <summary>
    /// The response to a TeleSign Verify API call. Contains the status information
    /// common to all TeleSign API calls and a VerifyInfo object which contains
    /// information about whether the code entered is valid, invalid or not
    /// checked yet.
    /// </summary>
    public class VerifyResponse : TeleSignResponse
    {
        /// <summary>
        /// Initializes a new instance of the VerifyResponse class.
        /// </summary>
        public VerifyResponse()
            : this(null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the VerifyResponse class providing
        /// the raw JSON response string.
        /// </summary>
        /// <param name="rawResponse">The raw JSON response string returned from the REST service.</param>
        public VerifyResponse(string rawResponse)
            : base(rawResponse)
        {
            this.VerifyInfo = new VerifyInfo();
        }

        /// <summary>
        /// Gets or sets the information about the state of the verification process.
        /// </summary>
        public VerifyInfo VerifyInfo { get; set; }
    }
}
