import sqlite3
import pandas as pd
import numpy as np
from skmultilearn.adapt import MLkNN
from sklearn.model_selection import GridSearchCV

# References
# article for MLkNN
#{
#  zhang2007ml,
#  title={ML-KNN: A lazy learning approach to multi-label learning},
#  author={Zhang, Min-Ling and Zhou, Zhi-Hua},
#  journal={Pattern recognition},
#  volume={40},
#  number={7},
#  pages={2038--2048},
#  year={2007},
#  publisher={Elsevier}
#}


# Data input
conn = sqlite3.connect('C:/Users/ianev/Desktop/School/4B Stuff/SYDE 522/Project/mxm_dataset.db')
dataframeColumns = []
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
data = {}
for column in dataframeColumns:
    # fill in the data with zeros
    data[column] = 0

for row in conn.execute('''SELECT word, count FROM lyrics
                           WHERE mxm_tid = 4623710'''):
    # Fill in the word counts
    word = row[0]
    count = row[1]
    data[word] = count

# TODO fill in the genre flags!

# Create the panadas dataframe
df = pd.DataFrame(data, columns = dataframeColumns, index = [0])

# TODO split up input and output data
X_train = df.iloc[:,0:-18].to_numpy()
Y_train = df.iloc[:,-18:-1].to_numpy()

X_test = []
Y_test = []


# Classifier section
classifier = MLkNN(k=3)

# train -- won't run until the data is set up properly
#classifier.fit(X_train, Y_train)

# predict
#predictions = classifier.predict(X_test)
