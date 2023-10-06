arr = [1,1,1,2,3,3,3,3,4,5,6,6,7,7,7,8]
dic = {}
count = 0
ar = {}
for i in arr:
    if i in dic.keys():
        count+=1
    else:
        ar[i] = count
        count = 1

print(ar)
