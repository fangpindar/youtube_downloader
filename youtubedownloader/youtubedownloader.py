# coding=utf-8
from pytube import YouTube
import os
import subprocess
import time

while True:
    url = input("Please input the url: ")
    yt = YouTube(url)

    #stream = yt.streams.first()
    # = yt.streams.filter(only_audio = True).all()
    stream= yt.streams.all()

    for i in range(len(stream)):
        print(i, '. ',stream[i])

    vnum = int(input("Enter the vid num you want:  "))
    #print(stream[vnum].filesize)
    name = input("Please input the ouput file name , Please do not use any strange symbol: ")
    new_filename = name+".mp3"
    default_filename = name
    
    print("Downloading, Please wait..........")

    stream[vnum].download(filename = default_filename)
    default_filename = default_filename+".mp4"

    ffmpeg = ('ffmpeg -i %s ' % default_filename + new_filename)

    subprocess.call(ffmpeg)

    print('done')

