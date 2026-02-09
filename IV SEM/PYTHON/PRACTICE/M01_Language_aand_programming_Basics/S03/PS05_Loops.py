'''
n = int(input("Enter a num: "))
for i in range(1,n+1):
    print(i , end = " ")

#while
i= 1
while i<=n:
    print(i)
    i +=1

#each character of 
name = "bharath kumar"
for ch in name:
    print(ch, end = " ")

name = "bharath kumar"
i = 0
while i < len(name):
    print(name[i])
    i += 1

name = "bharath kumar"
i = len(name) - 1

while i >= 0:
    print(name[i],end = " ")
    i -= 1

for i in range(10):
    if i == 8:
        break
    print(i)
'''
for i in range(5):
    if i == 2:
        continue
    print(i)

