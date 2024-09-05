import glob, os
from moviepy.editor import *
from mutagen.easyid3 import EasyID3

PATH = "C:/Users/Karol/Desktop/"
SAVE_DIR_NAME = "Mp3 Files"

ALBUM = "album name"
ARTIST = "artist name"

os.chdir(PATH)

if not os.path.exists(SAVE_DIR_NAME):
    os.mkdir(SAVE_DIR_NAME)

print("Files found:")
i = 1
for file in glob.glob("*.mp4"):
    print(f"{i}. {file}")
    i += 1
    
    video = VideoFileClip(file)

    new_filename = file[:-1]+str(3)

    output_file = os.path.join(SAVE_DIR_NAME, new_filename)
    video.audio.write_audiofile(output_file)

    audio = EasyID3(output_file)
    audio['album'] = ALBUM
    audio['artist'] = ARTIST
    audio.save()

print("Conversion completed!")
