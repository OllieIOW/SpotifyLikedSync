import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime

# Set your credentials [Check the README.md for help with setup]
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'user-library-read playlist-modify-public'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

results = sp.current_user_saved_tracks()
liked_songs = []
while results:
    for item in results['items']:
        track = item['track']
        liked_songs.append(track['id'])
    if results['next']:
        results = sp.next(results)
    else:
        results = None

user_id = sp.current_user()['id']
playlist_name = 'Liked Songs Sync'
playlists = sp.user_playlists(user_id)
playlist_id = None
for playlist in playlists['items']:
    if playlist['name'] == playlist_name:
        playlist_id = playlist['id']
        break

if not playlist_id:
    playlist = sp.user_playlist_create(user_id, playlist_name)
    playlist_id = playlist['id']

sp.user_playlist_replace_tracks(user_id, playlist_id, liked_songs[:100])

for i in range(100, len(liked_songs), 100):
    sp.user_playlist_add_tracks(user_id, playlist_id, liked_songs[i:i+100])

sync_time = datetime.now().strftime("%d-%m-%Y @ %H:%M:%S")
description = f"This playlist was synced automatically at {sync_time}"
sp.user_playlist_change_details(user_id, playlist_id, description=description)

print(f'Synced {len(liked_songs)} liked songs to the playlist "{playlist_name}".')
print(f'Playlist description updated to: "{description}"')
