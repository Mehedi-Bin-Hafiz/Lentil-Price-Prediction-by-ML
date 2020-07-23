import pandas as pd


import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 8})
plt.rcParams["font.family"] = "Times New Roman"

MainDatabase = pd.read_excel(r'../Database/RicePriceData.xlsx')
print(MainDatabase.head())



x = MainDatabase.iloc[:, :4].values  #independent variables
print(x)
y = MainDatabase.iloc[ : , -1].values #dependent variables
print(y)

plt.figure()
plt.show()


eighteen=MainDatabase.iloc[:365]
nineteen=MainDatabase.iloc[-365:]

eighteen_price=eighteen.iloc[: , -1].values
eightcount=[]
for i in range(1,len(eighteen_price)+1):
    eightcount.append(i)

nineteen_price=nineteen.iloc[: , -1].values
nine_count=[]
for i in range(1,len(nineteen_price)+1):
    nine_count.append(i)


plt.plot(eightcount,eighteen_price,color='red',linewidth=2)
plt.plot(nine_count,nineteen_price,color='green',linewidth=2)
axes = plt.axes()
axes.set_ylim([30, 90])
axes.set_xticks([1,31,59,90,120,151,181,212,243,273,304,334,365])
x_ticks_labels = ['1','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
axes.set_xticklabels(x_ticks_labels, rotation='vertical', fontsize=10)

plt.xlabel("Months")
plt.ylabel("price")
plt.legend(['2018','2019'])
plt.grid()
plt.savefig('price up down by line graph.png') # need to call before calling show
plt.show()



"""compare prediction with real price graph """

twentyrealdata=pd.read_excel(r'../Database/Real2020Data.xlsx')

RealPrice=[]
for ind in twentyrealdata.index:
    RealPrice.append((twentyrealdata['price'][ind]))


twentypredictprice=pd.read_csv(r'../Database/2020_3_month_prediction_price.csv')
PredictPrice=[]
for ind in twentypredictprice.index:
  PredictPrice.append((twentypredictprice['price'][ind]))
# print(len(PredictPrice))
# print(len(RealPrice))

XandYLen=[]
for i in range(1,len(RealPrice)+1):
    XandYLen.append(i)
axes = plt.axes()
plt.plot(XandYLen,RealPrice,color='red',linewidth=3)
plt.plot(XandYLen,PredictPrice,color='green',linewidth=3)
axes.set_yticks([35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
axes.set_xticks([1, 10,  20,  30,  40, 50, 60, 65])
plt.grid()
plt.legend(['Real Price','Predicted Price'])

plt.xlabel('Days')
plt.ylabel('Price')
plt.savefig('Real price versus predicted price.png')
plt.show()


