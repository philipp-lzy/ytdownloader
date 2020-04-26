#testting of Playlist Download
#Test playlist: https://www.youtube.com/watch?v=_NdHySPJr8I&list=OLAK5uy_nfj-ClCRuKN6o4qzzJFbpdeLG1XwIPfb0

#Testresults:
#Download works fine, but sometimes it calls the Video just YouTube (?)
#Happens randomly and not allways...

from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
import eyed3
import os
import time

start = time.time()

playlist = Playlist("https://www.youtube.com/watch?v=_NdHySPJr8I&list=OLAK5uy_nfj-ClCRuKN6o4qzzJFbpdeLG1XwIPfb0")
urls = playlist.video_urls
n = len(urls)

for x in urls:
    #Get Video
    video = YouTube(x)

    #Get Title from Video
    title = video.title

    #Select Stream
    stream = video.streams.order_by("bitrate").filter(only_audio=True, file_extension="mp4").last()

    # Store File in Variable
    File = stream.download("C:\Temp")

    # Rename File   ---> Doesn't Work
    """
    base = os.path.dirname(File)
    newFile = base + "\\" + title + '.mp4'
    print(newFile)
    os.rename(File, newFile)
    """

    newFile, ext = os.path.splitext(File)

    # Convert File
    audio = AudioFileClip(os.path.abspath(File))
    audio.write_audiofile(newFile + ".mp3")
    os.remove(os.path.abspath(File))

    # Get Metadata
    finalFile = eyed3.load(os.path.abspath(newFile + ".mp3"))
    finalFile.tag.artist = "ACDC"
    finalFile.tag.album = "Rock or Bust"
    finalFile.tag.title = title
    finalFile.tag.save()

    print("Finished Download and Converting of: " + title)


print("Finished downloading Playlist")

end = time.time()
print("Download took: " + str(end - start) + "Seconds")
