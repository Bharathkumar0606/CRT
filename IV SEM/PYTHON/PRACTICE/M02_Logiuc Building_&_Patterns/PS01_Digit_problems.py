'''
1)write a python code to num = 156787

num = 15678
count =len(str(num))
print(f"Number of digits:{count}")

#sum of digits of a given number
num = int(input("enter num"))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print(sum)

#products of digits of given number
num = int(input())
sum = 1
while num >0:
    sum *= num % 10
    num //=10
print(sum)

# revere a given number
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)
# reverse 
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)

#count the even and odd digits?
n = int(input("Enter n"))
even = 0
odd = 0
while n>0:
    d = n%10
    if d%2 == 0:
        even +=1
    else:
        odd +=1
    n //= 10
print(even)
print(odd)
'''
#largest digit of a given number
num = int(input())
largest = 0
while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit 
    num //= 10
print(largest)
