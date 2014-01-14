//-----------------------------------------------------------------------
// <copyright file="JsonDotNetVerifyResponseParser.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.Verify
{
    using System;
    using Newtonsoft.Json;
    using Newtonsoft.Json.Linq;
    using TeleSign.Services;

    /// <summary>
    /// Parses the JSON responses for the TeleSign API's using JSon.Net library.
    /// </summary>
    public class JsonDotNetVerifyResponseParser : JsonDotNetResponseParser, IVerifyResponseParser
    {
        /// <summary>
        /// Parses a TeleSign Verify JSON response into a rich object.
        /// </summary>
        /// <param name="json">The json string containing the response.</param>
        /// <returns>A VerifyResponse object populated with the data from the response.</returns>
        public VerifyResponse ParseVerifyResponse(string json)
        {
            CheckArgument.NotNull(json, "json");

            JObject node = JObject.Parse(json);

            VerifyResponse response = new VerifyResponse(json)
            {
                VerifyInfo = this.ParseVerifyInfo((JObject)node["verify"]),
            };

            this.PopulateStatusResponseFields(response, node);

            return response;
        }

        /// <summary>
        /// Parses the Verify data package from a Verify response.
        /// </summary>
        /// <param name="node">The verify node.</param>
        /// <returns>A populate VerifyInfo object.</returns>
        private VerifyInfo ParseVerifyInfo(JObject node)
        {
            if (node == null)
            {
                return null;
            }

            return new VerifyInfo()
            {
                CodeState = this.ParseCodeState(EmptyStringIfNull(node["code_state"])),
                CodeEntered = EmptyStringIfNull(node["code_entered"]),
            };
        }

        /// <summary>
        /// Parses the code state string with the Verify data package to an
        /// enumeration. If the string doesn't convert to a known value
        /// it will return the value Other. This is to ensure that if
        /// the REST API changes and adds new values this will not fail.
        /// </summary>
        /// <param name="codeStateString">The code state as a string.</param>
        /// <returns>The CodeState enumeration.</returns>
        private CodeState ParseCodeState(string codeStateString)
        {
            CodeState codeState = CodeState.None;

            if (!Enum.TryParse<CodeState>(codeStateString, true, out codeState))
            {
                if (codeStateString == "VALID_YES")
                {
                    codeState = CodeState.Valid;
                }
                else
                {
                    codeState = CodeState.Other;
                }
            }

            return codeState;
        }
    }
}
