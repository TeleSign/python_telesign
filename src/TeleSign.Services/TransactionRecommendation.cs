//-----------------------------------------------------------------------
// <copyright file="TransactionRecommendation.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    /// <summary>
    /// The recommendation for a transaction.
    /// Determined based on risk.
    /// </summary>
    public enum TransactionRecommendation
    {
        /// <summary>
        /// This is the default value.
        /// </summary>
        None,

        /// <summary>
        /// Recommendation is to block this transaction.
        /// </summary>
        Block,

        /// <summary>
        /// Recommendation is to flag this transaction for further inquiry.
        /// </summary>
        Flag,

        /// <summary>
        /// Recommendation is to allow this transaction.
        /// </summary>
        Allow,

        /// <summary>
        /// A recommendation was not applicable.
        /// </summary>
        NotApplicable,

        /// <summary>
        /// Unparsable value. The REST API returned an unknown recommendation string.
        /// </summary>
        Other = int.MaxValue,
    }
}
