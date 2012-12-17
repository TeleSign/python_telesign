//-----------------------------------------------------------------------
// <copyright file="Program.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.TeleSignCmd
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Net;
    using System.Text;
    using TeleSign.Services;

    public class Program
    {
        public static int Main(string[] args)
        {
            ////AdHoc();
            if (args.Length == 0)
            {
                Usage();
                return -1;
            }

            string commandName = args[0];
            string[] commandArgs = new string[args.Length - 1];
            Array.Copy(args, 1, commandArgs, 0, args.Length - 1);

            CommandDelegate func = AttributeHelper.LookupCommand(commandName);
            func(commandArgs);
            return 0;
        }

        private static void AdHoc()
        {
        }

        private static void Usage()
        {
            Console.WriteLine("TODO: usage...");
        }
    }
}
