//-----------------------------------------------------------------------
// <copyright file="TestPhoneIdService.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.UnitTests
{
    using System;
    using NUnit.Framework;
    using TeleSign.Services.PhoneId;

    [TestFixture]
    public class TestPhoneIdService : BaseServiceTest
    {
        private PhoneIdService CreateService(
                    IWebRequester webRequester = null, 
                    IPhoneIdResponseParser responseParser = null)
        {
            if (webRequester == null)
            {
                webRequester = new FakeWebRequester();
            }

            if (responseParser == null)
            {
                responseParser = new FakeResponseParser();
            }

            return new PhoneIdService(
                        this.GetConfiguration(), 
                        webRequester, 
                        responseParser);
        }

        [Test]
        public void TestStandardRejectsNullNumber()
        {
            Assert.Throws<ArgumentNullException>(delegate
            {
                this.CreateService().StandardLookup(null);
            });
        }

        [Test]
        public void TestContactRejectsNullNumber()
        {
            Assert.Throws<ArgumentNullException>(delegate
            {
                this.CreateService().ContactLookup(null);
            });
        }

        [Test]
        public void TestScoreRejectsNullNumber()
        {
            Assert.Throws<ArgumentNullException>(delegate
            {
                this.CreateService().ScoreLookup(null);
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
                this.CreateService().ContactLookup(string.Empty);
            });
        }

        [Test]
        public void TestScoreRejectsEmptyNumber()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().ScoreLookup(string.Empty);
            });
        }

        [Test]
        public void TestStandardRejectsNumberWithNoDigits()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().StandardLookup("X+#$?");
            });
        }

        [Test]
        public void TestContactRejectsNumberWithNoDigits()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().ContactLookup("X+#$?");
            });
        }

        [Test]
        public void TestScoreRejectsNumberWithNoDigits()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().ScoreLookup("X+#$?");
            });
        }

        [Test]
        public void TestPhoneIdStandardWrapsParserErrors()
        {
            string message = "My exception message";
            IPhoneIdResponseParser parser = new FakeResponseParser()
            {
                ExpectedException = new Exception(message),
            };

            PhoneIdService service = this.CreateService(null, parser);

            Assert.Throws<ResponseParseException>(delegate
            {
                service.StandardLookup("15555555555");
            });
        }

        [Test]
        public void TestPhoneIdContactWrapsParserErrors()
        {
            string message = "My exception message";
            IPhoneIdResponseParser parser = new FakeResponseParser()
            {
                ExpectedException = new Exception(message),
            };

            PhoneIdService service = this.CreateService(null, parser);

            Assert.Throws<ResponseParseException>(delegate
            {
                service.ContactLookup("15555555555");
            });
        }

        [Test]
        public void TestPhoneIdScoreWrapsParserErrors()
        {
            string message = "My exception message";
            IPhoneIdResponseParser parser = new FakeResponseParser()
            {
                ExpectedException = new Exception(message),
            };

            PhoneIdService service = this.CreateService(null, parser);

            Assert.Throws<ResponseParseException>(delegate
            {
                service.ScoreLookup("15555555555");
            });
        }
    }
}