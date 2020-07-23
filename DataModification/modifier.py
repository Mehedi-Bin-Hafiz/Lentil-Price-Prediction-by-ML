#
# import pandas as pd
#
#
#
# ###sort based on price##
#
# MainData = pd.read_excel(r'LentilRawData.xlsx')
# MainDatabase = MainData.sort_values('Price', ascending=False)
#
# price = MainDatabase.iloc[ : , -1].values
#
#
# nz=0
# no=0
# nt=0
# Classes=[]
#
# for i in price:
#     if i<56 and i>0:
#         Classes.append(0)
#         nz = nz + 1
#     elif i < 61 and i >= 56:
#         Classes.append(1)
#         no = no + 1
#     elif i >= 61:
#         nt = nt + 1
#         Classes.append(2)
#
# MainDatabase.insert(7,"Classes",Classes,True)
# MainDatabase.to_excel(r'../Database/FinalDatabase.xlsx', index=False)
#
# print("zero=",nz,"one=",no,"two=",nt)
