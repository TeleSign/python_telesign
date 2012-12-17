//-----------------------------------------------------------------------
// <copyright file="CheckArgument.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services
{
    using System;
    using System.Globalization;

    /// <summary>
    /// Static helper class for parameter validation.
    /// </summary>
    public static class CheckArgument
    {
        /// <summary>
        /// Checks if the provided object is null. If it is an ArgumentNullException
        /// is throw otherwise it does nothing. This is just a way to simplify/shorten
        /// parameter checkin.
        /// </summary>
        /// <param name="value">The value to check for null.</param>
        /// <param name="parameterName">
        /// The name of the parameter. This is used to populate the exception.
        /// </param>
        public static void NotNull(
                    object value, 
                    string parameterName)
        {
            if (value == null)
            {
                throw new ArgumentNullException(parameterName);
            }
        }

        /// <summary>
        /// Checks if the provided object is null. If it is an ArgumentNullException
        /// is throw otherwise it does nothing. This is just a way to simplify/shorten
        /// parameter checkin.
        /// </summary>
        /// <param name="value">The value to check for null.</param>
        /// <param name="parameterName">
        /// The name of the parameter. This is used to populate the exception.
        /// </param>
        public static void NotNullOrEmpty(string value, string parameterName)
        {
            CheckArgument.NotNull(value, parameterName);
            CheckArgument.NotEmpty(value, parameterName);
        }

        /// <summary>
        /// Checks if the provided object is the empty string. If it is an ArgumentException
        /// is throw otherwise it does nothing. This is just a way to simplify/shorten
        /// parameter checkin. If the value is null it does nothing.
        /// </summary>
        /// <param name="value">The value to check for empty string.</param>
        /// <param name="parameterName">
        /// The name of the parameter. This is used to populate the exception.
        /// </param>
        public static void NotEmpty(string value, string parameterName)
        {
            if (value == null)
            {
                return;
            }

            if (value.Length == 0)
            {
                string message = string.Format(
                            "Argument '{0}' cannot be an empty string",
                            parameterName);

                throw new ArgumentException(message);
            }
        }

        /// <summary>
        /// Validates that the array is not null and of at least a certain length.
        /// If the array is null an ArgumentNullException is throw per the NotNull
        /// method - if the array is shorter than the required length an
        /// ArgumentException is thrown. Otherwise does nothing.
        /// </summary>
        /// <param name="value">The array to check.</param>
        /// <param name="minimumLength">The minimum length the array should be.</param>
        /// <param name="parameterName">The name of the parameter. Used to populate the exception.</param>
        public static void ArrayLengthAtLeast(
                    Array value, 
                    int minimumLength, 
                    string parameterName)
        {
            CheckArgument.NotNull(value, parameterName);

            if (value.Length < minimumLength)
            {
                string message = string.Format(
                            CultureInfo.InvariantCulture,
                            "Array '{0}' has length '{1}' but must be at least '{2}'",
                            parameterName,
                            value.Length,
                            minimumLength);

                throw new ArgumentException(
                            message,
                            FormatParameterName(parameterName));
            }
        }

        /// <summary>
        /// Validates that the array is not null and exactly a certain length.
        /// If the array is null an ArgumentNullException is throw per the NotNull
        /// method - if the array is not the required length an
        /// ArgumentException is thrown. Otherwise does nothing.
        /// </summary>
        /// <param name="value">The array to check.</param>
        /// <param name="expectedLength">The expected length the array should be.</param>
        /// <param name="parameterName">The name of the parameter. Used to populate the exception.</param>
        public static void ArrayLengthIs(
                    Array value,
                    int expectedLength,
                    string parameterName)
        {
            CheckArgument.NotNull(value, parameterName);

            if (value.Length != expectedLength)
            {
                string message = string.Format(
                            CultureInfo.InvariantCulture,
                            "Array '{0}' has length '{1}' but must be '{2}'",
                            parameterName,
                            value.Length,
                            expectedLength);

                throw new ArgumentException(
                            message,
                            FormatParameterName(parameterName));
            }
        }

        /// <summary>
        /// Helper method for when parameter names are not supplied to the verification
        /// functions. This just gives a default name for the parameter.
        /// </summary>
        /// <param name="parameterName">The name of the parameter.</param>
        /// <returns>The name of the parameter of a default value.</returns>
        private static string FormatParameterName(string parameterName)
        {
            if (string.IsNullOrEmpty(parameterName))
            {
                return "<unnamed>";
            }

            return parameterName;
        }
    }
}
