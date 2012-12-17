//-----------------------------------------------------------------------
// <copyright file="TestVerifyService.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.UnitTests
{
    using System;
    using NUnit.Framework;
    using TeleSign.Services.Verify;

    [TestFixture]
    public class TestVerifyService : BaseServiceTest
    {
        private VerifyService CreateService(
                    IWebRequester webRequester = null, 
                    IVerifyResponseParser responseParser = null)
        {
            if (webRequester == null)
            {
                webRequester = new FakeWebRequester();
            }

            if (responseParser == null)
            {
                responseParser = new FakeResponseParser();
            }

            return new VerifyService(
                        this.GetConfiguration(), 
                        webRequester, 
                        responseParser);
        }

        [Test]
        public void TestSmsRejectsNullNumber()
        {
            Assert.Throws<ArgumentNullException>(delegate
            {
                this.CreateService().SendSms(null);
            });
        }

        [Test]
        public void TestSmsRejectsEmptyNumber()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().SendSms(string.Empty);
            });
        }

        [Test]
        public void TestSmsRejectsNumberWithNoDigits()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                this.CreateService().SendSms("X+#$?");
            });
        }

        [Test]
        public void TestSmsDoesNotRejectCleanableNumbers()
        {
            this.CreateService().SendSms("+61 (08) 1111-1234");
        }
    }
}