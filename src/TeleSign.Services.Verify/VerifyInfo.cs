//-----------------------------------------------------------------------
// <copyright file="VerifyInfo.cs" company="TeleSign Corporation">
//     Copyright (c) TeleSign Corporation 2012.
// </copyright>
// <license>MIT</license>
// <author>Zentaro Kavanagh</author>
//-----------------------------------------------------------------------

namespace TeleSign.Services.Verify
{
    /// <summary>
    /// The state of a verification transaction. Whether a code has been entered
    /// and if so what code was entered.
    /// </summary>
    public class VerifyInfo
    {
        /// <summary>
        /// Initializes a new instance of the VerifyInfo class.
        /// </summary>
        public VerifyInfo()
        {
            this.CodeState = CodeState.None;
            this.CodeEntered = string.Empty;
        }

        /// <summary>
        /// Gets or sets the state of the verification code.
        /// </summary>
        /// <value>The state of the verification code.</value>
        public CodeState CodeState { get; set; }

        /// <summary>
        /// Gets or sets the code that was entered by the user.
        /// </summary>
        /// <value>The code that was entered by the user.</value>
        public string CodeEntered { get; set; }
    }
}
