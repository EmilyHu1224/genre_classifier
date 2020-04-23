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

# TODO import data from the .npy files

# Classifier section
# GridSearch to find best parameters
# ripped from: http://scikit.ml/api/skmultilearn.adapt.mlknn.html
# Wont work until the data is sorted out
parameters = {'k': range(1,3), 's': [0.5, 0.7, 1.0]}
score = 'f1_macro'

classifier = GridSearchCV(MLkNN(), parameters, scoring=score)
classifier.fit(X_train, Y_train)

print (classifier.best_params_, classifier.best_score_)

# predict
predictions = classifier.predict(X_test)
