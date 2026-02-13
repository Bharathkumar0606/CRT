'''
n = int(input())
l=len(str(n))
res = 0
for i in str(n):
    res += int(i)**l
print("Armstrong" if n == res else "not Armstrong")

num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp = temp // 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

# perfect number
n = int(input())
sum = 0

for i in range(1, n//2+1):
    if n % i == 0:
        sum += i

if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")
'''
#Strong number
def factorial(n):
    if n<0:
        return "no factorial for -ve"
    elif n ==0 or n==1:
        return 1
    else:
        fact =1 
        for i in range(1,n+1):
            fact *=i
        return fact
s=0
n= int(input())
for i in str(n):
    s += factorial(int(i))
print("strong number" if n ==s else "not strong number")