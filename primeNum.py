def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        # else:
    return True
num = 14
print(f'number is prime : ',prime(num))