# ScriptsToHelpTheWorld | PetitionBot

Requirements:
  - Python 3
  - Geckodriver (Included within Zip)
  - Firefox

Instructions:
Run Petitionbot in the same directory as the Geckodriver. Currently no arguments are fed in, run the script as is. You will be prompted for your first name, last name, and email to enter into the change.org petitions. Keystrokes are intentionally slowed down to mimic human input. Waits will occur after signing petition to prevent captcha. Finally, after each petition a summary output will be given.

The Petition Bot is currently in v1. Captcha is an issue I am not sure how to bypass entirely at the moment. Most likely will need to focus on:
  - Greater degree of "Human" looking input (Have attempted, randomized time of individual key strokes, set waits, etc.)
  - Randomize user agents (Have not attempted)
  - Mess with the viewport? (Have tried different resolution sizes no luck)
  
 Specific issue: First 3 petitions are signed fine, but after the 3rd a captcha appears for most petitions :(
 
Things to do: 
  - Clean up code. I am aware it is sloppy.
  - Incorporate library of additional petitions
  - random fake information generator
  - threading and desired number of requests for a single petition. i.e run 1000 signs for a single petition (somehow avoid       detection by change.org and captch :/
