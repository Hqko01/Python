import pytube

link = input('url: ')
yt = pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded', link)