# Creator---Fahim Ahmed                 # pip install pytube 
from pytube import YouTube              # importing Youtube from pytube
from pytube import Playlist             # importing playlist Module from pytube

print("\n What do you want to Download \n\n 1.Video\n 2.Playlist\n 3.Audio")
number =int(input(" Enter :"))                              # taking input from user

if number ==1:                                              # For Download Video Only
    link = input("\nEnter Link : ")
    youtube_1 = YouTube(link)

    print( youtube_1.title)

    video = youtube_1.streams.filter(only_video= True)     # filtering only video from link
    vid = list(enumerate(video))                           # List of video pixels
    for i in vid:
        print(i)

    strm = int(input("enter : "))
    print("Downloading.......")
    video[strm].download()
    print("Successfully")

elif number == 2:                                           # For Download Playlist
    link = input("Enter Link : ")
    py = Playlist(link)

    print(f'Downloading : {py.title}')

    for video in py.videos:
        video.streams.first().download()
    print("Successfully")

elif number == 3:                                              # For Download Audio
    link = input("Enter Link : ")
    youtube_1 = YouTube(link)

    print( youtube_1.title)

    video = youtube_1.streams.filter(only_audio = True)       # filtering only audio from link
    vid = list(enumerate(video))                              # List of though videos audio qulity
    for i in vid:
        print(i)

    strm = int(input("enter : "))
    print("Downloading.......")
    video[strm].download()
    print("Successfully")

else:
    print("Worng Input Please Try Again")    
