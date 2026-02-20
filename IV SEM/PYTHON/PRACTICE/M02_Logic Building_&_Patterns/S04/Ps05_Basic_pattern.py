'''
# 4*r*c
n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

#lower triangle
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*" ,end= " ")
    print()

#inverted traingle
n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

#print
n = int(input())
num = 1
for i in range(n+1):      
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()
#a to d
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#print a,.....j
n = int(input())
ch = 65
for i in range(n):
    for j in range(i+1):
        print(chr(ch), end=" ")
        ch += 1
    print()
'''
#hallow square
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
