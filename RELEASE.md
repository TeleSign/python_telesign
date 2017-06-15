2.2.0
 - AutoVerify rebranded to AppVerify, please update your integration

2.1.1
 - Added completion endpoint to VerifyClient
 - Added console output and verify code input to verify_sms and verify_voice examples
 - Simplified RELEASE.md

2.1.0
 - updated and improved README
 - secret_key refactored to api_key to align with docs and portal
 - api_host is now known as rest_endpoint to align with docs and portal

2.0.0
 - Major refactor and simplification into generic REST client.
 - API parameters are now passed as parans to endpoint handlers.
 - Now using OkHttp as a web client internally which avoids a lot of redundant code.
 - UserAgent is now set to track client usage and help debug issues.
 - generateTelesignHeaders is a static and easily extracted from the SDK if custom behavior/implementation is required.
 - SDK is now targeting Java 8 as Java 7 has reached EoL

0.6.0
 - Added tts_message, sms_message, push_message to smartVerify Api. Also updated Test cases.
 - Added text to speech (TTS) feature of Voice Verify to the Java SDK.
 - Renaming resource variable(Code cleanup)
 - README.rst formatting, punctuation, and link fixes.
 - TMR-141/142 : Changes done for handling changes in AuthMethod enumeration value,  used when signing the Authentication header.
 - Throw IOException for better visibility of underlying subclasses in all APIs.
 
0.5.0
 - Configured Https protocol via constructor parameters
 - Removed string literals from method bodies
 - Capitalized constants
 - Renamed resource variables
 - Moved baseUrl and resource suffixes into static variables

0.4.0
 - Updated Verify Push, Verify Soft Token, Verify Registration, and Smart Verify
 - Set default TLS version to 1.2
 - Overloaded verify status method for backwards compatibility
 - Added debug info to the jar and now generate sources jar during build.
 - Preventing Gson instance from being serialized.
 - Adding verbose junit error output.

0.3.0
 - Adding carrier info to PhoneID Live and Contact responses.

0.2.0
 - Updated comments to PhoneId
 - Removed special characters as it was giving errors while running Junit test
 - Added pom.xml used while migrating to Maven central
 - Use Locale.US for date header
 - Added Originating_ip & Session_id to PhoneId & Verify calls

0.1.0
 - Added connect and read timeouts as configurable parameters
 - Removed redundant 'url.openConnection() & additional timeouts'
 - Added carrier information to PhoneId Standard response
 - Specify UTF-8 encoding in ant build.xml file