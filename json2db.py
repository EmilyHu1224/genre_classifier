import sqlite3
import json

GENRES = {
    'blues': 'blues',
    'comedy': 'comedy',
    'country': 'country',
    'classical': 'classical',
    'electronic': 'electronic',
    'electronica': 'electronic',
    'folk': 'folk',
    'house': 'house',
    'jazz': 'jazz',
    'pop': 'pop',
    'r&b': 'r&b',
    'soul': 'soul',
    'rock': 'rock',
    'hop': 'hip hop',
    'rap': 'hip hop',
    'metal': 'metal',
    'punk': 'punk',
    'disco': 'disco',
    'gospel': 'gospel',
    'christian': 'gospel',
    'easy': 'easy listening',
    'relax': 'easy listening'
}

def get_genres(tup):
    res = set()
    for t in tup:
        words = t.split(' ')
        for w in words:
            if w.lower() in GENRES:
                res.add(GENRES[w])
    
    return res

unique_genres = set(GENRES.values())
track_artist_map = json.load(open('track_artist_map.json', 'r'))
artist_genre_map = json.load(open('artist_genre_map.json', 'r'))

conn = sqlite3.connect('main.db')
conn.execute('CREATE TABLE "genres" (\
	"genre"	TEXT,\
	PRIMARY KEY("genre")\
)')
for g in unique_genres:
    conn.execute('INSERT INTO genres (genre) VALUES (?)', [g])

conn.execute('CREATE TABLE "artist_genre" (\
	"artist_id"	TEXT,\
	"genre"	TEXT,\
	FOREIGN KEY("genre") REFERENCES "genres",\
	FOREIGN KEY("artist_id") REFERENCES "artists"("artist_id")\
)')
for a in artist_genre_map.keys():
    for g in artist_genre_map[a]:
        conn.execute('INSERT INTO artist_genre (artist_id, genre) VALUES (?, ?)', [a, g])

conn.execute('CREATE TABLE "track_artist" (\
	"track_id"	TEXT,\
	"artist_id"	TEXT,\
	PRIMARY KEY("track_id"),\
	FOREIGN KEY("track_id") REFERENCES "songs"("track_id"),\
	FOREIGN KEY("artist_id") REFERENCES "artists"("artist_id")\
)')
for t, a in artist_genre_map.items():
    conn.execute('INSERT INTO artist_genre (artist, artist_id) VALUES (?, ?)', [t, a])

artist_genre_map = json.load(open('artist_genre_map.json', 'r'))
for t, a in track_artist_map.items():
    conn.execute('INSERT INTO track_artist (track_id, artist_id) VALUES (?, ?)', [t, a])

conn.commit()
conn.close()