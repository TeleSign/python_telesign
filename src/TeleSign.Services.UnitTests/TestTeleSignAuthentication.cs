//-----------------------------------------------------------------------
// <copyright file="TestTeleSignAuthentication.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.UnitTests
{
    using System;
    using NUnit.Framework;

    [TestFixture] 
    public class TestTeleSignAuthentication
    {
        [Test]
        public void TestConstructorThrowsOnNullInput()
        {
            Assert.Throws<ArgumentNullException>(delegate
            {
                TeleSignAuthentication auth = new TeleSignAuthentication(null);
            });
        }

        [Test]
        public void TestInvalidAuthMethodThrows()
        {
            TeleSignAuthentication auth = new TeleSignAuthentication(this.GetCredential());

            Assert.Throws<NotSupportedException>(delegate
            {
                auth.MapAuthenticationMethodToHeaderString(AuthenticationMethod.None);
            });
        }

        [Test]
        public void TestSha1Hash()
        {
            TeleSignAuthentication auth = new TeleSignAuthentication(this.GetCredential());
            string hash = auth.ComputeHash("HASH ME", AuthenticationMethod.HmacSha1);
            Assert.Greater(hash.Length, 0);
        }

        [Test]
        public void TestSha256Hash()
        {
            TeleSignAuthentication auth = new TeleSignAuthentication(this.GetCredential());
            string hash = auth.ComputeHash("HASH ME", AuthenticationMethod.HmacSha256);
            Assert.Greater(hash.Length, 0);
        }

        [Test]
        public void TestAuthStringConstructionThrowsOnNullStringToSign()
        {
            TeleSignAuthentication auth = new TeleSignAuthentication(this.GetCredential());

            Assert.Throws<ArgumentNullException>(delegate
            {
                auth.ConstructAuthorizationString(null, AuthenticationMethod.HmacSha1);
            });
        }

        [Test]
        public void TestAuthStringConstructionThrowsOnEmptyStringToSign()
        {
            TeleSignAuthentication auth = new TeleSignAuthentication(this.GetCredential());

            Assert.Throws<ArgumentException>(delegate
            {
                auth.ConstructAuthorizationString(string.Empty, AuthenticationMethod.HmacSha1);
            });
        }

        [Test]
        public void TestBasicFormatOfAuthorizationString()
        {
            TeleSignCredential credential = this.GetCredential();
            TeleSignAuthentication auth = new TeleSignAuthentication(credential);
            string authString = auth.ConstructAuthorizationString("FakeStringToSign", AuthenticationMethod.HmacSha1);

            string expectedStart = string.Format("TSA {0}:", credential.CustomerId);
            Assert.True(authString.StartsWith(expectedStart));
        }

        private TeleSignCredential GetCredential()
        {
            return new TeleSignCredential(
                        Guid.NewGuid(),
                        "abababababababababababababababababa+Jkababababababababababababab+3ababababababababaP1w==");
        }
    }
}
