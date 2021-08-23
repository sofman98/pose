from joblib import dump, load
from sklearn import svm
from sklearn.model_selection import train_test_split
import pandas as pd


dataset = pd.read_csv("vec_dataset.csv")
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
clf.fit(X_train, y_train)
print('Score',clf.score(X_test,y_test))


#dump(clf, 'weights_vec.joblib')

