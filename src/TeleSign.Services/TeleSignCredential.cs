//-----------------------------------------------------------------------
// <copyright file="TeleSignCredential.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    using System;

    /// <summary>
    /// A credential to use the TeleSign service. It consists of a customer id
    /// guid (supplied to you by TeleSign) and a secret key.
    /// </summary>
    public class TeleSignCredential
    {
        /// <summary>
        /// Initializes a new instance of the TeleSignCredential class.
        /// </summary>
        /// <param name="customerId">The customer id.</param>
        /// <param name="secretKey">The customers secret key.</param>
        public TeleSignCredential(
                    Guid customerId,
                    string secretKey)
        {
            CheckArgument.NotNullOrEmpty(secretKey, "secretKey");

            this.CustomerId = customerId;
            this.SecretKey = secretKey;
        }

        /// <summary>
        /// Gets or sets the customer id.
        /// </summary>
        public Guid CustomerId { get; set; }

        /// <summary>
        /// Gets or sets the secret key.
        /// </summary>
        public string SecretKey { get; set; }
    }
}
