#install pytube before running code using "pip install pytube"
import pathlib
from pytube import Playlist
from pytube import YouTube

def progress_function(stream, chunk, bytes_remaining):

    size = stream.filesize
    progress_bar(size-bytes_remaining, size)
    # p = 0
    # while p <= 100:
    #     progress = p
    #     print str(p)+'%'
    #     p = progress_bar(bytes_remaining, size)

def progress_bar(progress,total):
    percent =100*(progress/float(total))
    bar='█'*int(percent) + '-'*(100-int(percent))
    print(f"\r|{bar}| {percent:.2f}%",end="\r")
    if(int(percent)==100):
        print(f"\r|{bar}| {percent:.2f}%")
        print('Dowload Complete')


download_path=pathlib.Path.home()/"Downloads"

#playlist link
link=input("enter youtube link : ")
choise = int(input("Enter 1 to download the video, 2 to download full playlist \n"))
if(choise==2):
    try:
        p =Playlist(link)
        print(f'Downloading: {p.title}')
        download_path=f"{download_path}/{p.title}"
        for video  in p.videos:
            try:
                print(f'Downloading: {video.title}')
                video.register_on_progress_callback(progress_function)
                video.streams.get_highest_resolution().download(download_path)
            except:
                print("Error: Something happened during dowload")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Connectionn error..")
    
elif(choise==1):
    try:
        y =YouTube(link)
        y.register_on_progress_callback(progress_function)
    except:
        print("Connectionn error..")
    print(f'Downloading: {y.title}')
    download_path=download_path
    try:
        y.streams.get_highest_resolution().download(download_path)
    except:
        print("Error: Something happened during dowload")
    
else:
    print(" wrong choise")
