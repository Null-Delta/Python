# variant 2

def power(a,n):
    return a if n == 1 else a * power(a, n - 1)

a = float(input())
n = int(input())

print(power(a,n))