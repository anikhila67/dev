ip = 'aaabbbbccddd'
# ot = 3a4b2c3d
temp = ip[0]
count = 0
arr = []
for i in [*ip]:
    # print(i)
    if temp == i:
        count+=1
    else:
        arr.append(str(count) + temp)
        temp = i
        count = 1
arr.append(str(count) + temp)

print(''.join(arr))