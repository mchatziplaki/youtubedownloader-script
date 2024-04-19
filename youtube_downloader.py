from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)

print("Title: ", yt.title)
print('Views: ',"{:,}".format(yt.views))


y_res = yt.streams.get_highest_resolution()

y_res.download("E:\\Youtube Videos")

print('All Done')