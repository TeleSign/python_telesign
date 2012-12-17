//-----------------------------------------------------------------------
// <copyright file="AuthenticationMethod.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    using System;

    /// <summary>
    /// Refers to the strength of the encryption method used in message authentication.
    /// Encryption produces a Hash-based Message Authentication Code (HMAC) using one of two 
    /// Secure Hash Algorithms (SHA-1 and SHA-2).
    /// </summary>
    public enum AuthenticationMethod
    {
        /// <summary>
        /// Do not use Hash-based Message Authentication. Default.
        /// </summary>
        None,

        /// <summary>
        /// Encrypt the message into a 160-bit hash value using the SHA-1 cryptographic function.
        /// </summary>
        HmacSha1,

        /// <summary>
        /// Encrypt the message into a stronger 256-bit hash value using the SHA-2 cryptographic function.
        /// </summary>
        HmacSha256,
    }
}
