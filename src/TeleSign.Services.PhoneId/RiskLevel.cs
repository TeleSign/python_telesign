//-----------------------------------------------------------------------
// <copyright file="RiskLevel.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    /// <summary>
    /// The level of risk of processing a transaction with the specified phone number.
    /// </summary>
    public enum RiskLevel
    {
        /// <summary>
        /// The default value for the enum. Not a valid value.
        /// </summary>
        None,

        /// <summary>
        /// Low risk transaction.
        /// </summary>
        Low,

        /// <summary>
        /// Medium-low risk transaction.
        /// </summary>
        MediumLow,

        /// <summary>
        /// Medium risk transaction.
        /// </summary>
        Medium,

        /// <summary>
        /// Medium-high risk transaction.
        /// </summary>
        MediumHigh,

        /// <summary>
        /// High risk transaction.
        /// </summary>
        High,

        /// <summary>
        /// No specific risk information.
        /// </summary>
        Neutral,

        /// <summary>
        /// An unparsable value. This is used when the parser cannot interpret the response
        /// from the REST API such as could happen if the REST API changes.
        /// </summary>
        Other = int.MaxValue,
    }
}
