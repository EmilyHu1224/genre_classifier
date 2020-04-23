import sqlite3
import json
import numpy as np

# The total number of song rows is 237662, but not all the songs are classified
# The total number of classified songs is 96949
dataArray = np.zeros((96949, 5018), dtype=np.int8)
# track to genre mapping
trackGenreMap = json.load(open('C:/Users/ianev/Documents/GitHub/genre_classifier/track_genre_map.json','r'))

# Data input
conn = sqlite3.connect('C:/Users/ianev/Desktop/School/4B Stuff/SYDE 522/Project/mxm_dataset.db')
dataframeColumns = []
GENRES = {
    'blues': 1,
    'comedy': 2,
    'country': 3,
    'classical': 4,
    'electronic': 5,
    'folk': 6,
    'house': 7,
    'jazz': 8,
    'pop': 9,
    'r&b': 10,
    'soul': 11,
    'rock': 12,
    'hip hop': 13,
    'metal': 14,
    'punk': 15,
    'disco': 16,
    'gospel': 17,
    'easy listening': 18
}
genres = ['genre_blues',
          'genre_comedy',
          'genre_country',
          'genre_classical',
          'genre_electronic',
          'genre_folk',
          'genre_house',
          'genre_jazz',
          'genre_pop',
          'genre_r&b',
          'genre_soul',
          'genre_rock',
          'genre_hip_hop',
          'genre_metal',
          'genre_punk',
          'genre_disco',
          'genre_gospel',
          'genre_easy_listening']

# Make each word from the mxm_dataset an input column
for row in conn.execute('SELECT * FROM words'):
    word = row[0]
    dataframeColumns.append(word)

# Make each genre an output column
for label in genres:
    dataframeColumns.append(label)

# creating a data row
wordCol = {}
counter = 0
for column in dataframeColumns:
    # fill in the data with zeros
    wordCol[column] = counter
    counter = counter + 1

counter = 0

# for each song fill in a data row
for track_id in conn.execute('''SELECT DISTINCT track_id
                               FROM lyrics'''):
    if track_id[0] in trackGenreMap.keys():
        for row in conn.execute('''SELECT word, count FROM lyrics
                                WHERE track_id = ?''', track_id):
            # Fill in the word counts
            word = row[0]
            count = row[1]
            if word in wordCol.keys():
                dataArray[counter, wordCol[word]] = count

        for label in trackGenreMap[track_id[0]]:
            dataArray[counter, GENRES[label]-19] = 1

        counter = counter + 1
        if counter > 99998:
            break

train_test = np.split(dataArray, [77559], 0)
X_train_Y_train = np.split(train_test[0], [5000], 1)
X_test_Y_test = np.split(train_test[1], [5000], 1)

np.save('C:/Users/ianev/Documents/GitHub/genre_classifier/MLKNN_fullData.npy', dataArray)
np.save('C:/Users/ianev/Documents/GitHub/genre_classifier/MLKNN_Xtrain.npy', X_train_Y_train[0])
np.save('C:/Users/ianev/Documents/GitHub/genre_classifier/MLKNN_Ytrain.npy', X_train_Y_train[1])
np.save('C:/Users/ianev/Documents/GitHub/genre_classifier/MLKNN_Xtest.npy', X_test_Y_test[0])
np.save('C:/Users/ianev/Documents/GitHub/genre_classifier/MLKNN_Ytest.npy', X_test_Y_test[1])