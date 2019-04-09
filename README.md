# World Quest Scanner
Scans Wowhead's active world quest website for keywords.

## Usage
This script is meant to send email notifications when a particular World of Warcraft world quest is active. Been looking for Whiplash for two months now to finish the achievement Adventurer of Stormsong Valley? Supply 'Whiplash' as a key word and put in your own gmail email address for both sender_email and receiver_email and you'll get an email from yourself letting you know that the quest is active!

## Requirements
- Python2 (not Python3 - several dependencies and methods are incompatible with Python3)
- A Gmail account

## Directions
- Install Python2 if not already installed
- Download the file `world_quest_scanner.py`
- Open the file and customize variables to your liking
  - `sender_email`: Needs to be your gmail account, or a gmail account you have access to
  - `receiver_email`: The email account you want to receive the notifications (can be the same as the sender_email, which is in fact what I recommend)
  - `password`: Your gmail password. Case sensative.
  - `strings`: Put the keywords to want to scan for in this array. You can put in as many as you want. Ex: `['Whiplash', 'Sabertron']` or `['Moxo the Beheader']` or `['Shell Game', 'Beachhead', 'Azerite Mining']`. Case does not matter.
  - `website`: Whatver URL you want to scan. Current value is Wowhead's site for Battle for Azeroth active world quests in North America.
  - `interval`: How often do you want to scan the website? Current value is 21600 seconds (which is 6 hours). Put in any amount of time you like (in seconds).
- Open a console and navigate to the where you have the file saved
- Start the script by running `python world_quest_scanner.py`. You must keep this console tab open indefinitely, if you close the console, the script will stop running in the background.
- Stop the script by pressing `ctrl+c` (`cmd+c` on mac) or by closing the console.

## Notes
- Feel free to email me with questions and I may have a quick answer, but I'm not really keen on providing intense IT support. I reserve the right to ignore you.
- Yes I know it's not the most eloquent and efficient thing ever, I'm fine with that.
- Feel free to share, distribute, edit, improve, etc.
- Does all of this sound too daunting? Get a really nice friend who knows their way around Python to run it for you! They can put your email address in the `receiver_email` field.
