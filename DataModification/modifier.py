
import pandas as pd



###sort based on price##

MainData = pd.read_excel(r'LentilRawData.xlsx')
MainDatabase = MainData.sort_values('Price')

price = MainDatabase.iloc[ : , -1].values


nz=0
no=0
nt=0
Classes=[]

for i in price:
    if i<92 and i>0:
        Classes.append(0)
        nz = nz + 1
    elif i < 110 and i >= 92:
        Classes.append(1)
        no = no + 1
    elif i >= 110:
        nt = nt + 1
        Classes.append(2)

MainDatabase.insert(7,"Classes",Classes,True)
MainDatabase.to_excel(r'../Database/FinalDatabase.xlsx', index=False)
print('Database generation is completed')
print("zero=",nz,"one=",no,"two=",nt)
