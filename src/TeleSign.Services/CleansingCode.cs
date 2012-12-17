//-----------------------------------------------------------------------
// <copyright file="CleansingCode.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    /// <summary>
    /// A code indicating how a phone number was cleansed/modified
    /// to make it a valid number.
    /// </summary>
    public enum CleansingCode
    {
        /// <summary>
        /// Default value. Not a valid cleansing code.
        /// </summary>
        None,

        /// <summary>
        /// No changes were made to the phone number. The phone 
        /// number was formatted properly, and no cleansing was required.
        /// </summary>
        NoChange = 100,

        /// <summary>
        /// The phone number was changed to ensure call completion. 
        /// For example, extraneous digits were removed, such as 011, 
        /// or additional digits were added to meet dialing rules.
        /// </summary>
        Changed = 101,

        /// <summary>
        /// The phone number entered is a restricted phone number. 
        /// Phone numbers that are restricted include premium rate numbers, 
        /// short codes (such as emergency services numbers), 
        /// and satellite phones.
        /// </summary>
        RestrictedNumber = 102,

        /// <summary>
        /// The phone number appears to be formatted correctly, 
        /// but cannot be matched to any specific area.
        /// </summary>
        NoMatch = 103,

        /// <summary>
        /// The phone number is not correctly formatted.
        /// </summary>
        Invalid = 104,

        /// <summary>
        /// The phone number length is either too long or too short.
        /// </summary>
        PartialMatch = 105,

        /// <summary>
        /// Unknown or unparseable value.
        /// This occurs when a REST API has changed, 
        /// yet the SDK has yet to be updated to accomodate the change.
        /// </summary>
        Other = int.MaxValue,
    }
}
