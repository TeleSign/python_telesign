//-----------------------------------------------------------------------
// <copyright file="PhoneIdContactResponse.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    /// <summary>
    /// <para>
    /// The response object from a TeleSign PhoneId Contact API call.
    /// </para>
    /// <para>
    /// This contains all the same information as a PhoneId standard
    /// response as well as Contact information about the owner of
    /// the phone.
    /// </para>
    /// </summary>
    public class PhoneIdContactResponse : PhoneIdStandardResponse
    {
        /// <summary>
        /// Initializes a new instance of the PhoneIdContactResponse class.
        /// </summary>
        public PhoneIdContactResponse()
            : this(null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the PhoneIdContactResponse class providing
        /// the raw JSON response string.
        /// </summary>
        /// <param name="rawResponse">The raw JSON response string returned from the REST service.</param>
        public PhoneIdContactResponse(string rawResponse)
            : base(rawResponse)
        {
            this.Contact = new ContactInfo();
        }

        /// <summary>
        /// Gets or sets the contact information about the owner
        /// of the phone.
        /// </summary>
        public ContactInfo Contact { get; set; }
    }
}
