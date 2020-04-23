 #Youtube Downloader by Philipp
#Python 3.7 using Tkinter | pytube
#
#
#Variables needed: url, path, title, artis, album


from tkinter import *

#Load Modules
try:
	from pytube import YouTube
	from pytube import Playlist
	import os
except Exception as e:
	print("Module is Missing {}".format(e))


#GUI
root = Tk()

w = Label (root,
			text="YT Downloader by Lazy",
			fg = "black",
			font = "Verdana 15 bold").grid (row=0, column=0)

#GUI | YT Download
Label(root, relief=GROOVE,
	text = "Downloader",
	bg = "orange",
	font = "15",
	width = 47, height=2
	).grid(row=1, columnspan=2)
Label(root, relief=RIDGE,
	text = "Post your URL",
	width = 30,
	).grid(row=2, sticky = W)
Label(root, relief=RIDGE,
	text = "Download Directory:",
	width = 30,
	).grid(row=3, sticky = W)
Label(root,
	text = "",
	width = 60,
	).grid(row=4, columnspan=2)

#GUI | Otions
Label(root, relief=GROOVE,
	text = "Options",
	bg = "orange",
	font = "15",
	width = 47, height=1
	).grid(row=5, columnspan=2)

Label(root, relief=RIDGE,
	text = "Title:",
	width = 30,
	).grid(row=6, sticky = W)
Label(root, relief=RIDGE,
	text = "Artist:",
	width = 30,
	).grid(row=7, sticky = W)
Label(root, relief=RIDGE,
	text = "Album:",
	width = 30,
	).grid(row=8, sticky = W)



#TextBoxes
url = Entry(root)
path = Entry(root)
title = Entry(root)
artist = Entry(root)
album = Entry(root)


url.grid(row=2, column=1, ipadx =18)
path.grid(row=3, column=1, ipadx =18)

title.grid(row=6, column=1, ipadx =18)
artist.grid(row=7, column=1, ipadx =18)
album.grid(row=8, column=1, ipadx =18)

#Get Variables



#Button
def onClickReset():
	url.delete("0", "end")
	path.delete("0","end")
	title.delete("0","end")
	artist.delete("0","end")
	album.delete("0","end")

def onClick():
	Message = Label(root, width=60, text="Download has startet")
	Message.grid(row=10, columnspan=2, ipadx=0)

	resetButton = Button(root, text="Empty Input", bg="gray", command=onClickReset)
	resetButton.grid(row=11, columnspan=2, ipadx=100)


#Function
def downloadVid():
	vurl = url.get()
	ytd = Youtube(vurl).streams.filter(only_audio=True).first().download()





dlButton = Button(root, text="Download", bg="gray", command=onClick)
dlButton.grid(row=9, columnspan=2, ipadx=100)

root.mainloop()
