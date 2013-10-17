//-----------------------------------------------------------------------
// <copyright file="TeleSignServiceConfiguration.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Reflection;
    using System.Text;
    using System.Xml.Linq;

    /// <summary>
    /// The information required to connect to the TeleSign REST API. This
    /// includes a credential containing a customer id and secret key and
    /// the Uri to connect to the service. In general there is no
    /// need to supply or modify the URL as the default value will
    /// point to the TeleSign service.
    /// </summary>
    public class TeleSignServiceConfiguration
    {
        /// <summary>
        /// The address to connect to.
        /// </summary>
        public const string DefaultServiceAddress = "https://rest.telesign.com/";

        /// <summary>
        /// Initializes a new instance of the TeleSignServiceConfiguration class
        /// with a supplied credential and service address URI. Most of the time
        /// you should use the other constructor which doesn't take the URI
        /// parameter.
        /// </summary>
        /// <param name="credential">
        /// The TeleSign credentials supplied to you for authenticating to
        /// Telesign services.
        /// </param>
        /// <param name="serviceAddress">
        /// The base URI of the TeleSign service. Most of the time you should not
        /// need to provide this.
        /// </param>
        public TeleSignServiceConfiguration(
                    TeleSignCredential credential,
                    Uri serviceAddress)
        {
            this.Credential = credential;
            this.ServiceAddress = serviceAddress;
        }

        /// <summary>
        /// Initializes a new instance of the TeleSignServiceConfiguration class
        /// with a supplied credential. The default URI contained in the constant
        /// TeleSignServiceConfiguration.DefaultServiceAddress will be used.
        /// </summary>
        /// <param name="credential">
        /// The TeleSign credentials supplied to you for authenticating to
        /// Telesign services.
        /// </param>
        public TeleSignServiceConfiguration(TeleSignCredential credential)
            : this(
                    credential,
                    new Uri(TeleSignServiceConfiguration.DefaultServiceAddress))
        {
        }

        /// <summary>
        /// Gets or sets the TeleSign credentials used in this configuration.
        /// </summary>
        /// <value>The TeleSign credentials used in this configuration.</value>
        public TeleSignCredential Credential { get; set; }

        /// <summary>
        /// Gets or sets the base URI of the telesign REST services.
        /// </summary>
        /// <value>The base URI of the telesign REST services.</value>
        public Uri ServiceAddress { get; set; }

        /// <summary>
        /// This reads a configuration file called TeleSign.config.xml from
        /// the same directory as this dll.
        /// </summary>
        /// <returns>An instantiated TeleSignServiceConfiguration object containing configuration.</returns>
        public static TeleSignServiceConfiguration ReadConfigurationFile(string accountName = "default")
        {
            string configFilePath = TeleSignServiceConfiguration.GetDefaultConfigurationFilePath();

            return TeleSignServiceConfiguration.ReadConfigurationFile(configFilePath, accountName);
        }

        public static List<string> GetAccountNames()
        {
            string configFilePath = TeleSignServiceConfiguration.GetDefaultConfigurationFilePath();

            return TeleSignServiceConfiguration.GetAccountNames(configFilePath);
        }

        public static List<string> GetAccountNames(string configFilePath)
        {
            XDocument doc = XDocument.Load(configFilePath);

            XElement root = doc.Element("TeleSignConfig");
            string serviceUri = (string)root.Element("ServiceUri");

            List<string> names = new List<string>();

            foreach (XElement account in root.Element("Accounts").Elements("Account"))
            {
                names.Add((string)account.Attribute("name"));
            }

            return names;
        }

        /// <summary>
        /// This reads a configuration file from a specific file location.
        /// </summary>
        /// <param name="configFilePath">The path to the configuration file.</param>
        /// <returns>An instantiated TeleSignServiceConfiguration object containing configuration.</returns>
        public static TeleSignServiceConfiguration ReadConfigurationFile(string configFilePath, string accountName = "default")
        {
            XDocument doc = XDocument.Load(configFilePath);

            XElement root = doc.Element("TeleSignConfig");
            string serviceUri = (string)root.Element("ServiceUri");

            foreach (XElement account in root.Element("Accounts").Elements("Account"))
            {
                if (((string)account.Attribute("name")).ToLowerInvariant() == accountName.ToLowerInvariant())
                {
                    string overrideServiceUri = (string)account.Element("ServiceUri");

                    if (overrideServiceUri != null)
                    {
                        serviceUri = overrideServiceUri;
                    }

                    string customerId = (string)account.Element("CustomerId");
                    string secretKey = (string)account.Element("SecretKey");

                    return new TeleSignServiceConfiguration(
                                new TeleSignCredential(Guid.Parse(customerId), secretKey),
                                new Uri(serviceUri));
                }
            }

            string message = string.Format(
                        "There was no account '{0}' found in the configuration", 
                        accountName);

            throw new ArgumentException(message);
        }
       
        /// <summary>
        /// Helper method to determine the location of the executing assembly then
        /// construct the path of the config file in that directory.
        /// </summary>
        /// <returns>The path to the default configuration file.</returns>
        private static string GetDefaultConfigurationFilePath()
        {
            string assemblyFilePath = Assembly.GetExecutingAssembly().Location;
            string assemblyDirectory = Path.GetDirectoryName(assemblyFilePath);

            return Path.Combine(
                        assemblyDirectory, 
                        "TeleSign.config.xml");
        }
    }
}
