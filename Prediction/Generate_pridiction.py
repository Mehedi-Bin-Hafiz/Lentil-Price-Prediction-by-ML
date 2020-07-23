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
MainDatabase = pd.read_excel(r'../Database/LoadableDatabase.xlsx')
# base on database we will set iloc
nx = MainDatabase.iloc[:, 1:5].values  #independent variables
ny = MainDatabase.iloc[ : , -1].values #dependent variables
print(nx)
print(ny)


nX_train,nX_test,ny_train,ny_test=train_test_split(nx,ny,test_size=0.3, random_state=3)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(nX_train,ny_train)
ny_pred=clf.predict(nX_test)
print("test size=40, accuracy = {0:.2f}".format(100*metrics.accuracy_score(ny_test, ny_pred)),"%")

# dtc = DecisionTreeClassifier()
# X_train, X_test, y_train, y_test=train_test_split(nx, ny, test_size=0.5, random_state=0)
# clf = dtc.fit(X_train,y_train)
#
# #Predict the response for test dataset
# pred = clf.predict(X_test)
# score=metrics.accuracy_score(y_test, pred)
# print("test size=50, accuracy = {0:.2f}".format(100*score),"%")

days=0
month=0
year=20
season=0
yearcode=0
normalprediction=[]
yearcode = 0
if (year % 2 == 0):
    yearcode = 4
else:
    yearcode = 2

for month in range(2,4):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        days=31
    elif month==2:
        days=28
    else:
        days=30
    #print("##################Month###################")
    for day in range(1,days+1):
        if ( month==1 and ( day >=1 and day<=31)):
            season=4
        elif (month==2 and ( day >=1 and day<=12)):
            season=4
        elif (month==2 and ( day >=13 and day<=28)):
            season=5
        elif (month==3 and ( day >=1 and day<=31)):
            season=5
        elif month==4 and ( day >=1 and day<=13):
            season=5
        elif month==4 and ( day >=14 and day<=30):
            season=0
        elif month==5 and ( day >=1 and day<=31):
            season=0
        elif month==6 and ( day >=1 and day<=14):
            season=0
        elif month==6 and ( day >=15 and day<=30):
            season=1
        elif month==7 and ( day >=1 and day<=31):
            season=1
        elif month==8 and ( day >=1 and day<=15):
            season=1
        elif month==8 and ( day >=16 and day<=31):
            season=2
        elif month == 9 and (day >= 1 and day <= 30):
            season = 2
        elif month == 10 and (day >= 1 and day <= 15):
            season = 2
        elif month == 10 and (day >= 16 and day <= 31):
            season = 3
        elif month == 11 and (day >= 1 and day <= 30):
            season = 3
        elif month == 12 and (day >= 1 and day <= 14):
            season = 3
        elif month == 12 and (day >= 15 and day <= 31):
            season = 4

        print("year=",year,"month=",month,"day=",day,"season=",season)
        ##############normal Prediction###################
        # Predict the response for test dataset
        pred = clf.predict([[year,day,month,season]])
        normalprediction.append(pred[0])
        pred=None

nz=0
no=0
nt=0
i=0
pfile = open("2020_3_month_prediction_Classes.csv", 'a')
print("normal=",normalprediction)
for i in normalprediction:
    if i == 0:
        nz = nz + 1
    elif i==1:
        no = no + 1
    elif i==2:
        nt = nt + 1
    pfile.write(str(i) + "\n")
print("zero=",nz,"one=",no,"two=",nt)

