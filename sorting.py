arr = [0,2,1,2,0,1,0]
# b = 8
temp = arr[0]
arra = []
for i in range(0,len(arr)):
    if i == len(arr)-1:
        # arra.append(temp)
        break
    if temp <= arr[i]:
        arra.append(temp)
        # temp = arr[i]
    else:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        # temp = arr[i]
    arra.append(temp)
    temp = arr[i+1]

print(arra)
