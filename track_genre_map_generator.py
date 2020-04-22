import json

track_artist_map = json.load(open('track_artist_map.json', 'r'))
artist_genre_map = json.load(open('artist_genre_map_MusicBrainz.json', 'r'))
track_genre_map = {}

for t, a in track_artist_map.items():
    if artist_genre_map[a]:
        track_genre_map[t] = artist_genre_map[a]

print(json.dumps(track_genre_map))