# This is just a test for classes
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import AudioFileClip
import time
import multiprocessing
import os
import eyed3
import asyncio

start = time.time()

#Test URL Daft Punkt |Discover: https://www.youtube.com/playlist?list=PLSdoVPM5WnndLX6Ngmb8wktMF61dJirKl

#get Input
print("Post your URL here: ")
in_playlistURL = input()
print("Choose Path: ")
in_path = "C:\Temp"
print("Artist: ")
in_artist = input()
print("Album: ")
in_album = input()

#Get Playlist List
playlist = Playlist(in_playlistURL)
in_urls = playlist.video_urls


class PlayListDownlaod:
    def __init__(self, url, path, artist, album):
        self.url = url
        self.path = path
        self.artist = artist
        self.album = album

    async def downloadVideo(self):
        # Get Video
        var_video = YouTube(self.url)
        time.sleep(0.05)

        # Get Title from Video
        var_title = var_video.title
        time.sleep(0.05)

        # Select Stream
        var_stream = var_video.streams.order_by("bitrate").filter(only_audio=True, file_extension="mp4").last()

        # Store File in Variable
        var_File = var_stream.download(self.path)
        var_newFile, ext = os.path.splitext(var_File)

        # Convert File
        audio = AudioFileClip(os.path.abspath(var_File))
        audio.write_audiofile(var_newFile + ".mp3")
        audio.close()
        os.remove(os.path.abspath(var_File))

        # Get Metadata
        finalFile = eyed3.load(os.path.abspath(var_newFile + ".mp3"))
        finalFile.tag.artist = self.artist
        finalFile.tag.album = self.album
        finalFile.tag.title = var_title
        finalFile.tag.save()

        print("Finished Download and Converting of: " + var_title)



end = time.time()
print("Download took: " + str(end - start) + " Seconds")
