//-----------------------------------------------------------------------
// <copyright file="JsonDotNetResponseParser.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    using System;
    using System.Collections.Generic;
    using Newtonsoft.Json;
    using Newtonsoft.Json.Linq;

    /// <summary>
    /// Parses the JSON responses for the TeleSign API's using JSon.Net library.
    /// </summary>
    public class JsonDotNetResponseParser
    {
        /// <summary>
        /// Returns an empty string if the input is null. Otherwise
        /// casts the value to a string and returns that.
        /// </summary>
        /// <param name="value">The value to check.</param>
        /// <returns>An empty string or the value cast to a string.</returns>
        protected static string EmptyStringIfNull(JToken value)
        {
            if (value == null)
            {
                return string.Empty;
            }

            return (string)value;
        }

        /// <summary>
        /// Returns an empty string if the input is null. Otherwise
        /// casts the value to a string and returns that.
        /// </summary>
        /// <param name="value">The value to check.</param>
        /// <returns>An empty string or the value cast to a string.</returns>
        protected static int ZeroIfNull(JToken value)
        {
            if (value == null)
            {
                return 0;
            }

            return int.Parse((string)value);
        }

        /// <summary>
        /// Populates the base status and error information from a TeleSign REST
        /// API response.
        /// </summary>
        /// <param name="response">The response object to populate.</param>
        /// <param name="node">The root response node.</param>
        protected void PopulateStatusResponseFields(
                    TeleSignResponse response,
                    JObject node)
        {
            response.ReferenceId = EmptyStringIfNull(node["reference_id"]);
            response.ResourceUri = EmptyStringIfNull(node["resource_uri"]);
            response.SubResource = EmptyStringIfNull(node["sub_resource"]);
            response.Status = this.ParseStatus((JObject)node["status"]);
            response.Errors = this.ParseErrorList((JArray)node["errors"]);
        }

        /// <summary>
        /// Parses the transaction status code. If the string doesn't 
        /// convert to a known value it will return the value Other. 
        /// This is to ensure that if the REST API changes and adds 
        /// new values this will not fail.
        /// </summary>
        /// <param name="transactionStatusInt">The transaction status code.</param>
        /// <returns>The TransactionStatusCode enumeration.</returns>
        private TransactionStatusCode ParseTransactionStatus(int transactionStatusInt)
        {
            TransactionStatusCode transactionStatus = TransactionStatusCode.None;

            if (!Enum.IsDefined(typeof(TransactionStatusCode), transactionStatusInt))
            {
                transactionStatus = TransactionStatusCode.Other;
            }
            else
            {
                try
                {
                    transactionStatus = (TransactionStatusCode)transactionStatusInt;
                }
                catch (Exception)
                {
                    transactionStatus = TransactionStatusCode.Other;
                }
            }

            return transactionStatus;
        }

        /// <summary>
        /// Parses the error code. If the int doesn't 
        /// convert to a known value it will return the value Other. 
        /// This is to ensure that if the REST API changes and adds 
        /// new values this will not fail.
        /// </summary>
        /// <param name="errorCodeInt">The error code.</param>
        /// <returns>The TeleSignErrorCode enumeration.</returns>
        private TeleSignErrorCode ParseErrorCode(int errorCodeInt)
        {
            TeleSignErrorCode errorCode = TeleSignErrorCode.None;

            if (!Enum.IsDefined(typeof(TeleSignErrorCode), errorCodeInt))
            {
                errorCode = TeleSignErrorCode.Other;
            }
            else
            {
                try
                {
                    errorCode = (TeleSignErrorCode)errorCodeInt;
                }
                catch (Exception)
                {
                    errorCode = TeleSignErrorCode.Other;
                }
            }

            return errorCode;
        }

        /// <summary>
        /// Parses the API response status. This is common on all TeleSign responses.
        /// </summary>
        /// <param name="node">The status node.</param>
        /// <returns>A Status object.</returns>
        private TransactionStatus ParseStatus(JObject node)
        {
            return new TransactionStatus()
            {
                UpdatedOn = (DateTime)node["updated_on"],
                Code = this.ParseTransactionStatus((int)node["code"]),
                Description = EmptyStringIfNull(node["description"]),
            };
        }

        /// <summary>
        /// Parses a single error from within the error list.
        /// </summary>
        /// <param name="node">An error node.</param>
        /// <returns>An error object.</returns>
        private TeleSignApiError ParseError(JObject node)
        {
            return new TeleSignApiError()
            {
                Code = this.ParseErrorCode((int)node["code"]),
                Description = EmptyStringIfNull(node["description"]),
            };
        }

        /// <summary>
        /// Parses a list of errors from an API response. When there are no
        /// errors an empty list is returned.
        /// </summary>
        /// <param name="node">The error list node.</param>
        /// <returns>A list of errors.</returns>
        private List<TeleSignApiError> ParseErrorList(JArray node)
        {
            List<TeleSignApiError> errors = new List<TeleSignApiError>();

            foreach (JObject o in node)
            {
                errors.Add(this.ParseError(o));
            }

            return errors;
        }
    }
}
