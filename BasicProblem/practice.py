
w=['দেখার','অনেক','অভিবাসন','দেখার','আবার']
pro=['অ','অঘা','অজ','অনা','কু','আ']

maxlen=1
found=0
sw=list(w[0])
print(sw)
spro=list(pro[0])
print(sw[0:maxlen])
m="".join(sw[0:maxlen])
for i in pro:
    if i == m:
        found=found+1
        break
    else:
        found=0
if found >= 1:
    print("found")
else:
    print("not found")
# if(pro[0]==m):
#     print("found")



# for i  in w[0]:
#     print(i)
#     for j in pro:
#         if j == i:
#             print("found")
#             break
#         else:
#             print("not found")
#             break
#     break