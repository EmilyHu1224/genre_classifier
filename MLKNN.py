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

X_train = np.load('C:/Users/ianev/Documents/GitHub/genre_classifier/MLKNN_Xtrain.npy')
Y_train = np.load('C:/Users/ianev/Documents/GitHub/genre_classifier/MLKNN_Ytrain.npy')
X_test = np.load('C:/Users/ianev/Documents/GitHub/genre_classifier/MLKNN_Xtest.npy')
Y_test = np.load('C:/Users/ianev/Documents/GitHub/genre_classifier/MLKNN_Ytest.npy')

X_train_split = np.split(X_train, [5000])
Y_train_split = np.split(Y_train, [5000])

# Classifier section
# GridSearch to find best parameters
parameters = {'k': [4], 's': [0.5]}
score = 'accuracy'

clf = GridSearchCV(MLkNN(), parameters, scoring=score)
clf.fit(X_train_split[0], Y_train_split[0])

print (clf.best_params_, clf.best_score_)
