//-----------------------------------------------------------------------
// <copyright file="TestRawVerifyService.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.UnitTests
{
    using System;
    using System.Collections.Generic;
    using NUnit.Framework;
    using TeleSign.Services;
    using TeleSign.Services.Verify;

    [TestFixture] 
    public class TestRawVerifyService : BaseServiceTest
    {
        private RawVerifyService CreateService(IWebRequester webRequester = null)
        {
            if (webRequester == null)
            {
                webRequester = new FakeWebRequester();
            }

            return new RawVerifyService(this.GetConfiguration(), webRequester);
        }

        private string CreateDefaultQueryString()
        {
            return this.CreateQueryString(new Dictionary<string, string>()
            {
                { "ucid", "othr" }
            });
        }

        [Test]
        public void TestCallAcceptsCleanableNumber()
        {
            this.CreateService().CallRaw("+1 (555)444-4444");
        }

        [Test]
        public void TestStandardWebRequest()
        {
            ////SerializingWebRequester requester = new SerializingWebRequester();

            ////string expectedResponse = requester.ConstructSerializedString(
            ////            "GET",
            ////            "/v1/phoneid/standard/61811111234",
            ////            null,
            ////            this.CreateDefaultQueryString());

            ////string actualResponse = this.CreateService(requester).StandardLookupRaw("61811111234");

            ////Assert.AreEqual(expectedResponse, actualResponse);
        }
    }
}