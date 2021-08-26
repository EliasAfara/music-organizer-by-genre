# Music Organizer by Genre
Organize a huge number of music audio files into distinct folders based on audio genre metadata.

## Libraries Used 🚀

- [os](https://docs.python.org/3/library/os.html)
- [Shutil](https://docs.python.org/3/library/shutil.html)
- [time](https://docs.python.org/3/library/time.html)
- [tinytag](https://pypi.org/project/tinytag/)

### Install tinytag

```bash
pip3 install tinytag
```
You need to modify `dir_path` and `output_path` to the path of your liking inside [music_organizer.py](music_organizer.py) as shown below:

```python
dir_path = '../../Music/'
output_path = '../../Playlists/'
```
