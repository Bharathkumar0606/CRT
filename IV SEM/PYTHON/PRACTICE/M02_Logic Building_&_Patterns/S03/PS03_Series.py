'''
#arthimetic
a = int(input("Enter first term: "))
d = int(input("Enter common difference: "))

n = 10  

for i in range(n):
    term = a + i*d
    print(term, end=",")

#fibonacci
n = int(input())
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
li = [0,1] # list
for i in range(2,n):
    li.append(li[i-2]+li[i-1])
print(li)


#fibonacci using list
n = int(input())
fib = [0, 1] 
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(*fib[:n])

#power of a number 
n = 2
terms = 5
power = 1
for i in range(1, terms + 1):
    power = power * n
    print(power, end=" ")

'''
n = int(input())

for i in range(1, 11):
    print(n ** i, end=" ")

