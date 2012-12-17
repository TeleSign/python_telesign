//-----------------------------------------------------------------------
// <copyright file="TeleSignApiError.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    /// <summary>
    /// Represents error information returned from the TeleSign web server.
    /// </summary>
    public class TeleSignApiError
    {
        /// <summary>
        /// Initializes a new instance of the TeleSignApiError class.
        /// </summary>
        public TeleSignApiError()
        {
            this.Code = TeleSignErrorCode.None;
            this.Description = string.Empty;
        }

        /// <summary>
        /// Gets or sets a numeric error code identifying the error.
        /// </summary>
        public TeleSignErrorCode Code { get; set; }

        /// <summary>
        /// Gets or sets a string description of the error.
        /// </summary>
        public string Description { get; set; }
    }
}
