//-----------------------------------------------------------------------
// <copyright file="PhoneIdScoreResponse.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    /// <summary>
    /// <para>
    /// The response object from a TeleSign PhoneId Score API call.
    /// </para>
    /// <para>
    /// This contains all the same information as a PhoneId standard
    /// response as well as Risk information about the risk level
    /// of the transaction.
    /// </para>
    /// </summary>
    public class PhoneIdScoreResponse : CommonPhoneIdResponse
    {
        /// <summary>
        /// Initializes a new instance of the PhoneIdScoreResponse class.
        /// </summary>
        public PhoneIdScoreResponse()
            : this(null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the PhoneIdScoreResponse class providing
        /// the raw JSON response string.
        /// </summary>
        /// <param name="rawResponse">The raw JSON response string returned from the REST service.</param>
        public PhoneIdScoreResponse(string rawResponse)
            : base(rawResponse)
        {
            this.Risk = new RiskInfo();
        }

        /// <summary>
        /// Gets or sets the risk information about the owner
        /// of the phone.
        /// </summary>
        public RiskInfo Risk { get; set; }
    }
}