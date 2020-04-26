#Youtube Downloader by Philipp
#Python 3.7 using Tkinter | pytube

"""
Features:
* Download YT Video to Specific Path
* Convert to mp3
* select your Own MetaData

Features Missing:
* Downlaod Playlist
* Operate Anyware (exe/webinterface)
"""


from tkinter import *
from tkinter import messagebox

#Load Modules
try:
	from pytube import YouTube
	from pytube import Playlist
	from moviepy.editor import *
	import eyed3
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
	width = 48, height=2
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
	width = 0,
	).grid(row=4, columnspan=2)

#GUI | Otions
Label(root, relief=GROOVE,
	text = "Options",
	bg = "orange",
	font = "15",
	width = 48, height=1
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


#DownloadButton Function
def onClick():
	#Define Error Message:
	if (url.get() == "") or (path.get() == "") or (title.get() == "") or (artist.get() == "") or (album.get() == ""):
		messagebox.showerror("Error", "There is at least one Field Emtpy!")

	#DownloadVideo
	#GetVideo
	yt = YouTube(url.get())
	#Select best Audio Stream (mp3)
	stream = yt.streams.order_by("bitrate").filter(only_audio=True, file_extension="mp4").last()

	#Store File in Variable
	File = stream.download(path.get())

	# Rename File

	base = os.path.dirname(File)
	newFile = base + "\\" + title.get() + '.mp4'
	os.rename(File, newFile)


	#Convert File
	audio = AudioFileClip(os.path.abspath(newFile))
	audio.write_audiofile(os.path.dirname(newFile) + "\\" + title.get() + ".mp3")
	os.remove(os.path.abspath(newFile))

	#Get Metadata
	finalFile = eyed3.load(os.path.dirname(newFile) + "\\" + title.get() + ".mp3")
	finalFile.tag.artist = artist.get()
	finalFile.tag.album = album.get()
	finalFile.tag.title = title.get()
	finalFile.tag.save()

	# Download is Done Messafe
	Message = Label(root, width=60, bg="red", text="Download is done")
	Message.grid(row=11, columnspan=2, ipadx=0)
	Message.after(4000, Message.grid_forget)


#resetButton
def onClickReset():
	url.delete("0", "end")
	#path.delete("0", "end")
	title.delete("0", "end")
	artist.delete("0", "end")
	album.delete("0", "end")

def clearTitle():
	url.delete("0", "end")
	title.delete("0", "end")


dlButton = Button(root, text="Download", bg="gray", command=onClick)
dlButton.grid(row=9, columnspan=2, ipadx=100)

resetButtonall = Button(root, text="Empty Input", command=onClickReset)
resetButtonall.grid(row=10, ipadx=30, sticky=W)

resetButtonCurrent = Button(root, text="Only Clear Title", command=clearTitle)
resetButtonCurrent.grid(row=10,column=1, ipadx=38)


root.mainloop()
