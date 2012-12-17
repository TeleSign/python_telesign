//-----------------------------------------------------------------------
// <copyright file="TransactionStatusCode.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    /// <summary>
    /// <para>
    /// The result code for transactions against the TeleSign REST API. Some of the status codes
    /// are common to all transaction types, and some are specific to each product.
    /// </para>
    /// <para>
    /// See TeleSign REST API documentation for further information.
    /// https://portal.telesign.com/docs/index.html
    /// </para>
    /// </summary>
    public enum TransactionStatusCode
    {
        /// <summary>
        /// The default value. This is not a valid code.
        /// </summary>
        None,

        /// <summary>
        /// The call was answered.
        /// </summary>
        CallAnswered = 100,

        /// <summary>
        /// The phone call was not answered.
        /// </summary>
        CallNotAnswered = 101,

        /// <summary>
        /// The telephone at the phone number called was taken off the hook, 
        /// but the call was disconnected (possibly hung-up) before the 
        /// verification message was completed.
        /// </summary>
        CallDisconnectedBeforeCompletion = 102,

        /// <summary>
        /// Call is currently in dialing stage or the message is 
        /// being listened to.
        /// </summary>
        CallInProgress = 103,

        /// <summary>
        /// The provided phone number is not a valid number.
        /// </summary>
        InvalidPhoneNumber = 104,

        /// <summary>
        /// The verification call has not yet been attempted.
        /// </summary>
        CallNotStarted = 105,

        /// <summary>
        /// An error occurred and no further attempt to call will be made.
        /// </summary>
        CallFailed = 106,

        /// <summary>
        /// The telephone number that was called returned a busy signal.
        /// </summary>
        LineBusy = 107,

        /// <summary>
        /// SMS has been delivered to the user’s phone.
        /// </summary>
        SmsDeliveredToHandset = 200,

        /// <summary>
        /// SMS has been delivered to the gateway. If the gateway responds 
        /// with further information (including successful delivery to 
        /// handset or delivery failure), the status is updated.
        /// </summary>
        SmsDeliveredToGateway = 203,

        /// <summary>
        /// Error delivering SMS to handset (reason unknown).
        /// SMS could not be delivered to the user’s handset for an unknown reason.
        /// </summary>
        SmsDeliveryError = 207,

        /// <summary>
        /// SMS could not be delivered to the handset due to a temporary 
        /// error with the phone. Examples: phone is turned off, 
        /// not enough memory to store the message.
        /// </summary>
        SmsTemporaryPhoneError = 210,

        /// <summary>
        /// SMS could not be delivered to the handset due to a permanent
        /// error with the phone. For example, phone is incompatible 
        /// with SMS, or phone is illegally registered on the network.
        /// </summary>
        SmsPermanentPhoneError = 211,

        /// <summary>
        /// Gateway/network cannot route message. Network cannot route 
        /// the message to the handset. This can happen when a phone 
        /// number is blacklisted on the network or is not a valid phone 
        /// number.
        /// </summary>
        SmsGatewayCannotRouteMessage = 220,

        /// <summary>
        /// The message was queued by the mobile provider and timed 
        /// out before it could be delivered to the handset.
        /// </summary>
        SmsTimeoutExpiredBeforeDelivery = 221,

        /// <summary>
        /// SMS is not supported by this phone, carrier, plan, or user.
        /// </summary>
        SmsNotSupported = 222,

        /// <summary>
        /// TeleSign blocked the SMS before it was sent. This can happen
        /// if the message contains spam or inappropriate material or if
        /// TeleSign believes the client is abusing the account in any way.
        /// </summary>
        SmsMessageBlocked = 230,

        /// <summary>
        /// The content of the message is not supported.
        /// </summary>
        SmsInvalidContent = 231,

        /// <summary>
        /// The final status of the message cannot be determined.
        /// </summary>
        SmsStatusUnknown = 250,

        /// <summary>
        /// The message is being sent to the SMS gateway.
        /// </summary>
        SmsMessageInProgress = 290,

        /// <summary>
        /// TeleSign is experiencing unusually high volume and has 
        /// queued the SMS message.
        /// </summary>
        SmsQueuedByTeleSign = 291,

        /// <summary>
        /// The SMS gateway has queued the message.
        /// </summary>
        SmsQueuedAtGateway = 292,

        /// <summary>
        /// The status of the SMS is temporarily unavailable.
        /// </summary>
        SmsStatusDelayed = 295,

        /// <summary>
        /// The Phone Id transaction completed successfully.
        /// </summary>
        Success = 300,

        /// <summary>
        /// The Phone Id transaction partially completed. Not all data fields may be
        /// present.
        /// </summary>
        PartiallyCompleted = 301,

        /// <summary>
        /// The transaction was not attempted. This is usually due to an
        /// error in the input parameters. Check the errors for more
        /// specific information.
        /// </summary>
        NotAttempted = 500,

        /// <summary>
        /// The transaction is not authorized. This could be invalid customer id,
        /// incorrect secret key or not subscribed to the requested product. Check
        /// the errors for more information.
        /// </summary>
        NotAuthorized = 501,

        /// <summary>
        /// The system was unable to provide status.
        /// </summary>
        StatusNotAvailable = 599,

        /// <summary>
        /// An unknown status code was returned. This could be a mismatch between
        /// the version of the SDK and the REST API. You can check the raw
        /// JSON output to see what the value is.
        /// </summary>
        Other = int.MaxValue,
    }
}
