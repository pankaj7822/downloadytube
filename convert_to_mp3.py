from pydub import AudioSegment
import os

files=os.listdir("data")
print(files)
for item in files:
    temp = item.split(".")
    audiofile=AudioSegment.from_file(os.path.join("data",item),format=temp[1])
    print("working on "+item)
    audiofile.export(os.path.join("Mp3",temp[0]+".mp3"),format="mp3")
    print("saved "+temp[0]+".mp3")