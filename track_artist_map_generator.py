import json
import sqlite3

conn = sqlite3.connect('mxm_database.db')
rows = conn.execute('\
    SELECT DISTINCT lyrics.track_id, artist_id\
    FROM lyrics\
    INNER JOIN songs ON lyrics.track_id = songs.track_id\
').fetchall()

track_artist_map = {}
for r in rows:
    track = r[0]
    artist = r[1]
    track_artist_map[track] = artist

    if artist not in artist_genre_map:
        artist_genre_map[artist] = set()

print(json.dumps(track_artist_map))