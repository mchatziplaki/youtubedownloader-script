from pytube import YouTube, Playlist
from sys import argv
import time

start_time = time.time()
link = argv[1]

yt_playlist = Playlist(link)

for video in yt_playlist.videos:
    print("Title: ", video.title)
    print('Views: ',"{:,}".format(video.views))
    print(f"File size: {video.filesize}")

    y_res = video.streams.get_highest_resolution()
    y_res.download("E:\\Youtube Videos")
    end_time = time.time()
    print(end_time - start_time)


print('All Done')