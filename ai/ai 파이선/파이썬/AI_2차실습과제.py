Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sklearn import datasets
>>> from sklearn import svm, tree
>>> from sklearn.ensemble import RandomForestClassifier
>>> from sklearn.model_selection import cross_val_score, train_test_split
>>> import numpy as np
>>> digit = datasets.load_digits()
>>> x_train, x_test, y_train, y_test = train_test_split(digit.data, digit.target, train_size=0.6)
>>> s = svm.SVC(gamma=0.001)
>>> accuracies_svm = cross_val_score(s, x_train, y_train, cv=5)
>>> print("\nSVM의 정확률: ", accuracies_svm)

SVM의 정확률:  [0.98611111 0.98148148 0.98148148 1.         0.99069767]
>>> print("정확률(평균)=%0.3f, 표준편차 =%0.3f" % (accuracies_svm.mean() * 100, accuracies_svm.std()))
정확률(평균)=98.795, 표준편차 =0.007
>>> t = tree.DecisionTreeClassifier()
>>> accuracies_tree = cross_val_score(t, x_train, y_train, cv=5)
>>> print("\n결정트리의 정확률: ", accuracies_tree)

결정트리의 정확률:  [0.83796296 0.84259259 0.77314815 0.87906977 0.84651163]
>>> print("정확률(평균)=%0.3f, 표준편차 =%0.3f" % (accuracies_tree.mean() * 100, accuracies_tree.std()))
정확률(평균)=83.586, 표준편차 =0.035
>>> r = RandomForestClassifier()
>>> accuracies_rf = cross_val_score(r, x_train, y_train, cv=5)
>>> print("\n랜덤포리스트의 정확률: ", accuracies_rf)

랜덤포리스트의 정확률:  [0.97685185 0.96296296 0.96759259 0.99534884 0.97209302]
>>> print("정확률(평균)=%0.3f, 표준편차 =%0.3f" % (accuracies_rf.mean() * 100, accuracies_rf.std()))
정확률(평균)=97.497, 표준편차 =0.011
>>> s.fit(x_train, y_train)
SVC(gamma=0.001)
>>> print('\n테스트 집합에 대한 정확률=%0.3f' % s.score(x_test, y_test))

테스트 집합에 대한 정확률=0.989
