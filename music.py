from __future__ import unicode_literals
import youtube_dl
from move import move_file

# Download function

def download(ydl_opts, url_list, new_path):

    '''
    Input: ydl options, dictionary with urls, path whereto you want to download the file
    '''

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for title, link in url_list.items():
            ydl.download([link])

            move_file(new_path)

# The YDL settings

ydl_opts = {
    'outtmpl':"%(title)s.%(ext)s",
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

url_list = {

    # Dictionary with the list of songs you want to download

    'XO Life':'https://www.youtube.com/watch?v=WrsFXgQk5UI'
}

download(ydl_opts, url_list, 'C:\\Users\\test\\person\\Music\\')
