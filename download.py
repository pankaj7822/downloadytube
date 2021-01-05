from __future__ import unicode_literals
import youtube_dl

lists=[
"https://www.youtube.com/watch?v=NvE7RR0xyiA",
"https://www.youtube.com/watch?v=69AnkBcan4o",
"https://www.youtube.com/watch?v=khjTorvaYBg",
"https://www.youtube.com/watch?v=T7Z-8FleZA8",
"https://www.youtube.com/watch?v=Hfp3bhpcQQY",
"https://www.youtube.com/watch?v=EsHA96QGW9s",
"https://www.youtube.com/watch?v=EjEMbdyHQxk",
"https://www.youtube.com/watch?v=8nCERnmqtqU",
"https://www.youtube.com/watch?v=h7dPoBf-SgQ",
"https://www.youtube.com/watch?v=dcRXwluTRco",
"https://www.youtube.com/watch?v=XtLAkVdgKCI",
"https://www.youtube.com/watch?v=jmsYRiphhFg",
"https://www.youtube.com/watch?v=is7YGKVTr08",
"https://www.youtube.com/watch?v=h2ZAgBywl6s",
"https://www.youtube.com/watch?v=0bop8Fq8yyQ",
"https://www.youtube.com/watch?v=J2LkWtNpIyA",
"https://www.youtube.com/watch?v=8nCERnmqtqU",
"https://www.youtube.com/watch?v=3SPNVz3PiEI",
"https://www.youtube.com/watch?v=88hz-iunL9Y",
"https://www.youtube.com/watch?v=6kwmQSmhL0k",
"https://www.youtube.com/watch?v=BNd-PUhd0Vw",
"https://www.youtube.com/watch?v=d8uWXgGjBR0",
"https://www.youtube.com/watch?v=EsHA96QGW9s",
"https://www.youtube.com/watch?v=9T2weheH4ek",
"https://www.youtube.com/watch?v=AGz5wOOrbMI",
"https://www.youtube.com/watch?v=U4f2h3uNm0I",
"https://www.youtube.com/watch?v=VdvlgES-HBI"
]

mylist=list(dict.fromkeys(lists))

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
for item in mylist:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([item])
        except:
            pass
