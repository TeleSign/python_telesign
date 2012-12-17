//-----------------------------------------------------------------------
// <copyright file="CodeState.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.Verify
{
    using System;

    /// <summary>
    /// The state of the code in a verify transaction.
    /// </summary>
    public enum CodeState
    {
        /// <summary>
        /// This is the default value.
        /// </summary>
        None,

        /// <summary>
        /// The code provided to the verify API was valid.
        /// </summary>
        Valid,

        /// <summary>
        /// The code provided to the verify API was invalid.
        /// </summary>
        Invalid,

        /// <summary>
        /// The code has not yet been provided to the verify API.
        /// </summary>
        Unknown,

        /// <summary>
        /// Some other value was returned. This may occur due to
        /// extension of the API when using an older version
        /// of the SDK. You can check the raw value.
        /// </summary>
        Other,
    }
}
