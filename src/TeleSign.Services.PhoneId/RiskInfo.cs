//-----------------------------------------------------------------------
// <copyright file="RiskInfo.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    /// <summary>
    /// <para>
    /// Represents the risk information associated with a phone number.
    /// Part of the PhoneId.Score
    /// Used to assess the 
    /// about the risk associated with accepting a transaction associated
    /// with this phone. This data is returned from PhoneID Score requests.
    /// </para>
    /// <para>
    /// A risk level, a recommendation and a numeric score 
    /// (TODO: higher or lower is better?).
    /// </para>
    /// </summary>
    public class RiskInfo
    {
        /// <summary>
        /// Initializes a new instance of the RiskInfo class.
        /// </summary>
        public RiskInfo()
        {
            this.Level = RiskLevel.None;
            this.Recommendation = TransactionRecommendation.None;
            this.Score = -1;
        }

        /// <summary>
        /// Gets or sets the risk level of this transaction.
        /// </summary>
        public RiskLevel Level { get; set; }

        /// <summary>
        /// Gets or sets the recommendation for this transaction.
        /// </summary>
        public TransactionRecommendation Recommendation { get; set; }

        /// <summary>
        /// Gets or sets the risk score for this transaction.
        /// </summary>
        public int Score { get; set; }
    }
}
