# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from pytube import YouTube
from pytube import Playlist
import helper
from pytube.cli import on_progress

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    playlist = Playlist(input("Enter the plylist url : "))
    print(f'Name of The Plylist is : {playlist.title}')
    print(f'Total Videos : {playlist.videos.cou}')
    folderPath = input("what the path you want to save in : ")
    isVideo = input("do you want to save this as video y=Yes/n=No : ") == "y"
    if isVideo:
        resolution = input("what resolution you want to save the video with : ")
    for video in playlist.videos:
        print(f'{video.title}')
        yt = YouTube(video.watch_url, on_progress_callback=helper.progress_func)
        if isVideo:
            yt.streams.filter(resolution=resolution).first().download(folderPath)
        else:
            yt.streams.filter(only_audio=True).first().download(folderPath)
        print('\n end downloading')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
