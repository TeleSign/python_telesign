//-----------------------------------------------------------------------
// <copyright file="Attributes.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.TeleSignCmd
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Reflection;

    internal delegate void CommandDelegate(string[] args);

    internal static class AttributeHelper
    {
        private static Dictionary<string, CommandDelegate> commandLookup;

        static AttributeHelper()
        {
            commandLookup = new Dictionary<string, CommandDelegate>(StringComparer.InvariantCultureIgnoreCase);

            MethodInfo[] methods = typeof(Commands).GetMethods(BindingFlags.Static | BindingFlags.Public)
                                  .Where(m => m.GetCustomAttributes(typeof(CliCommandAttribute), false).Length > 0)
                                  .ToArray();

            foreach (MethodInfo method in methods)
            {
                commandLookup.Add(method.Name, (CommandDelegate)Delegate.CreateDelegate(typeof(CommandDelegate), null, method));
            }
        }

        internal static CommandDelegate LookupCommand(string commandName)
        {
            CommandDelegate d;

            if (commandLookup.TryGetValue(commandName, out d))
            {
                return d;
            }

            return null;
        }
    }

    [AttributeUsage(AttributeTargets.Method)]
    internal class CliCommandAttribute : Attribute
    {
        public string HelpString { get; set; }
    }
}
