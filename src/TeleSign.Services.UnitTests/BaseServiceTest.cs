//-----------------------------------------------------------------------
// <copyright file="BaseServiceTest.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.UnitTests
{
    using System;
    using System.Collections.Generic;

    public class BaseServiceTest
    {
        protected TeleSignServiceConfiguration GetConfiguration()
        {
            return null;

            ////Guid customerId = Guid.Parse("**** Put customer id here ********");
            ////string secretKey = "***** Put secret key here *****";

            ////TeleSignCredential credential = new TeleSignCredential(
            ////            customerId,
            ////            secretKey);

            ////Uri uri = new Uri("https://rest.telesign.com");

            ////return new TeleSignServiceConfiguration(
            ////            credential,
            ////            uri);
        }

        protected string CreateQueryString(Dictionary<string, string> fields)
        {
            return TeleSignService.ConstructQueryString(fields);
        }
    }
}
