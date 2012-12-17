//-----------------------------------------------------------------------
// <copyright file="ContactInfo.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    using System.Collections.Generic;
    using System.Text;

    /// <summary>
    /// Contact information returned about the owner of a phone number.
    /// </summary>
    public class ContactInfo
    {
        /// <summary>
        /// Initializes a new instance of the ContactInfo class.
        /// </summary>
        public ContactInfo()
        {
            this.FirstName = string.Empty;
            this.LastName = string.Empty;
            this.City = string.Empty;
            this.StateProvince = string.Empty;
            this.ZipPostalCode = string.Empty;
            this.Country = string.Empty;
            this.AddressLines = new List<string>();
        }

        /// <summary>
        /// Gets or sets the first name associated with the owner of the
        /// phone number.
        /// </summary>
        public string FirstName { get; set; }

        /// <summary>
        /// Gets or sets the last name associated with the owner of the
        /// phone number.
        /// </summary>
        public string LastName { get; set; }

        /// <summary>
        /// Gets the concatenation [first name] [last name].
        /// </summary>
        public string FullName
        {
            get
            {
                string name = string.Format(
                            "{0} {1}", 
                            this.FirstName, 
                            this.LastName);

                return name.Trim();
            }
        }

        /// <summary>
        /// Gets the lines of address information. There may be 0-4 lines. 
        /// </summary>
        public List<string> AddressLines { get; private set; }

        /// <summary>
        /// Gets the address lines concatenated with crlf as a 
        /// single string.
        /// </summary>
        public string Address
        {
            get
            {
                return string.Join("\r\n", this.AddressLines).Trim();
            }
        }

        /// <summary>
        /// Gets or sets the city associated with the owner of the 
        /// phone number.
        /// </summary>
        /// <value>
        /// The city associated with the owner of the phone number.
        /// </value>
        public string City { get; set; }

        /// <summary>
        /// Gets or sets the state/province associated with the owner 
        /// of the phone number.
        /// </summary>
        public string StateProvince { get; set; }

        /// <summary>
        /// Gets or sets the country associated with the owner of the 
        /// phone number.
        /// </summary>
        /// <value></value>
        public string Country { get; set; }

        /// <summary>
        /// Gets or sets the zip/postal code associated with the owner of the 
        /// phone number.
        /// </summary>
        public string ZipPostalCode { get; set; }

        /// <summary>
        /// Returns the full address in a format as you would
        /// see on an envelope.
        /// </summary>
        /// <returns>The full address as a string.</returns>
        public string GetFullAddress()
        {
            string address = string.IsNullOrEmpty(this.Address)
                        ? "[no address]"
                        : this.Address;

            string city = string.IsNullOrEmpty(this.City)
                        ? "[no city]"
                        : this.City;

            string state = string.IsNullOrEmpty(this.StateProvince)
                        ? "[no state/province]"
                        : this.StateProvince;

            string zip = string.IsNullOrEmpty(this.ZipPostalCode)
                        ? "[no zip]"
                        : this.ZipPostalCode;

            string country = string.IsNullOrEmpty(this.Country)
                        ? "[no country]"
                        : this.Country;

            return string.Format(
                        "{0}\r\n{1}, {2}, {3}\r\n{4}",
                        address,
                        city,
                        state,
                        zip,
                        country);
        }

        /// <summary>
        /// Returns a single line form of address separated by comma's.
        /// </summary>
        /// <returns>A single line form of address separated by comma's.</returns>
        public string GetFullAddressOnSingleLine()
        {
            return string.Format(
                    "{0},{1},{2},{3},{4}",
                    this.Address,
                    this.City,
                    this.StateProvince,
                    this.ZipPostalCode,
                    this.Country);
        }
    }
}
