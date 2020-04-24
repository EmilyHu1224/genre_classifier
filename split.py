import sqlite3
import json
from collections import OrderedDict

GENRES = OrderedDict([
    ('blues', 1),
    ('comedy', 2),
    ('country', 3),
    ('classical', 4),
    ('electronic', 5),
    ('folk', 6),
    ('house', 7),
    ('jazz', 8),
    ('pop', 9),
    ('r&b', 10),
    ('soul', 11),
    ('rock', 12),
    ('hip hop', 13),
    ('metal', 14),
    ('punk', 15),
    ('disco', 16),
    ('gospel', 17),
    ('easy listening', 18)
])

def get_results(genres):
    return ' '.join([str(GENRES[g]) for g in genres]) + '\n'

track_genre_map = json.load(open('track_genre_map.json', 'r'))

TRAIN_FILE = 'train.txt'
TEST_FILE = 'test.txt'
TEST_RES_FILE = 'test_res.txt'

LINE_FORMAT = '{labels} | {features}\n'
LABEL_FORMAT = '{label}:{cost}'
FEATURE_FORMAT = '{word}:{count}'

conn = sqlite3.connect('mxm_dataset.db')

train_file = open(TRAIN_FILE, 'w')
test_file = open(TEST_FILE, 'w')
test_res_file = open(TEST_RES_FILE, 'w')

counter = 0
error_count = 0
for track_id, genres in track_genre_map.items():
    rows = conn.execute('SELECT word, count FROM lyrics WHERE track_id = ?', [track_id]).fetchall()
    
    try:
        labels = ' '.join([LABEL_FORMAT.format(label=l, cost=0 if g in genres else 1) for g, l in GENRES.items()])
        features = ' '.join([FEATURE_FORMAT.format(word=r[0], count=r[1]) for r in rows])
    except UnicodeEncodeError as e:
        # print(e)
        error_count += 1
    else:
        line = LINE_FORMAT.format(labels=labels, features=features)
        
        file = None
        if counter < 8:
            file = train_file
        else:
            file = test_file
            test_res_file.write(get_results(genres))

        file.write(line)
        counter = (counter + 1) % 10

train_file.close()
test_file.close()
# print(error_count)