import os
import time
import shutil
from tinytag import TinyTag

dir_path = '../../Arabic/'
output_path = '../../Playlists/Arabic/'
file_list = os.listdir(dir_path)

genre_list = []

for file in file_list:
    tag = TinyTag.get(dir_path + file)
    if type(tag.genre) != str:
        # Genre is unknown if its type is NoneType
        # Appending Unkown instead of None of type NoneType
        genre_list.append('Unknown')
    else:
        genre_list.append(tag.genre)

# Removing duplicated genre from the list
res = list(set(genre_list))

genre = []
for name in res:
    modified_name = name.replace("/", "-")
    genre.append(modified_name)

for dir in genre:
    if not os.path.exists(dir):
        try:
            os.mkdir(os.path.join(output_path, dir))
        except FileExistsError:
            time.sleep(0.001)  # Prevent high load in pathological conditions

for file_name in file_list:
    tag = TinyTag.get(dir_path + file_name)
    if tag.genre is not None:
        genre_name = (tag.genre).replace("/", "-")
        if genre_name in genre:
            shutil.move(os.path.join(dir_path, file_name),
                        os.path.join(output_path, genre_name))
    else:
        genre_name = 'Unknown'
        if genre_name in genre:
            shutil.move(os.path.join(dir_path, file_name),
                        os.path.join(output_path, genre_name))
