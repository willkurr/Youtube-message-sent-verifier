# Youtube-message-sent-verifier
Program for verifying that your messages are being sent in a Youtube Live chat.

## Purpose
When it comes to Youtube's message handling in live broadcasts, it's less than stellar. Occasionally you will try to send a message, and it will appear to have sent from your end, but noone else will have received it. Youtube seems to have some sort of fuzzy logic taking care of messages, causing them to not be sent, without even telling the user. And it sucks and accomplishes nothing.

This program aims to at the very least allow you to be aware of this issue. Given a youtube link ID and a username, this program will listen for messages in realtime and notify you when a message appears that matches the provided username. This also works for superchats!

By making use of the pytchat library, the program watches the chat of a given youtube live as if it were someone on the other end, and lets you know if your messages have actually been sent out, or if youtube is ghosting you.

## How to use
It is quite simple to use. All you need is the 11-character video ID found at the end of the video link (after the /watch?v=) and your username. Upon starting, you will be greeted with the following

![What you see on startup](https://i.imgur.com/el8Cfos.png)

Upon entering a valid video ID, the program will let you know it's listening for whatever username you enter.

![Successful ID entered](https://i.imgur.com/0l21xLu.png)

After you enter a username and it detects that a message has gone through, it will tell you the message it saw and what time and date it was recieved at in whatever your computer time is set to.

![Found a comment](https://i.imgur.com/Q1Kbc5T.png)

Messages with member emotes will display the emote shortcut text instead of the actual emote. Built in emotes with a unicode equivalent will display in unicode.

## Features
* Stays on top of other windows, even in fullscreen
* Can be opened multiple times to track as many youtube chats as you'd like
* Outputs message text when detected
* Outputs time and date of latest message sent
* Detects if youtube ID is invalid
* Does not have to be ran on same computer you're sending messages on

## Requirements 
A computer running Windows is required to run the precompiled version in the releases section. Support for a precompiled version is planned for macOS down the line.

You only need [pytchat 0.5.3](https://pypi.org/project/pytchat/) to run this successfully. A requirements.txt is included. Simply `pip install -r requirements.txt` to get all dependencies.

This was made in Python 3.9.2.
