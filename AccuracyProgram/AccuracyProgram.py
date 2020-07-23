
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier

#database

MainDatabase = pd.read_excel(r'../Database/FinalDatabase.xlsx')
print(MainDatabase.head())
# base on database we will set iloc
x = MainDatabase.iloc[:, 1:5].values  #independent variables
print('independent:',x)
y = MainDatabase.iloc[ : , -1].values #dependent variables
print('dependent:',y)
#datauserate



#datauserate

thirtypercent=0.30  # training size 70%
fourtypercent=0.40   # training size 60%
fiftypercent=0.50    # training size 50%
sixtypercent=0.60    # training size 40%
seventypercent=0.70   # training size 30%


#knn

print("########## KNN algorithm ###########")

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=thirtypercent, random_state=0)
knn=KNeighborsClassifier(n_neighbors=3,p=2)
knn.fit(X_train,y_train)
score=knn.score(X_test,y_test)
print("test size=30, accuracy = {0:.2f}".format(100*score),"%")


X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=fourtypercent, random_state=0)
knn=KNeighborsClassifier(n_neighbors=3,p=2)
knn.fit(X_train,y_train)
score=knn.score(X_test,y_test)
print("test size=40, accuracy = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fiftypercent, random_state=0)
knn=KNeighborsClassifier(n_neighbors=3,p=2)
knn.fit(X_train,y_train)
score=knn.score(X_test, y_test)
print("test size=50, accuracy = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=sixtypercent, random_state=0)
knn=KNeighborsClassifier(n_neighbors=3,p=2)
knn.fit(X_train,y_train)
score=knn.score(X_test, y_test)
print("test size=60, accuracy = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=seventypercent, random_state=0)
knn=KNeighborsClassifier(n_neighbors=3,p=2)
knn.fit(X_train,y_train)
score=knn.score(X_test, y_test)
print("test size=70, accuracy = {0:.2f}".format(100*score),"%")



#naive bayes
print("\n########## Naive Bayes algorithm ###########")
gnb = GaussianNB()

X_train, X_test, y_train, y_test=train_test_split(x, y,test_size=thirtypercent, random_state=0)
gnb.fit(X_train, y_train)
#Predict the response for test dataset
pred = gnb.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=30, accuracy = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y,test_size=fourtypercent, random_state=0)
gnb.fit(X_train, y_train)
#Predict the response for test dataset
pred = gnb.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=40, accuracy = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fiftypercent, random_state=0)
gnb.fit(X_train, y_train)
#Predict the response for test dataset
pred = gnb.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=50, accuracy = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=sixtypercent, random_state=0)
gnb.fit(X_train, y_train)
#Predict the response for test dataset
pred = gnb.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=60, accuracy = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y,test_size=seventypercent, random_state=0)
gnb.fit(X_train, y_train)
#Predict the response for test dataset
pred = gnb.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=70, accuracy = {0:.2f}".format(100*score),"%")


print("\n########## Decision tree algorithm ###########")

dtc = DecisionTreeClassifier()
X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=thirtypercent, random_state=0)
clf = dtc.fit(X_train,y_train)

#Predict the response for test dataset
pred = clf.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=30, accuracy = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fourtypercent, random_state=0)
clf = dtc.fit(X_train,y_train)

#Predict the response for test dataset
pred = clf.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=40, accuracy = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fiftypercent, random_state=3)
clf = dtc.fit(X_train,y_train)

#Predict the response for test dataset
pred = clf.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=50, accuracy = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=sixtypercent, random_state=0)
clf = dtc.fit(X_train,y_train)

#Predict the response for test dataset
pred = clf.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=60, accuracy = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=seventypercent, random_state=0)
clf = dtc.fit(X_train,y_train)

#Predict the response for test dataset
pred = clf.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=70, accuracy = {0:.2f}".format(100*score),"%")


print("\n########## SVM algorithm ###########")

clf = svm.SVC(kernel='linear') # Linear Kernel
X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=thirtypercent, random_state=0)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=30, accuracy = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fourtypercent, random_state=0)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=40, accuracy = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fiftypercent, random_state=0)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=50, accuracy = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=sixtypercent, random_state=0)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=60, accuracy = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=seventypercent, random_state=0)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
score=metrics.accuracy_score(y_test, pred)
print("test size=70, accuracy = {0:.2f}".format(100*score),"%")


print("\n########## Random Forest Algorithm ###########")
X_train, X_test, y_train, y_test=train_test_split(x, y,test_size=thirtypercent, random_state=0)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print("test size=30, accuracy = {0:.2f}".format(100*metrics.accuracy_score(y_test, y_pred)),"%")


X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=fourtypercent, random_state=0)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print("test size=40, accuracy = {0:.2f}".format(100*metrics.accuracy_score(y_test, y_pred)),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fiftypercent, random_state=0)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print("test size=50, accuracy = {0:.2f}".format(100*metrics.accuracy_score(y_test, y_pred)),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=sixtypercent, random_state=0)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print("test size=60, accuracy = {0:.2f}".format(100*metrics.accuracy_score(y_test, y_pred)),"%")


X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=seventypercent, random_state=0)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print("test size=70, accuracy = {0:.2f}".format(100*metrics.accuracy_score(y_test, y_pred)),"%")