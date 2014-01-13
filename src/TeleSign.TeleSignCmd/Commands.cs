//-----------------------------------------------------------------------
// <copyright file="Commands.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.TeleSignCmd
{
    using System;
    using System.Collections.Generic;
    using System.Diagnostics;
    using System.IO;
    using System.Linq;
    using System.Text;
    using TeleSign.Services;
    using TeleSign.Services.PhoneId;
    using TeleSign.Services.Verify;

    public class Commands
    {
        public static TeleSignServiceConfiguration GetConfiguration()
        {
            // By passing null (or not passing the parameter at all) to
            // the services config will be pulled from TeleSign.config.xml.
            // 
            // If you comment out return null, and uncomment the block 
            // below, then fill in your customer id and secret key
            // you can construct the configuration object in code.
            return null;

            ////Guid customerId = Guid.Parse("*** Customer ID goes here ***");
            ////string secretKey = "*** Secret Key goes here ***";
            ////
            ////TeleSignCredential credential = new TeleSignCredential(
            ////            customerId,
            ////            secretKey);
            ////
            ////return new TeleSignServiceConfiguration(credential);
        }

        [CliCommand(HelpString = "Help me")]
        public static void RawPhoneIdStandard(string[] args)
        {
            CheckArgument.ArrayLengthIs(args, 1, "args");
            string phoneNumber = args[0];

            RawPhoneIdService service = new RawPhoneIdService(GetConfiguration());
            string jsonResponse = service.StandardLookupRaw(phoneNumber);

            Console.WriteLine(jsonResponse);
        }

        [CliCommand(HelpString = "Help me")]
        public static void RawPhoneIdContact(string[] args)
        {
            CheckArgument.ArrayLengthIs(args, 1, "args");
            string phoneNumber = args[0];

            RawPhoneIdService service = new RawPhoneIdService(GetConfiguration());
            string jsonResponse = service.ContactLookupRaw(phoneNumber);

            Console.WriteLine(jsonResponse);
        }

        [CliCommand(HelpString = "Help me")]
        public static void RawPhoneIdScore(string[] args)
        {
            CheckArgument.ArrayLengthIs(args, 1, "args");
            string phoneNumber = args[0];

            RawPhoneIdService service = new RawPhoneIdService(GetConfiguration());
            string jsonResponse = service.ScoreLookupRaw(phoneNumber);

            Console.WriteLine(jsonResponse);
        }

        [CliCommand(HelpString = "Help me")]
        public static void RawPhoneIdLive(string[] args)
        {
            CheckArgument.ArrayLengthIs(args, 1, "args");
            string phoneNumber = args[0];

            RawPhoneIdService service = new RawPhoneIdService(GetConfiguration());
            string jsonResponse = service.LiveLookupRaw(phoneNumber);

            Console.WriteLine(jsonResponse);
        }

        [CliCommand(HelpString = "Help me")]
        public static void PhoneIdStandard(string[] args)
        {
            CheckArgument.ArrayLengthIs(args, 1, "args");
            string phoneNumber = args[0];

            PhoneIdService service = new PhoneIdService(GetConfiguration());
            PhoneIdStandardResponse response = service.StandardLookup(phoneNumber);
        }
        
        [CliCommand(HelpString = "Help me")]
        public static void PhoneIdScore(string[] args)
        {
            CheckArgument.ArrayLengthIs(args, 1, "args");
            string phoneNumber = args[0];

            PhoneIdService service = new PhoneIdService(GetConfiguration());
            PhoneIdScoreResponse response = service.ScoreLookup(phoneNumber);

            Console.WriteLine("Phone Number: {0}", phoneNumber);
            Console.WriteLine("Risk        : {0} [{1}] - Recommend {2}", response.Risk.Level, response.Risk.Score, response.Risk.Recommendation);
        }

        [CliCommand(HelpString = "Help me")]
        public static void PhoneIdLive(string[] args)
        {
            CheckArgument.ArrayLengthIs(args, 1, "args");
            string phoneNumber = args[0];

            PhoneIdService service = new PhoneIdService(GetConfiguration());
            PhoneIdLiveResponse response = service.LiveLookup(phoneNumber);

            Console.WriteLine("Phone Number      : {0}", phoneNumber);
            Console.WriteLine("Subscriber Status : {0}", response.Live.SubscriberStatus);
            Console.WriteLine("Device            : {0}", response.Live.DeviceStatus);
            Console.Write("Roaming           : {0}", response.Live.Roaming);

            if (string.IsNullOrEmpty(response.Live.RoamingCountry))
            {
                Console.WriteLine();
            }
            else
            {
                Console.WriteLine(" in {0}", response.Live.RoamingCountry);
            }
        }

        [CliCommand(HelpString = "Help me")]
        public static void PhoneIdContact(string[] args)
        {
            CheckArgument.ArrayLengthIs(args, 1, "args");
            string phoneNumber = args[0];

            PhoneIdService service = new PhoneIdService(GetConfiguration());
            PhoneIdContactResponse response = service.ContactLookup(phoneNumber);

            Console.WriteLine("Phone Number: {0}", phoneNumber);
            Console.WriteLine("Name        : {0}", response.Contact.FullName);
            Console.WriteLine("Address     :\r\n{0}", response.Contact.GetFullAddress());
        }
        
        [CliCommand(HelpString = "Help me")]
        public static void MapRegistrationLocation(string[] args)
        {
            CheckArgument.ArrayLengthIs(args, 1, "args");
            string phoneNumber = args[0];

            PhoneIdService service = new PhoneIdService(GetConfiguration());
            PhoneIdStandardResponse response = service.StandardLookup(phoneNumber);

            string url = string.Format(
                        "http://maps.google.com/maps?q={0},{1}", 
                        response.Location.Coordinates.Latitude, 
                        response.Location.Coordinates.Longitude);

            Process.Start(url);
        }

        [CliCommand(HelpString = "Help me")]
        public static void MapContactLocation(string[] args)
        {
            CheckArgument.ArrayLengthIs(args, 1, "args");
            string phoneNumber = args[0];

            PhoneIdService service = new PhoneIdService(GetConfiguration());
            PhoneIdContactResponse response = service.ContactLookup(phoneNumber);

            string address = response.Contact.GetFullAddressOnSingleLine();
            Console.WriteLine("Google Mapping: {0}", address);

            string url = string.Format(
                        "http://maps.google.com/maps?q={0}",
                        address);

            Process.Start(url);
        }

        [CliCommand(HelpString = "Help me")]
        public static void VerifySms(string[] args)
        {
            PerformVerify(args, VerificationMethod.Sms);
        }

        [CliCommand(HelpString = "Help me")]
        public static void VerifyCall(string[] args)
        {
            PerformVerify(args, VerificationMethod.Call);
        }

        [CliCommand(HelpString = "Help me")]
        public static void VerifyPush(string[] args)
        {
            PerformVerify(args, VerificationMethod.Push);
        }

        [CliCommand(HelpString = "Help me")]
        public static void SendSms(string[] args)
        {
            CheckArgument.ArrayLengthAtLeast(args, 1, "args");

            string phoneNumber = args[0];

            string code = null;
            if (args.Length >= 2)
            {
                code = args[1];
            }

            string language = "en";
            if (args.Length >= 3)
            {
                language = args[2];
            }

            try
            {
                VerifyService verify = new VerifyService(GetConfiguration());
                VerifyResponse verifyResponse = null;
                verifyResponse = verify.SendSms(phoneNumber, code, string.Empty, language);
                Console.WriteLine("Sent sms");
            }
            catch (Exception x)
            {
                Console.WriteLine("Error: " + x.ToString());
            }
        }

        private static void PerformVerify(string[] args, VerificationMethod method)
        {
            CheckArgument.ArrayLengthAtLeast(args, 1, "args");

            string phoneNumber = args[0];

            string code = null;
            if (args.Length >= 2)
            {
                code = args[1];
            }

            string language = "en";
            if (args.Length >= 3)
            {
                language = args[2];
            }

            VerifyService verify = new VerifyService(GetConfiguration());
            VerifyResponse verifyResponse = null;

            if (method == VerificationMethod.Sms)
            {
                verifyResponse = verify.SendSms(phoneNumber, code, string.Empty, language);
            }
            else if (method == VerificationMethod.Call)
            {
                verifyResponse = verify.InitiateCall(phoneNumber, code, language);
            }
            else if (method == VerificationMethod.Push)
            {
                verifyResponse = verify.InitiatePush(phoneNumber, code);
            }
            else
            {
                throw new NotImplementedException("Invalid verification method");
            }

            foreach (TeleSignApiError e in verifyResponse.Errors)
            {
                Console.WriteLine(
                            "ERROR: [{0}] - {1}", 
                            e.Code, 
                            e.Description);
            }

            while (true)
            {
                Console.Write("Enter the code sent to phone [Just <enter> checks status. 'quit' to exit]: ");
                string enteredCode = Console.ReadLine();

                if (enteredCode.Equals("quit", StringComparison.InvariantCultureIgnoreCase))
                {
                    break;
                }

                Console.WriteLine(string.IsNullOrEmpty(enteredCode) ? "Checking status..." : "Validating code...");

                VerifyResponse statusResponse = verify.ValidateCode(
                            verifyResponse.ReferenceId,
                            enteredCode);

                Console.WriteLine(
                            "Transaction Status: {0} -- {1}\r\nCode State: {2}",
                            statusResponse.Status.Code,
                            statusResponse.Status.Description,
                            (statusResponse.VerifyInfo != null) 
                                        ? statusResponse.VerifyInfo.CodeState.ToString()
                                        : "Not Sent");

                if ((statusResponse.VerifyInfo != null) && (statusResponse.VerifyInfo.CodeState == CodeState.Valid))
                {
                    Console.WriteLine("Code was valid. Exiting.");
                    break;
                }
            }
        }
    }
}
