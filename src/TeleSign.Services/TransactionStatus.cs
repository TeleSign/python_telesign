//-----------------------------------------------------------------------
// <copyright file="TransactionStatus.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    using System;

    /// <summary>
    /// The status of the API request. This is part of the response from all 
    /// TeleSign services.
    /// </summary>
    public class TransactionStatus
    {
        /// <summary>
        /// Initializes a new instance of the TransactionStatus class.
        /// </summary>
        public TransactionStatus()
        {
            this.UpdatedOn = DateTime.MinValue;
            this.Code = TransactionStatusCode.None;
            this.Description = string.Empty;
        }

        /// <summary>
        /// Gets or sets the time the response was updated.
        /// </summary>
        /// <value>The time the response was updated.</value>
        public DateTime UpdatedOn { get; set; }

        /// <summary>
        /// Gets or sets the API return code.
        /// </summary>
        /// <value>The API return code.</value>
        public TransactionStatusCode Code { get; set; }

        /// <summary>
        /// Gets or sets the description of the result.
        /// </summary>
        /// <value>The description of the result.</value>
        public string Description { get; set; }
    }
}
