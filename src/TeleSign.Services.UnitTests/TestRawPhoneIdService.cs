//-----------------------------------------------------------------------
// <copyright file="TestPhoneIdRawService.cs" company="TeleSign Corporation">
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
    using TeleSign.Services.PhoneId;

    [TestFixture] 
    public class TestRawPhoneIdService : BaseServiceTest
    {
        private RawPhoneIdService CreateService(IWebRequester webRequester = null)
        {
            if (webRequester == null)
            {
                webRequester = new FakeWebRequester();
            }

            return new RawPhoneIdService(this.GetConfiguration(), webRequester);
        }

        private string CreateDefaultQueryString()
        {
            return this.CreateQueryString(new Dictionary<string, string>()
            {
                { "ucid", "othr" }
            });
        }

        [Test]
        public void TestStandardRejectsNullNumber()
        {
            Assert.Throws<ArgumentNullException>(delegate
            {
                this.CreateService().StandardLookupRaw(null);
            });
        }

        [Test]
        public void TestContactRejectsNullNumber()
        {
            Assert.Throws<ArgumentNullException>(delegate
            {
                this.CreateService().ContactLookupRaw(null);
            });
        }

        [Test]
        public void TestScoreRejectsNullNumber()
        {
            Assert.Throws<ArgumentNullException>(delegate
            {
                this.CreateService().ScoreLookupRaw(null);
            });
        }

        [Test]
        public void TestLiveRejectsNullNumber()
        {
            Assert.Throws<ArgumentNullException>(delegate
            {
                this.CreateService().LiveLookupRaw(null);
            });
        }

        [Test]
        public void TestStandardRejectsEmptyNumber()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().StandardLookupRaw(string.Empty);
            });
        }

        [Test]
        public void TestContactRejectsEmptyNumber()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().ContactLookupRaw(string.Empty);
            });
        }

        [Test]
        public void TestScoreRejectsEmptyNumber()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().ScoreLookupRaw(string.Empty);
            });
        }

        [Test]
        public void TestLiveRejectsEmptyNumber()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().LiveLookupRaw(string.Empty);
            });
        }

        [Test]
        public void TestStandardRejectsNumberWithNoDigits()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().StandardLookupRaw("X+#$?");
            });
        }

        [Test]
        public void TestContactRejectsNumberWithNoDigits()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().ContactLookupRaw("X+#$?");
            });
        }

        [Test]
        public void TestScoreRejectsNumberWithNoDigits()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().ScoreLookupRaw("X+#$?");
            });
        }

        [Test]
        public void TestLiveRejectsNumberWithNoDigits()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().LiveLookupRaw("X+#$?");
            });
        }

        [Test]
        public void TestStandardDoesNotRejectCleanableNumbers()
        {
            this.CreateService().StandardLookupRaw("+61 (08) 9791-1234");
        }

        [Test]
        public void TestContactDoesNotRejectCleanableNumbers()
        {
            this.CreateService().ContactLookupRaw("+61 (08) 1111-1234");
        }

        [Test]
        public void TestScoreDoesNotRejectCleanableNumbers()
        {
            this.CreateService().ScoreLookupRaw("+61 (08) 1111-1234");
        }

        [Test]
        public void TestLiveDoesNotRejectCleanableNumbers()
        {
            this.CreateService().LiveLookupRaw("+61 (08) 1111-1234");
        }

        [Test]
        public void TestStandardWebRequest()
        {
            SerializingWebRequester requester = new SerializingWebRequester();

            string expectedResponse = requester.ConstructSerializedString(
                        "GET",
                        "/v1/phoneid/standard/61811111234",
                        null,
                        this.CreateDefaultQueryString());

            string actualResponse = this.CreateService(requester).StandardLookupRaw("61811111234");

            Assert.AreEqual(expectedResponse, actualResponse);
        }

        [Test]
        public void TestContactWebRequest()
        {
            SerializingWebRequester requester = new SerializingWebRequester();
            string expectedResponse = requester.ConstructSerializedString(
                        "GET",
                        "/v1/phoneid/contact/61811111234",
                        null,
                        this.CreateDefaultQueryString());

            string actualResponse = this.CreateService(requester).ContactLookupRaw("61811111234");

            Assert.AreEqual(expectedResponse, actualResponse);
        }

        [Test]
        public void TestScoreWebRequest()
        {
            SerializingWebRequester requester = new SerializingWebRequester();

            string expectedResponse = requester.ConstructSerializedString(
                        "GET",
                        "/v1/phoneid/score/61811111234",
                        null,
                        this.CreateDefaultQueryString());

            string actualResponse = this.CreateService(requester).ScoreLookupRaw("61811111234");

            Assert.AreEqual(expectedResponse, actualResponse);
        }

        [Test]
        public void TestLiveWebRequest()
        {
            SerializingWebRequester requester = new SerializingWebRequester();

            string expectedResponse = requester.ConstructSerializedString(
                        "GET",
                        "/v1/phoneid/live/61811111234",
                        null,
                        this.CreateDefaultQueryString());

            string actualResponse = this.CreateService(requester).LiveLookupRaw("61811111234");

            Assert.AreEqual(expectedResponse, actualResponse);
        }
    }
}
