//-----------------------------------------------------------------------
// <copyright file="TeleSignErrorCode.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    /// <summary>
    /// A collection of TeleSign error codes that map to error information returned for the web server, 
    /// and parsed using <see cref="M:TeleSign.Services.JsonDotNetResponseParser.ParseErrorCode(System.Int32)"/>.
    /// The <see cref="T:TeleSign.Services.TeleSignApiError"/> class contains a value of this type.
    /// </summary>
    public enum TeleSignErrorCode
    {
        /// <summary>
        /// Default value. Not a valid error code.
        /// </summary>
        None,

        /// <summary>
        /// Invalid parameter passed.
        /// </summary>
        InvalidParameter = -10001,

        /// <summary>
        /// Invalid source IP address.
        /// </summary>
        InvalidSourceIPAddress = -10009,

        /// <summary>
        /// Invalid request.
        /// </summary>
        InvalidRequest = -20001,

        /// <summary>
        /// This product is not enabled for this CustomerID.
        /// </summary>
        ProductNotEnabled = -20002,

        /// <summary>
        /// Invalid CustomerID.
        /// </summary>
        InvalidCustomerId = -30000,

        /// <summary>
        /// Account suspended.
        /// </summary>
        AccountSuspended = -30001,

        /// <summary>
        /// Account not activated.
        /// </summary>
        AccountNotActivated = -30002,

        /// <summary>
        /// Account limit reached.
        /// </summary>
        AccountLimitReached = -30003,

        /// <summary>
        /// Missing required Authorization header.
        /// </summary>
        MissingAuthorizationHeader = -30004,

        /// <summary>
        /// Required Authorization header is not in the correct format.
        /// </summary>
        InvalidAuthorizationHeaderFormat = -30005,

        /// <summary>
        /// Invalid signature.
        /// </summary>
        InvalidSignature = -30006,

        /// <summary>
        /// Missing required Date or X-TS-Date header.
        /// </summary>
        MissingDateHeader = -30007,

        /// <summary>
        /// Invalid X-TS-Auth-Method header.
        /// </summary>
        InvalidAuthMethodHeader = -30008,

        /// <summary>
        /// Date or X-TS-Date header is not RFC-822 compliant.
        /// </summary>
        InvalidDateFormat = -30009,

        /// <summary>
        /// Date or X-TS-Date header is out of range.
        /// </summary>
        InvalidDateRange = -30010,

        /// <summary>
        /// X-TS-Nonce header value is either too long or too short.
        /// </summary>
        InvalidNonce = -30011,

        /// <summary>
        /// X-TS-Nonce header value has been used recently.
        /// </summary>
        NonceReused = -30012,

        /// <summary>
        /// Status unavailable.
        /// </summary>
        StatusUnavailable = -40001,

        /// <summary>
        /// Not authorized.
        /// </summary>
        NotAuthorized = -40002,

        /// <summary>
        /// Resource not found.
        /// </summary>
        ResourceNotFound = -40004,

        /// <summary>
        /// Method not allowed.
        /// </summary>
        MethodNotFound = -40005,

        /// <summary>
        /// The maximum number of retries has been reached.
        /// </summary>
        MaxRetriesReached = -50001,

        /// <summary>
        /// Warning: PhoneID Contact/Live information not found, but PhoneID Standard
        /// information found and returned.
        /// </summary>
        ContactDataNotFound = -60001,

        /// <summary>
        /// System unavailable, please try again later.
        /// </summary>
        SystemUnavailable = -90001,

        /// <summary>
        /// Unknown or unparseable value.
        /// This is returned when the parser is unable to convert an error code in a web server response, 
        /// into one of these enumumeration values.
        /// This situation will occur only when the underlying TeleSign REST API is updated with new enumeration values,
        /// and you are not using the latest version of the <bold>TeleSign .NET SDK</bold>.
        /// </summary>
        Other = int.MinValue,
    }
}
