//-----------------------------------------------------------------------
// <copyright file="FakeResponseParser.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.UnitTests
{
    using System;
    using TeleSign.Services.PhoneId;
    using TeleSign.Services.Verify;

    public class FakeResponseParser : IPhoneIdResponseParser, IVerifyResponseParser
    {
        public FakeResponseParser()
        {
            this.ExpectedPhoneIdContactResponse = new PhoneIdContactResponse();
            this.ExpectedPhoneIdScoreResponse = new PhoneIdScoreResponse();
            this.ExpectedPhoneIdLiveResponse = new PhoneIdLiveResponse();
            this.ExpectedPhoneIdStandardResponse = new PhoneIdStandardResponse();
            this.ExpectedVerifyResponse = new VerifyResponse();
        }

        public PhoneIdStandardResponse ExpectedPhoneIdStandardResponse { get; set; }

        public PhoneIdScoreResponse ExpectedPhoneIdScoreResponse { get; set; }

        public PhoneIdLiveResponse ExpectedPhoneIdLiveResponse { get; set; }

        public PhoneIdContactResponse ExpectedPhoneIdContactResponse { get; set; }

        public VerifyResponse ExpectedVerifyResponse { get; set; }

        public Exception ExpectedException { get; set; }

        public PhoneIdStandardResponse ParsePhoneIdStandardResponse(string json)
        {
            this.ThrowIfNeeded(json);

            return this.ExpectedPhoneIdStandardResponse;
        }

        public PhoneIdScoreResponse ParsePhoneIdScoreResponse(string json)
        {
            this.ThrowIfNeeded(json);
            return this.ExpectedPhoneIdScoreResponse;
        }

        public PhoneIdLiveResponse ParsePhoneIdLiveResponse(string json)
        {
            this.ThrowIfNeeded(json);
            return this.ExpectedPhoneIdLiveResponse;
        }

        public PhoneIdContactResponse ParsePhoneIdContactResponse(string json)
        {
            this.ThrowIfNeeded(json);
            return this.ExpectedPhoneIdContactResponse;
        }

        public VerifyResponse ParseVerifyResponse(string json)
        {
            this.ThrowIfNeeded(json);
            return this.ExpectedVerifyResponse;
        }

        private void ThrowIfNeeded(string json)
        {
            CheckArgument.NotNull(json, "json");

            if (this.ExpectedException != null)
            {
                throw this.ExpectedException;
            }
        }
    }
}
