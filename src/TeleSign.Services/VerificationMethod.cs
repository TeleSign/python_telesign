//-----------------------------------------------------------------------
// <copyright file="VerificationMethod.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    /// <summary>
    /// The method used for TeleSign Verification. Currently either
    /// voice call or sms.
    /// </summary>
    public enum VerificationMethod
    {
        /// <summary>
        /// No verification method. Not a valid value.
        /// </summary>
        None,

        /// <summary>
        /// Verify by voice call.
        /// </summary>
        Call,

        /// <summary>
        /// Verify by sms.
        /// </summary>
        Sms,
    }
}
