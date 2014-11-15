push-on-change
==============

This tiny script pushes a notification to your phone once a shell script outputs a new value.

## Setup
Create an account over at [Pushover](https://pushover.net/), and create an application.
Insert the API keys for both your user and application into tokens.py.example, and rename it to tokens.py.
After that you simply call the script, specifying what command to execute, how often to execute it (in seconds),
and what title should be displayed for the notification.

## Example

    $ ./push-on-change.py "ls -l" 10 LS
  
This will execute "ls -l" every 10 seconds, and once the output changes it will notify your device with the title "LS".
