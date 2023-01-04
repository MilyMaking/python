import pytube
link = input('Enter Youtube URL:')
yt = pytube.YouTube(link)
yt.streams.first().download()
print('downloaded', link)

