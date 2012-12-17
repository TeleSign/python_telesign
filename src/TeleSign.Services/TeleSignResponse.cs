//-----------------------------------------------------------------------
// <copyright file="TeleSignResponse.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    using System.Collections.Generic;

    /// <summary>
    /// The base class for all TeleSign API responses.
    /// </summary>
    public class TeleSignResponse
    {
        /// <summary>
        /// Initializes a new instance of the TeleSignResponse class.
        /// </summary>
        public TeleSignResponse()
            : this(null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the TeleSignResponse class providing
        /// the raw JSON response string.
        /// </summary>
        /// <param name="rawResponse">The raw JSON response string returned from the REST service.</param>
        public TeleSignResponse(string rawResponse)
        {
            this.RawResponse = rawResponse;
        }

        /// <summary>
        /// Gets or sets the raw JSON response from this transaction. You should generally
        /// not build logic around this field. It is provided primarily at this level
        /// of abstraction for debugging and logging of failures.
        /// </summary>
        public string RawResponse { get; protected set; }

        /// <summary>
        /// Gets or sets a reference id which uniquely identifies the transaction.
        /// </summary>
        /// <value>A reference id which uniquely identifies the transaction.</value>
        public string ReferenceId { get; set; }

        /// <summary>
        /// Gets or sets the resource URI that was accessed.
        /// </summary>
        /// <value>The resource URI that was accessed.</value>
        public string ResourceUri { get; set; }

        /// <summary>
        /// Gets or sets the sub resource that was accessed.
        /// </summary>
        /// <value>The sub resource that was accessed.</value>
        public string SubResource { get; set; }

        /// <summary>
        /// Gets or sets the list of errors returned from this API call.
        /// </summary>
        /// <value>The list of errors returned from this API call.</value>
        public List<TeleSignApiError> Errors { get; set; }

        /// <summary>
        /// Gets or sets the status of the transaction.
        /// </summary>
        /// <value>The status of the transaction.</value>
        public TransactionStatus Status { get; set; }
    }
}
