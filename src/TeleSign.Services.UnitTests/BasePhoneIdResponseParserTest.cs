//-----------------------------------------------------------------------
// <copyright file="BasePhoneIdResponseParserTest.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.UnitTests
{
    using System;
    using System.IO;
    using NUnit.Framework;
    using TeleSign.Services.PhoneId;

    public abstract class BasePhoneIdResponseParserTest
    {
        [Test]
        public void TestValidPhoneIdScoreParsing()
        {
            string json = this.LoadJsonFromFile("PhoneIdScoreValidResponse_AsSent.txt");

            PhoneIdScoreResponse response = this.CreateParser().ParsePhoneIdScoreResponse(json);

            Assert.AreEqual(response.Errors.Count, 0);
            Assert.AreEqual(response.ReferenceId, "013890676FB7010BE1D4494A0000000E");
            Assert.AreEqual(response.ResourceUri, string.Empty);
            Assert.AreNotEqual(response.RawResponse, null);
            Assert.AreEqual(response.SubResource, "score");

            Assert.AreEqual(response.Status.UpdatedOn, DateTime.Parse("2012-07-16T15:28:14.349203Z").ToUniversalTime());
            Assert.AreEqual(response.Status.Code, TransactionStatusCode.Success);
            Assert.AreEqual(response.Status.Description, "Transaction successfully completed");

            Assert.AreEqual(response.OriginalNumber.CompletePhoneNumber, "13107409700");
            Assert.AreEqual(response.OriginalNumber.CountryCode, "1");
            Assert.AreEqual(response.OriginalNumber.PhoneNumber, "3107409700");

            Assert.AreEqual(response.CallCleansedNumber.CleanseCode, CleansingCode.NoChange);
            Assert.AreEqual(response.CallCleansedNumber.MaxLength, 10);
            Assert.AreEqual(response.CallCleansedNumber.MinLength, 10);
            Assert.AreEqual(response.CallCleansedNumber.CountryCode, "1");
            Assert.AreEqual(response.CallCleansedNumber.PhoneNumber, "3107409700");

            Assert.AreEqual(response.SmsCleansedNumber.CleanseCode, CleansingCode.NoChange);
            Assert.AreEqual(response.SmsCleansedNumber.MaxLength, 10);
            Assert.AreEqual(response.SmsCleansedNumber.MinLength, 10);
            Assert.AreEqual(response.SmsCleansedNumber.CountryCode, "1");
            Assert.AreEqual(response.SmsCleansedNumber.PhoneNumber, "3107409700");

            Assert.AreEqual(response.Risk.Level, RiskLevel.Low);
            Assert.AreEqual(response.Risk.Recommendation, TransactionRecommendation.Allow);
            Assert.AreEqual(response.Risk.Score, 0);
        }

        [Test]
        public void TestValidPhoneIdStandardParsing()
        {
            string json = this.LoadJsonFromFile("PhoneIdStandardValidResponse_AsSent.txt");

            PhoneIdStandardResponse response = this.CreateParser().ParsePhoneIdStandardResponse(json);

            Assert.AreEqual(response.Errors.Count, 0);
            Assert.AreEqual(response.ReferenceId, "01389064DBCE010BE1D449490000000E");
            Assert.AreEqual(response.ResourceUri, string.Empty);
            Assert.AreNotEqual(response.RawResponse, null);
            Assert.AreEqual(response.SubResource, "standard");

            Assert.AreEqual(response.Status.UpdatedOn, DateTime.Parse("2012-07-16T15:25:25.417924Z").ToUniversalTime());
            Assert.AreEqual(response.Status.Code, TransactionStatusCode.Success);
            Assert.AreEqual(response.Status.Description, "Transaction successfully completed");

            Assert.AreEqual(response.OriginalNumber.CompletePhoneNumber, "13107409700");
            Assert.AreEqual(response.OriginalNumber.CountryCode, "1");
            Assert.AreEqual(response.OriginalNumber.PhoneNumber, "3107409700");

            Assert.AreEqual(response.CallCleansedNumber.CleanseCode, CleansingCode.NoChange);
            Assert.AreEqual(response.CallCleansedNumber.MaxLength, 10);
            Assert.AreEqual(response.CallCleansedNumber.MinLength, 10);
            Assert.AreEqual(response.CallCleansedNumber.CountryCode, "1");
            Assert.AreEqual(response.CallCleansedNumber.PhoneNumber, "3107409700");

            Assert.AreEqual(response.SmsCleansedNumber.CleanseCode, CleansingCode.NoChange);
            Assert.AreEqual(response.SmsCleansedNumber.MaxLength, 10);
            Assert.AreEqual(response.SmsCleansedNumber.MinLength, 10);
            Assert.AreEqual(response.SmsCleansedNumber.CountryCode, "1");
            Assert.AreEqual(response.SmsCleansedNumber.PhoneNumber, "3107409700");

            Assert.AreEqual(response.PhoneType.PhoneType, PhoneType.FixedLine);
            Assert.AreEqual(response.PhoneType.Description, "FIXED_LINE");

            Assert.AreEqual(response.Location.City, "Los Angeles");
            Assert.AreEqual(response.Location.State, "CA");
            Assert.AreEqual(response.Location.Zip, "90066");
            Assert.AreEqual(response.Location.MetroCode, "4480");
            Assert.AreEqual(response.Location.County, "Los Angeles");

            Assert.AreEqual(response.Location.Country.Name, "United States");
            Assert.AreEqual(response.Location.Country.Iso2, "US");
            Assert.AreEqual(response.Location.Country.Iso3, "USA");

            Assert.AreEqual(response.Location.Coordinates.Longitude, -118.42302);
            Assert.AreEqual(response.Location.Coordinates.Latitude, 33.99791);

            Assert.AreEqual(response.Location.TimeZoneRange.Name, "America/Los_Angeles");
            Assert.AreEqual(response.Location.TimeZoneRange.UtcOffsetMin, "-8");
            Assert.AreEqual(response.Location.TimeZoneRange.UtcOffsetMax, "-8");
        }

        [Test]
        public void TestValidPhoneIdContactNoMatchParsing()
        {
            string json = this.LoadJsonFromFile("PhoneIdContactValidNoMatchResponse_AsSent.txt");

            PhoneIdContactResponse response = this.CreateParser().ParsePhoneIdContactResponse(json);

            Assert.AreEqual(response.ReferenceId, "013890689D26010BE1D4494700000010");
            Assert.AreEqual(response.ResourceUri, string.Empty);
            Assert.AreNotEqual(response.RawResponse, null);
            Assert.AreEqual(response.SubResource, "contact");

            Assert.AreEqual(response.Errors.Count, 1);
            Assert.AreEqual(response.Errors[0].Code, TeleSignErrorCode.ContactDataNotFound);
            Assert.AreEqual(response.Errors[0].Description, "PhoneID Contact Data Not Found");

            Assert.AreEqual(response.Status.UpdatedOn, DateTime.Parse("2012-07-16T15:29:34.508037Z").ToUniversalTime());
            Assert.AreEqual(response.Status.Code, TransactionStatusCode.Success);
            Assert.AreEqual(response.Status.Description, "Transaction successfully completed");

            Assert.AreEqual(response.OriginalNumber.CompletePhoneNumber, "13107409700");
            Assert.AreEqual(response.OriginalNumber.CountryCode, "1");
            Assert.AreEqual(response.OriginalNumber.PhoneNumber, "3107409700");

            Assert.AreEqual(response.CallCleansedNumber.CleanseCode, CleansingCode.NoChange);
            Assert.AreEqual(response.CallCleansedNumber.MaxLength, 10);
            Assert.AreEqual(response.CallCleansedNumber.MinLength, 10);
            Assert.AreEqual(response.CallCleansedNumber.CountryCode, "1");
            Assert.AreEqual(response.CallCleansedNumber.PhoneNumber, "3107409700");

            Assert.AreEqual(response.SmsCleansedNumber.CleanseCode, CleansingCode.NoChange);
            Assert.AreEqual(response.SmsCleansedNumber.MaxLength, 10);
            Assert.AreEqual(response.SmsCleansedNumber.MinLength, 10);
            Assert.AreEqual(response.SmsCleansedNumber.CountryCode, "1");
            Assert.AreEqual(response.SmsCleansedNumber.PhoneNumber, "3107409700");

            Assert.AreEqual(response.PhoneType.PhoneType, PhoneType.FixedLine);
            Assert.AreEqual(response.PhoneType.Description, "FIXED_LINE");

            Assert.AreEqual(response.Location.City, "Los Angeles");
            Assert.AreEqual(response.Location.State, "CA");
            Assert.AreEqual(response.Location.Zip, "90066");
            Assert.AreEqual(response.Location.MetroCode, "4480");
            Assert.AreEqual(response.Location.County, "Los Angeles");

            Assert.AreEqual(response.Location.Country.Name, "United States");
            Assert.AreEqual(response.Location.Country.Iso2, "US");
            Assert.AreEqual(response.Location.Country.Iso3, "USA");

            Assert.AreEqual(response.Location.Coordinates.Longitude, -118.42302);
            Assert.AreEqual(response.Location.Coordinates.Latitude, 33.99791);

            Assert.AreEqual(response.Location.TimeZoneRange.Name, "America/Los_Angeles");
            Assert.AreEqual(response.Location.TimeZoneRange.UtcOffsetMin, "-8");
            Assert.AreEqual(response.Location.TimeZoneRange.UtcOffsetMax, "-8");
        }

        [Test]
        public void TestValidPhoneIdContactMatchParsing()
        {
            string json = this.LoadJsonFromFile("PhoneIdContactValidMatchResponse_AsSent.txt");

            PhoneIdContactResponse response = this.CreateParser().ParsePhoneIdContactResponse(json);

            Assert.AreEqual(response.Errors.Count, 0);
            Assert.AreEqual(response.ReferenceId, "0138906A9011010BE1D4494B0000000E");
            Assert.AreEqual(response.ResourceUri, string.Empty);
            Assert.AreNotEqual(response.RawResponse, null);
            Assert.AreEqual(response.SubResource, "contact");

            Assert.AreEqual(response.Status.UpdatedOn, DateTime.Parse("2012-07-16T15:31:45.476050Z").ToUniversalTime());
            Assert.AreEqual(response.Status.Code, TransactionStatusCode.Success);
            Assert.AreEqual(response.Status.Description, "Transaction successfully completed");

            Assert.AreEqual(response.OriginalNumber.CompletePhoneNumber, "16502530000");
            Assert.AreEqual(response.OriginalNumber.CountryCode, "1");
            Assert.AreEqual(response.OriginalNumber.PhoneNumber, "6502530000");

            Assert.AreEqual(response.CallCleansedNumber.CleanseCode, CleansingCode.NoChange);
            Assert.AreEqual(response.CallCleansedNumber.MaxLength, 10);
            Assert.AreEqual(response.CallCleansedNumber.MinLength, 10);
            Assert.AreEqual(response.CallCleansedNumber.CountryCode, "1");
            Assert.AreEqual(response.CallCleansedNumber.PhoneNumber, "6502530000");

            Assert.AreEqual(response.SmsCleansedNumber.CleanseCode, CleansingCode.NoChange);
            Assert.AreEqual(response.SmsCleansedNumber.MaxLength, 10);
            Assert.AreEqual(response.SmsCleansedNumber.MinLength, 10);
            Assert.AreEqual(response.SmsCleansedNumber.CountryCode, "1");
            Assert.AreEqual(response.SmsCleansedNumber.PhoneNumber, "6502530000");

            Assert.AreEqual(response.PhoneType.PhoneType, PhoneType.FixedLine);
            Assert.AreEqual(response.PhoneType.Description, "FIXED_LINE");

            Assert.AreEqual(response.Location.City, "Mountain View");
            Assert.AreEqual(response.Location.State, "CA");
            Assert.AreEqual(response.Location.Zip, "94041");
            Assert.AreEqual(response.Location.MetroCode, "7400");
            Assert.AreEqual(response.Location.County, "Santa Clara");

            Assert.AreEqual(response.Location.Country.Name, "United States");
            Assert.AreEqual(response.Location.Country.Iso2, "US");
            Assert.AreEqual(response.Location.Country.Iso3, "USA");

            Assert.AreEqual(response.Location.Coordinates.Longitude, -122.079);
            Assert.AreEqual(response.Location.Coordinates.Latitude, 37.39199);

            Assert.AreEqual(response.Location.TimeZoneRange.Name, "America/Los_Angeles");
            Assert.AreEqual(response.Location.TimeZoneRange.UtcOffsetMin, "-8");
            Assert.AreEqual(response.Location.TimeZoneRange.UtcOffsetMax, "-8");

            Assert.AreEqual(response.Contact.FirstName, "GOOGLE INC");
            Assert.AreEqual(response.Contact.LastName, string.Empty);
            Assert.AreEqual(response.Contact.AddressLines.Count, 1);
            Assert.AreEqual(response.Contact.AddressLines[0], "1600 AMPHITHEATRE PKWY");
            Assert.AreEqual(response.Contact.Address, "1600 AMPHITHEATRE PKWY");
            Assert.AreEqual(response.Contact.City, "MOUNTAIN VIEW");
            Assert.AreEqual(response.Contact.StateProvince, "CA");
            Assert.AreEqual(response.Contact.Country, "US");
            Assert.AreEqual(response.Contact.ZipPostalCode, "940431351");
        }

        [Test]
        public void TestValidPhoneIdLiveNoMatchParsing()
        {
            string json = this.LoadJsonFromFile("PhoneIdLiveValidNoMatchResponse_AsSent.txt");

            PhoneIdLiveResponse response = this.CreateParser().ParsePhoneIdLiveResponse(json);

            Assert.AreEqual(response.ReferenceId, "013B23ED8EC2010BE4D40E410000006B");
            Assert.AreEqual(response.ResourceUri, string.Empty);
            Assert.AreNotEqual(response.RawResponse, null);
            Assert.AreEqual(response.SubResource, "live");

            Assert.AreEqual(response.Errors.Count, 1);
            Assert.AreEqual(response.Errors[0].Code, TeleSignErrorCode.ContactDataNotFound);
            Assert.AreEqual(response.Errors[0].Description, "PhoneID Live Data Not Found");

            Assert.AreEqual(response.Status.UpdatedOn, DateTime.Parse("2012-11-21T17:04:29.701218Z").ToUniversalTime());
            Assert.AreEqual(response.Status.Code, TransactionStatusCode.PartiallyCompleted);
            Assert.AreEqual(response.Status.Description, "Transaction partially completed");

            Assert.AreEqual(response.OriginalNumber.CompletePhoneNumber, "14256479999");
            Assert.AreEqual(response.OriginalNumber.CountryCode, "1");
            Assert.AreEqual(response.OriginalNumber.PhoneNumber, "4256479999");

            Assert.AreEqual(response.CallCleansedNumber.CleanseCode, CleansingCode.NoChange);
            Assert.AreEqual(response.CallCleansedNumber.MaxLength, 10);
            Assert.AreEqual(response.CallCleansedNumber.MinLength, 10);
            Assert.AreEqual(response.CallCleansedNumber.CountryCode, "1");
            Assert.AreEqual(response.CallCleansedNumber.PhoneNumber, "4256479999");

            Assert.AreEqual(response.SmsCleansedNumber.CleanseCode, CleansingCode.NoChange);
            Assert.AreEqual(response.SmsCleansedNumber.MaxLength, 10);
            Assert.AreEqual(response.SmsCleansedNumber.MinLength, 10);
            Assert.AreEqual(response.SmsCleansedNumber.CountryCode, "1");
            Assert.AreEqual(response.SmsCleansedNumber.PhoneNumber, "4256479999");

            Assert.AreEqual(response.PhoneType.PhoneType, PhoneType.Mobile);
            Assert.AreEqual(response.PhoneType.Description, "MOBILE");

            Assert.AreEqual(response.Location.City, "Bellevue");
            Assert.AreEqual(response.Location.State, "WA");
            Assert.AreEqual(response.Location.Zip, "98004");
            Assert.AreEqual(response.Location.MetroCode, "7600");
            Assert.AreEqual(response.Location.County, string.Empty);

            Assert.AreEqual(response.Location.Country.Name, "United States");
            Assert.AreEqual(response.Location.Country.Iso2, "US");
            Assert.AreEqual(response.Location.Country.Iso3, "USA");

            Assert.AreEqual(response.Location.Coordinates.Longitude, -122.20282);
            Assert.AreEqual(response.Location.Coordinates.Latitude, 47.61684);

            Assert.AreEqual(response.Location.TimeZoneRange.Name, "America/Los_Angeles");
            Assert.AreEqual(response.Location.TimeZoneRange.UtcOffsetMin, "-8");
            Assert.AreEqual(response.Location.TimeZoneRange.UtcOffsetMax, "-8");
        }

        [Test]
        public void TestValidPhoneIdLiveMatchParsing()
        {
            string json = this.LoadJsonFromFile("PhoneIdLiveValidMatchResponse_AsSent.txt");

            PhoneIdLiveResponse response = this.CreateParser().ParsePhoneIdLiveResponse(json);

            Assert.AreEqual(response.ReferenceId, "013B23B1FCCB010BE4D40D4D0000005F");
            Assert.AreEqual(response.ResourceUri, string.Empty);
            Assert.AreNotEqual(response.RawResponse, null);
            Assert.AreEqual(response.SubResource, "live");

            Assert.AreEqual(response.Status.UpdatedOn, DateTime.Parse("2012-11-21T15:59:26.802135Z").ToUniversalTime());
            Assert.AreEqual(response.Status.Code, TransactionStatusCode.Success);
            Assert.AreEqual(response.Status.Description, "Transaction successfully completed");

            Assert.AreEqual(response.OriginalNumber.CompletePhoneNumber, "17142829999");
            Assert.AreEqual(response.OriginalNumber.CountryCode, "1");
            Assert.AreEqual(response.OriginalNumber.PhoneNumber, "7142829999");

            Assert.AreEqual(response.CallCleansedNumber.CleanseCode, CleansingCode.NoChange);
            Assert.AreEqual(response.CallCleansedNumber.MaxLength, 10);
            Assert.AreEqual(response.CallCleansedNumber.MinLength, 10);
            Assert.AreEqual(response.CallCleansedNumber.CountryCode, "1");
            Assert.AreEqual(response.CallCleansedNumber.PhoneNumber, "7142829999");

            Assert.AreEqual(response.SmsCleansedNumber.CleanseCode, CleansingCode.NoChange);
            Assert.AreEqual(response.SmsCleansedNumber.MaxLength, 10);
            Assert.AreEqual(response.SmsCleansedNumber.MinLength, 10);
            Assert.AreEqual(response.SmsCleansedNumber.CountryCode, "1");
            Assert.AreEqual(response.SmsCleansedNumber.PhoneNumber, "7142829999");

            Assert.AreEqual(response.PhoneType.PhoneType, PhoneType.FixedLine);
            Assert.AreEqual(response.PhoneType.Description, "FIXED_LINE");

            Assert.AreEqual(response.Location.City, "ORANGE");
            Assert.AreEqual(response.Location.State, "CA");
            Assert.AreEqual(response.Location.Zip, "92665");
            Assert.AreEqual(response.Location.MetroCode, string.Empty);
            Assert.AreEqual(response.Location.County, string.Empty);

            Assert.AreEqual(response.Location.Country.Name, "United States");
            Assert.AreEqual(response.Location.Country.Iso2, "US");
            Assert.AreEqual(response.Location.Country.Iso3, "USA");

            Assert.AreEqual(response.Location.Coordinates.Longitude, -117.8495);
            Assert.AreEqual(response.Location.Coordinates.Latitude, 33.83141);

            Assert.AreEqual(response.Location.TimeZoneRange.Name, "America/Los_Angeles");
            Assert.AreEqual(response.Location.TimeZoneRange.UtcOffsetMin, "-8");
            Assert.AreEqual(response.Location.TimeZoneRange.UtcOffsetMax, "-8");
        }

        protected abstract IPhoneIdResponseParser CreateParser();

        protected virtual string LoadJsonFromFile(string filename)
        {
            string basePath = @"TestData\Json";
            string fullPath = Path.Combine(basePath, filename);

            return File.ReadAllText(fullPath);
        }
    }
}
