# Using readlines() 
import json
file1 = open('airlines.xls', 'r') 
lines = file1.readline()
dicto={}
for lines in file1.readlines():
    pname=lines.split('"')[1]
    if pname in dicto:
        dicto[pname]+=1
    else:
        dicto[pname]=1
print("{")
m=list(dicto.keys())[0]
maxnum=dicto[m]
minnum=dicto[m]
maxstr=m
minstr=m
for x in dicto:
    if dicto[x]>maxnum:
        maxnum=dicto[x]
        maxstr=x
    elif dicto[x]<minnum:
        minnum=dicto[x]
        minstr=x
    print('"',x,'": ',dicto[x],',',sep='')
print("}")
print(maxstr,maxnum)
print(minstr,minnum)