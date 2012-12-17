//-----------------------------------------------------------------------
// <copyright file="TestJsonDotNetPhoneIdResponseParser.cs" company="TeleSign Corporation">
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

    /// <summary>
    /// Note that the tests are in the base class. This is so that if you
    /// happened to implement your own response parser you just need to
    /// create an override class such as this to run all the same test cases
    /// against it.
    /// </summary>
    [TestFixture]
    public class TestJsonDotNetPhoneIdResponseParser : BasePhoneIdResponseParserTest
    {
        protected override IPhoneIdResponseParser CreateParser()
        {
            return new JsonDotNetPhoneIdResponseParser();
        }
    }
}