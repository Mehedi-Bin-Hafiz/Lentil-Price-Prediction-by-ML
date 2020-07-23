
import pandas as pd

import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 8})
plt.rcParams["font.family"] = "Times New Roman"

MainDatabase = pd.read_excel(r'../Database/LoadableDatabase.xlsx')
print(MainDatabase.head())
# base on database we will set iloc
# x = MainDatabase.iloc[:, :4].values  #independent variables
# print(x)
# y = MainDatabase.iloc[ : , -2].values #dependent variables
# print(y)

# plt.figure()
# andrews_curves(MainDatabase,'Price')
# plt.show()
eteen=MainDatabase.iloc[:365]
nteen=MainDatabase.iloc[-365:]
eighteen= eteen.sort_values('Price',ascending=True)
nineteen= nteen.sort_values('Price',ascending=True)



nineprice=nineteen.iloc[ : , -2].values


el=0
em=0
eh=0
eightlow=[]
eightmid=[]
eighthigh=[]
eightprice=eighteen.iloc[ : , -2].values
for i in eightprice:
    if i<55 and i>0:
        el=el+1
        eightlow.append(i)
    elif i < 60 and i >= 55:
        em=em+1
        eightmid.append(i)
    elif i >= 60:
        eh=eh+1
        eighthigh.append(i)
print("price about 2018:")
print("price bellow 40:",el)
print("price bellow 60:",em)
print("price upper 60:",eh)

nl=0
nm=0
nh=0
ninelow=[]
ninemid=[]
ninehigh=[]

nineteenprice=nineteen.iloc[ : , -2].values
for i in nineteenprice:
    if i < 56 and i > 0:
        nl=nl+1
        ninelow.append(i)
    elif i < 61 and i >= 56:
        nm=nm+1
        ninemid.append(i)
    elif i >= 61:
        nh=nh+1
        ninehigh.append(i)

print("\nprice about 2019:")
print("price bellow 40:",nl)
print("price bellow 60:",nm)
print("price upper 60:",nh)





year=['2018',"2019"]
eightdetails=[el,em,eh]
ninedetails=[nl,nm,nh]
data = [ eightdetails, ninedetails]
# Creates pandas DataFrame.
df = pd.DataFrame(data,index=['2018','2019'],columns=['low','mid','high'])
#it create 3 columns
print(df)
df.plot.bar(rot=0,color=['#ff9f43','#16a085','#ff6348'])
axes = plt.axes()
axes.set_ylim([1, 370])
plt.xlabel('Year')
plt.ylabel('Day')
plt.grid()
#plt.savefig('Price range.png') # need to call before calling show

plt.show()




"""Compere prediction class """

twentyrealdata=pd.read_excel(r'../Database/Real2020Data.xlsx')
RealPrice=[]
for ind in twentyrealdata.index:
    RealPrice.append((twentyrealdata['Classes'][ind]))

twentypredictprice=pd.read_csv(r'../Database/2020_3_month_prediction_Classes.csv')
PredictPrice=[]
for ind in twentypredictprice.index:
  PredictPrice.append((twentypredictprice['Classes'][ind]))
# print(len(PredictPrice))
# print(len(RealPrice))
Rl,Rm,Rh,Pl,Pm,Ph=0,0,0,0,0,0

for r in RealPrice:
    if r==0:
        Rl += 1
    elif r==1:
        Rm += 1
    elif r==2:
        Rh += 1
    else:
        pass
for p in PredictPrice:
    if p==0:
        Pl += 1
    elif p==1:
        Pm += 1
    elif p==2:
        Ph += 1
    else:
        pass

year=['Real Range ',"Predicted Range"]
RealClass=[Rl,Rm,Rh]
Predictedclass=[Pl,Pm,Ph]
data = [ RealClass, Predictedclass]
# Creates pandas DataFrame.
df = pd.DataFrame(data,index=['Real Range ',"Predicted Range"],columns=['low','mid','high'])
#it create 3 columns
print(df)
df.plot.bar(rot=0,color=['#12CBC4','#5758BB','#ff6348'])
axes = plt.axes()
axes.set_ylim([1, 100])
plt.grid()
plt.legend(['Low','Mid','High'])
plt.ylabel('Days')
plt.savefig('Real Class versus predicted Class.png')
plt.show()