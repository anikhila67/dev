# ot = 3 # second minimum value

def secMini(arr):
    c = arr[0]
    arrr = []
    for i in arr:
        while c < i:
            # print(c)
            arrr.append(c)
            c = i
    return arrr

arr = [2,5,7,3,8,9]
print(secMini(arr))

# c = [3,5,6,8,2,1,]
# # print(sorted(set(c))[1]) 

# m1 = c[0] 
# for idx, i in enumerate(c): 
#     while m1 < i: 
#         if m1 < i: c[idx] = m1 
#             print(c) 
