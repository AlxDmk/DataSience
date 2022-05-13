# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

n = int(input('Введите число ->'))

def summery(n, sum=0):
    if n ==1: return n
    while n > 0:
        sum+=n
        n-=1
        summery(n, sum)
    return sum
  
print(bool(summery(n) == (n*(n+1)/2)))
