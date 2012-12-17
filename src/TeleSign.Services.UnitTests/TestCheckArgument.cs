//-----------------------------------------------------------------------
// <copyright file="TestCheckArgument.cs" company="TeleSign Corporation">
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
    public class TestCheckArgument : BaseServiceTest
    {   
        [Test]
        public void TestNotNullThrowsWhenPassedNull()
        {
            Assert.Throws<ArgumentNullException>(delegate
            {
                CheckArgument.NotNull(null, "value");
            });
        }

        [Test]
        public void TestNotNullDoesntThrowWhenPassedNonNull()
        {
            CheckArgument.NotNull(string.Empty, "value");
        }

        [Test]
        public void TestNotNullStillWorksWhenNameIsNull()
        {
            Assert.Throws<ArgumentNullException>(delegate
            {
                CheckArgument.NotNull(null, null);
            });
        }

        [Test]
        public void TestNotNullOrEmptyThrowsWhenPassedNull()
        {
            Assert.Throws<ArgumentNullException>(delegate
            {
                CheckArgument.NotNullOrEmpty(null, "value");
            });
        }

        [Test]
        public void TestNotNullOrEmptyThrowsWhenPassedEmptyString()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                CheckArgument.NotNullOrEmpty(string.Empty, "value");
            });
        }

        [Test]
        public void TestNotNullOrEmptyDoesntThrowWhenPassedNonNullNonEmptyString()
        {
            CheckArgument.NotNullOrEmpty("foo", "value");
        }

        [Test]
        public void TestNotNullOrEmptyStillWorksWhenNameIsNull()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                CheckArgument.NotNullOrEmpty(string.Empty, null);
            });
        }
    }
}