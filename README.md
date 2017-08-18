# simplisafe_alexa

Alexa skill to control SimpliSafe security system. 

Currently uses curl at the OS level as a BASH command to submit HTTP POST to Simplisafe mobile app. Requires a subscription to their mobile app to work.  

Planning to build this out to include a full library for the API and more functionality on the Alexa skill.


Currently does not have logic for loging in. Must have the cookie, uid and lid set up.

See this page of API documentation 
http://ben.hutchins.co/simplisafe/

See this page for a helpful tutorial on how to use the API including logging in
http://www.leftovercode.info/simplisafe.php