A simple script that syncs your liked songs on Spotify to a playlist.


Requirements:
1. [Python](https://www.python.org/downloads/)
2. Pip (Run `python -m ensurepip` if its not installed)
3. Spotipy (Run `pip install spotipy`)


Setup (windows):

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/) and log in with your Spotify account.
2. Once logged in, go to the [Dashboard](https://developer.spotify.com/dashboard) and accept the terms.
3. Create an app and fill out the required details. Make sure the "Redirect URIs" is set to `http://localhost:8888/callback`.
4. Click on your app settings, copy the "Client ID", and paste it into `CLIENT_ID` in `sync.py`.
5. Click "View client secret", copy the "Client secret", and paste it into `CLIENT_SECRET` in `sync.py`.
6. 
Once you have completed the setup, you can run the `sync.py` file. All your liked songs will be synced to a playlist.


Automation (windows):

1. Place the `sync.bat` in the same folder as `sync.py`
2. Press Win+R and type `shell:startup`
3. create a shortcut in the startup folder to your `sync.bat` file
