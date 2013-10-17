//-----------------------------------------------------------------------
// <copyright file="JsonDotNetPhoneIdResponseParser.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.PhoneId
{
    using System;
    using System.Collections.Generic;
    using Newtonsoft.Json;
    using Newtonsoft.Json.Linq;

    /// <summary>
    /// Parses the JSON responses for the TeleSign API's using JSon.Net library.
    /// </summary>
    public class JsonDotNetPhoneIdResponseParser : JsonDotNetResponseParser, IPhoneIdResponseParser
    {
        /// <summary>
        /// Parses a TeleSign PhoneID Standard JSON response into a rich object.
        /// </summary>
        /// <param name="json">The json string containing the response.</param>
        /// <returns>A StandardPhoneIdResponse object populated with the data from the response.</returns>
        public PhoneIdStandardResponse ParsePhoneIdStandardResponse(string json)
        {
            CheckArgument.NotNull(json, "json");

            JObject node = JObject.Parse(json);

            PhoneIdStandardResponse response = new PhoneIdStandardResponse(json);
            this.PopulateCommonPhoneIdResponseFields(response, node);
            this.PopulateStatusResponseFields(response, node);
            this.PopulatePhoneIdStandardResponseFields(response, node);

            return response;
        }

        /// <summary>
        /// Parses a TeleSign PhoneID Contact JSON response into a rich object.
        /// </summary>
        /// <param name="json">The json string containing the response.</param>
        /// <returns>A ContactPhoneIdResponse object populated with the data from the response.</returns>
        public PhoneIdContactResponse ParsePhoneIdContactResponse(string json)
        {
            CheckArgument.NotNull(json, "json");

            JObject node = JObject.Parse(json);

            PhoneIdContactResponse response = new PhoneIdContactResponse(json);
            this.PopulateCommonPhoneIdResponseFields(response, node);
            this.PopulateStatusResponseFields(response, node);
            this.PopulatePhoneIdStandardResponseFields(response, node);

            response.Contact = this.ParseContactInfo(node["contact"]);

            return response;
        }

        /// <summary>
        /// Parses a TeleSign PhoneID Score JSON response into a rich object.
        /// </summary>
        /// <param name="json">The json string containing the response.</param>
        /// <returns>A ScorePhoneIdResponse object populated with the data from the response.</returns>
        public PhoneIdScoreResponse ParsePhoneIdScoreResponse(string json)
        {
            CheckArgument.NotNull(json, "json");

            JObject node = JObject.Parse(json);

            PhoneIdScoreResponse response = new PhoneIdScoreResponse(json);
            this.PopulateCommonPhoneIdResponseFields(response, node);
            this.PopulateStatusResponseFields(response, node);
            this.PopulatePhoneIdStandardResponseFields(response, node);

            response.Risk = this.ParseRisk(node["risk"]);

            return response;
        }

        /// <summary>
        /// Parses a TeleSign PhoneID Score JSON response into a rich object.
        /// </summary>
        /// <param name="json">The json string containing the response.</param>
        /// <returns>A PhoneIdLiveResponse object populated with the data from the response.</returns>
        public PhoneIdLiveResponse ParsePhoneIdLiveResponse(string json)
        {
            CheckArgument.NotNull(json, "json");

            JObject node = JObject.Parse(json);

            PhoneIdLiveResponse response = new PhoneIdLiveResponse(json);
            this.PopulateCommonPhoneIdResponseFields(response, node);
            this.PopulateStatusResponseFields(response, node);
            this.PopulatePhoneIdStandardResponseFields(response, node);

            response.Live = this.ParseLive(node["live"]);

            return response;
        }

        /// <summary>
        /// Parses the root node of a PhoneID JSON response and populates the
        /// data pacakges that are common to all PhoneID requests. The data
        /// common to all PhoneID responses is the numbering and cleansing
        /// information.
        /// </summary>
        /// <param name="response">The response object to populate.</param>
        /// <param name="node">The root node of the JSON response.</param>
        private void PopulateCommonPhoneIdResponseFields(
                    CommonPhoneIdResponse response,
                    JObject node)
        {
            JToken numberingNode = node["numbering"];
            if (numberingNode == null)
            {
                response.OriginalNumber = new NumberingInfo();
                response.CallCleansedNumber = new CleansingInfo();
                response.SmsCleansedNumber = new CleansingInfo();
            }
            else
            {
                response.OriginalNumber = this.ParseNumberingInfo((JObject)numberingNode["original"]);

                JObject cleansingNode = (JObject)numberingNode["cleansing"];
                response.CallCleansedNumber = this.ParseCleansingInfo((JObject)cleansingNode["call"]);
                response.SmsCleansedNumber = this.ParseCleansingInfo((JObject)cleansingNode["sms"]);
            }
        }

        /// <summary>
        /// Populates the additional data packages that are provided by PhoneID Standard.
        /// These are the location and phone type information.
        /// </summary>
        /// <param name="response">The response object to populate.</param>
        /// <param name="node">The root node of the JSON response.</param>
        private void PopulatePhoneIdStandardResponseFields(
                    PhoneIdStandardResponse response,
                    JObject node)
        {
            response.Location = this.ParseLocation((JObject)node["location"]);
            response.PhoneType = this.ParsePhoneTypeInfo((JObject)node["phone_type"]);
        }

        /// <summary>
        /// Parses the contact data package. This package includes information about
        /// the owner of the phone, such as name and address.
        /// </summary>
        /// <param name="node">The contact data package node.</param>
        /// <returns>A new populated Contact object.</returns>
        private ContactInfo ParseContactInfo(JToken node)
        {
            if (node.Type == JTokenType.Null)
            {
                return new ContactInfo();
            }

            ContactInfo contactInfo = new ContactInfo()
            {
                FirstName = EmptyStringIfNull(node["firstname"]),
                LastName = EmptyStringIfNull(node["lastname"]),
                City = EmptyStringIfNull(node["city"]),
                StateProvince = EmptyStringIfNull(node["state_province"]),
                Country = EmptyStringIfNull(node["country"]),
                ZipPostalCode = EmptyStringIfNull(node["zip_postal_code"]),
            };

            for (int i = 1; i <= 4; i++)
            {
                string keyName = string.Format("address{0}", i);
                string line = (string)node[keyName];

                if (!string.IsNullOrWhiteSpace(line))
                {
                    contactInfo.AddressLines.Add(line);
                }
            }

            return contactInfo;
        }

        /// <summary>
        /// Parses the Risk data package. This package includes a score
        /// representing a risk level and a recommendation.
        /// </summary>
        /// <param name="node">The risk data package node.</param>
        /// <returns>A new populated Risk object.</returns>
        private RiskInfo ParseRisk(JToken node)
        {
            if (node.Type == JTokenType.Null)
            {
                return new RiskInfo();
            }

            return new RiskInfo()
            {
                Level = this.ParseRiskLevel(EmptyStringIfNull(node["level"])),
                Recommendation = this.ParseTransactionRecommendation(EmptyStringIfNull(node["recommendation"])),
                Score = (int)node["score"],
            };
        }

        /// <summary>
        /// Parses the Live data package. This package includes roaming,
        /// subscriber and device status.
        /// </summary>
        /// <param name="node">The live data package node.</param>
        /// <returns>A new populated LiveInfo object.</returns>
        private LiveInfo ParseLive(JToken node)
        {
            if (node.Type == JTokenType.Null)
            {
                return new LiveInfo();
            }

            return new LiveInfo()
            {
                SubscriberStatus = EmptyStringIfNull(node["subscriber_status"]),
                DeviceStatus = EmptyStringIfNull(node["device_status"]),
                Roaming = EmptyStringIfNull(node["roaming"]),
                RoamingCountry = EmptyStringIfNull(node["roaming_country"]),
            };
        }

        /// <summary>
        /// Parses the location data package. The package includes information
        /// about the phones registration, such as coordinates, time zone and
        /// basic geographical location. This is information about the phone
        /// numbers registration not the owner of the phone.
        /// </summary>
        /// <param name="node">The location data package node.</param>
        /// <returns>A new populated Location object.</returns>
        private LocationInfo ParseLocation(JObject node)
        {
            return new LocationInfo()
            {
                City = EmptyStringIfNull(node["city"]),
                Zip = EmptyStringIfNull(node["zip"]),
                MetroCode = EmptyStringIfNull(node["metro_code"]),
                County = EmptyStringIfNull(node["county"]),
                State = EmptyStringIfNull(node["state"]),
                Country = this.ParseCountry((JObject)node["country"]),
                TimeZoneRange = this.ParseTimeZoneRange((JObject)node["time_zone"]),
                Coordinates = this.ParseCoordinates((JObject)node["coordinates"]),
            };
        }

        /// <summary>
        /// Parses the coordinate information.
        /// </summary>
        /// <param name="node">The coordinate node within the location data package.</param>
        /// <returns>A new populated Coordinates object.</returns>
        private Coordinates ParseCoordinates(JObject node)
        {
            return new Coordinates()
            {
                Latitude = ZeroDoubleIfNull(node["latitude"]),
                Longitude = ZeroDoubleIfNull(node["longitude"]),
            };
        }

        /// <summary>
        /// Parses the time zone range information.
        /// </summary>
        /// <param name="node">The time zone range node within the location data package.</param>
        /// <returns>A new populated TimeZoneRange object.</returns>
        private TimeZoneRange ParseTimeZoneRange(JObject node)
        {
            return new TimeZoneRange()
            {
                UtcOffsetMin = EmptyStringIfNull(node["utc_offset_min"]),
                UtcOffsetMax = EmptyStringIfNull(node["utc_offset_max"]),
                Name = EmptyStringIfNull(node["name"]),
            };
        }

        /// <summary>
        /// Parses the country information from the Country node.
        /// </summary>
        /// <param name="node">The country node.</param>
        /// <returns>A Country object.</returns>
        private Country ParseCountry(JObject node)
        {
            return new Country()
            {
                Name = EmptyStringIfNull(node["name"]),
                Iso2 = EmptyStringIfNull(node["iso2"]),
                Iso3 = EmptyStringIfNull(node["iso3"]),
            };
        }

        /// <summary>
        /// Parses the risk level string with the Risk data package to an
        /// enumeration. If the string doesn't convert to a known value
        /// it will return the value Other. This is to ensure that if
        /// the REST API changes and adds new values this will not fail.
        /// </summary>
        /// <param name="riskLevelString">The risk level as a string.</param>
        /// <returns>The RiskLevel enumeration.</returns>
        private RiskLevel ParseRiskLevel(string riskLevelString)
        {
            // This one gets parsed with a case statement because the
            // strings include characters that can't be .net variables.
            riskLevelString = riskLevelString.ToLowerInvariant().Trim();

            switch (riskLevelString)
            {
                case "low":
                    return RiskLevel.Low;
                case "medium":
                    return RiskLevel.Medium;
                case "high":
                    return RiskLevel.High;
                case "medium-low":
                    return RiskLevel.MediumLow;
                case "medium-high":
                    return RiskLevel.MediumHigh;
                case "neutral":
                    return RiskLevel.Neutral;
                default:
                    return RiskLevel.Other;
            }
        }

        /// <summary>
        /// Parses the transaction recommendation string with the Risk 
        /// data package to an enumeration. If the string doesn't 
        /// convert to a known value, it returns the value <strong>Other</strong>. 
        /// This ensures the API won't fail if new enumeration 
        /// values are added to the underlying <strong>TeleSign REST API</strong>.
        /// </summary>
        /// <param name="recommendationString">The recommendation as a string.</param>
        /// <returns>The RiskLevel enumeration.</returns>
        private TransactionRecommendation ParseTransactionRecommendation(string recommendationString)
        {
            // This one gets parsed with a case statement because the
            // strings include characters that can't be .net variables.
            recommendationString = recommendationString.ToLowerInvariant().Trim();

            switch (recommendationString)
            {
                case "allow":
                    return TransactionRecommendation.Allow;
                case "block":
                    return TransactionRecommendation.Block;
                case "flag":
                    return TransactionRecommendation.Flag;
                case "n/a":
                    return TransactionRecommendation.NotApplicable;
                default:
                    return TransactionRecommendation.Other;
            }
        }

        /// <summary>
        /// Parses the phone type code. If the string doesn't 
        /// convert to a known value it will return the value Other. 
        /// This is to ensure that if the REST API changes and adds 
        /// new values this will not fail.
        /// </summary>
        /// <param name="phoneTypeCode">The phone type code.</param>
        /// <returns>The PhoneType enumeration.</returns>
        private PhoneType ParsePhoneType(int phoneTypeCode)
        {
            PhoneType phoneType = PhoneType.None;

            if (!Enum.IsDefined(typeof(PhoneType), phoneTypeCode))
            {
                phoneType = PhoneType.Other;
            }
            else
            {
                try
                {
                    phoneType = (PhoneType)phoneTypeCode;
                }
                catch (Exception)
                {
                    phoneType = PhoneType.Other;
                }
            }

            return phoneType;
        }

        /// <summary>
        /// Parses the cleaning code. If the int doesn't 
        /// convert to a known value it will return the value Other. 
        /// This is to ensure that if the REST API changes and adds 
        /// new values this will not fail.
        /// </summary>
        /// <param name="cleanseCodeInt">The cleansing code.</param>
        /// <returns>The TeleSignErrorCode enumeration.</returns>
        private CleansingCode ParseCleanseCode(int cleanseCodeInt)
        {
            CleansingCode cleanseCode = CleansingCode.None;

            if (!Enum.IsDefined(typeof(CleansingCode), cleanseCodeInt))
            {
                cleanseCode = CleansingCode.Other;
            }
            else
            {
                try
                {
                    cleanseCode = (CleansingCode)cleanseCodeInt;
                }
                catch (Exception)
                {
                    cleanseCode = CleansingCode.Other;
                }
            }

            return cleanseCode;
        }

        /// <summary>
        /// Parses the phone type information.
        /// </summary>
        /// <param name="node">The phone type node.</param>
        /// <returns>
        /// Returns a PhoneType object which consists of
        /// a numberic code and a text description of the type of
        /// phone.
        /// </returns>
        private PhoneTypeInfo ParsePhoneTypeInfo(JObject node)
        {
            return new PhoneTypeInfo()
            {
                PhoneType = this.ParsePhoneType(ZeroIfNull(node["code"])),
                Description = EmptyStringIfNull(node["description"]),
            };
        }

        /// <summary>
        /// Parses cleansing information.
        /// </summary>
        /// <param name="node">The cleansing node.</param>
        /// <returns>A CleansingInfo object.</returns>
        private CleansingInfo ParseCleansingInfo(JObject node)
        {
            return new CleansingInfo()
            {
                CleanseCode = this.ParseCleanseCode((int)node["cleansed_code"]),
                CountryCode = EmptyStringIfNull(node["country_code"]),
                PhoneNumber = EmptyStringIfNull(node["phone_number"]),
                MinLength = ZeroIfNull(node["min_length"]),
                MaxLength = ZeroIfNull(node["max_length"]),
            };
        }

        /// <summary>
        /// Parses numbering information.
        /// </summary>
        /// <param name="node">The numbering info node.</param>
        /// <returns>A NumberingInfo node.</returns>
        private NumberingInfo ParseNumberingInfo(JObject node)
        {
            return new NumberingInfo()
            {
                PhoneNumber = EmptyStringIfNull(node["phone_number"]),
                CompletePhoneNumber = EmptyStringIfNull(node["complete_phone_number"]),
                CountryCode = EmptyStringIfNull(node["country_code"]),
            };
        }
    }
}