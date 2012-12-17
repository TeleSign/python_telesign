//-----------------------------------------------------------------------
// <copyright file="PhoneTypeInfo.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    /// <summary>
    /// The type of phone - such as mobile, VOIP, landline, etc.
    /// </summary>
    public class PhoneTypeInfo
    {
        /// <summary>
        /// Initializes a new instance of the PhoneTypeInfo class.
        /// </summary>
        public PhoneTypeInfo()
        {
            this.PhoneType = PhoneType.None;
            this.Description = string.Empty;
        }

        /// <summary>
        /// Gets or sets the phone type.
        /// </summary>
        public PhoneType PhoneType { get; set; }

        /// <summary>
        /// Gets or sets the description of the phone type.
        /// </summary>
        public string Description { get; set; }
    }
}
