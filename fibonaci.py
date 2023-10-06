def fibo(num):
    n1 = 0
    n2 = 1
    c = 0
    if num <= 1:
        return n2
    else:
        while c < num:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            c +=1
        return n2

print(fibo(5)) # 0 1 1 2 3 5 8 13 21 34 ...