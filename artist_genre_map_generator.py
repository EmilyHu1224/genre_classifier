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

conn = sqlite3.connect('main.db')
track_artist_map = json.load(open('track_artist_map.json', 'r'))
artist_genre_map = {a: set() for a in track_artist_map.values()}

for a in artist_genre_map.keys():
    terms = conn.execute('SELECT mbtag FROM artist_mbtag WHERE artist_id = ?', [a]).fetchall()
    for t in terms:
        genres = get_genres(t)
        if genres:
            artist_genre_map[a] |= genres

artist_genre_map_new = {a: list(artist_genre_map[a]) for a in artist_genre_map.keys()}

conn.close()
print(json.dumps(artist_genre_map_new))