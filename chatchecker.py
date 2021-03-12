import pytchat
import tkinter as tk
#from playsound import playsound
import threading
import time
import os
import tempfile
import iconData

#global to allow tracking of whether the checkChat thread should be running
killThread = False

#global used to pass the date between threads
date = ""

#gets a the path of a file included in the executable
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#runs whenever the user changes the video ID
def videoIDCallback(*args):
    global killThread
    shortenedID = videoID.get()[0:11]
    videoID.set(shortenedID)
    
    if len(videoID.get()) < 11:
        lbl_status["text"] = "Waiting for valid Video ID"
        lbl_status["bg"] = "#FF8888"
        killThread = True
        return
    
    try:
        global chat
        chat = pytchat.create(video_id=videoID.get())
    except pytchat.exceptions.InvalidVideoIdException:
        lbl_status["text"] = "The specified ID was not found."
        killThread = True
        return

    if chat.is_alive():
        lbl_status["text"] = "Connected, listening for messages from specified username"
        lbl_status["bg"] = "#91FF81"
        killThread = False
        thread_checkChat = threading.Thread(target=checkForMessage)
        thread_checkChat.start()

#check for messages while the GUI mainloop does its important stuff
def checkForMessage():
    while not killThread:
        while chat.is_alive() and not killThread:
            for c in chat.get().sync_items():
                if c.author.name == username.get():
                    global date
                    date = c.datetime
                    latestMessage.set("Latest message from " + username.get() + ": " + c.message)
    return

#inform the user that a new message has been received
def ifNewMessage(*args):
    global date
    lbl_received["text"] = "Last message received at " + date
    lbl_received["bg"] = "#91FF81"
    #playsound("alert.mp3", False)

#parse the raw icon data to make an image, and store it temporarily 
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(iconData.ICON)

#making the window
window = tk.Tk()
window.wm_attributes("-topmost", 1)
window.title("YT Message Checker")
window.iconbitmap(ICON_PATH)

#making frames to hold widgets
frm_title = tk.Frame(master=window)
frm_videoID = tk.Frame(master=window)
frm_username = tk.Frame(master=window)
frm_status = tk.Frame(master=window)
frm_latestMessage = tk.Frame(master=window)
frm_received = tk.Frame(master=window)

#making widgets
lbl_title = tk.Label(master=frm_title, text="Youtube Live Message-Sent Verifier")

videoID = tk.StringVar()
videoID.trace_add("write",videoIDCallback)
lbl_videoID = tk.Label(master=frm_videoID, text="Video ID:   ")
ent_videoID = tk.Entry(master=frm_videoID, textvariable=videoID)

username = tk.StringVar()
lbl_username = tk.Label(master=frm_username, text="Username:")
ent_username = tk.Entry(master=frm_username, textvariable=username)

lbl_status = tk.Label(master=frm_status, text="Not tracking", bg="#FF8888", width=50)

latestMessage = tk.StringVar()
latestMessage.set("Waiting for message...")
latestMessage.trace_add("write",ifNewMessage)
lbl_latestMessage = tk.Label(master=frm_latestMessage, textvariable=latestMessage, justify=tk.LEFT, wraplength=350)

lbl_received = tk.Label(master=frm_received)

#packing widgets in frames
lbl_title.pack()

lbl_videoID.pack(side=tk.LEFT)
ent_videoID.pack(side=tk.LEFT)

lbl_username.pack(side=tk.LEFT)
ent_username.pack(side=tk.LEFT)

lbl_status.pack(fill=tk.X)

lbl_latestMessage.pack()

lbl_received.pack(fill=tk.X)

#packing frames in window
frm_title.pack()
frm_videoID.pack(anchor="w")
frm_username.pack(anchor="w")
frm_status.pack(fill=tk.X)
frm_latestMessage.pack(anchor="w")
frm_received.pack(fill=tk.BOTH)

#start the GUI
window.mainloop()

#once the window is closed, end the check chat thread
killThread = True