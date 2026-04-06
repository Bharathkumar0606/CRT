'''
a= [12, 45, 7, 89, 34]
print(max(a))

#2) palindrome(using reversed() and join())
s = input("Enter a string: ")
rev = "".join(reversed(s))
if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#3) count even num
nums = [1, 2, 3, 4, 5, 6, 8]
count = list(filter(lambda x: x % 2 == 0, nums))
print(count)

#4) remove duplicates (using set())
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)

#5) sum of digits(using sum())
n = input("Enter a number: ")
digit_sum = sum(int(d) for d in n)
print("Sum of digits:", digit_sum)

#6) sort words alphabetically (using sorted())
a = ['bharath','apple']
print(list(sorted(a)))

#7) +finding common elements using set
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print(set(a) & set(b))


#8) index with value using enumerate()
fruits = ["apple", "banana", "mango"]
for index, value in enumerate(fruits):
    print(index, value)
'''
arr = list(map(int,input().split()))
seen=set()
for i in arr:
    if i in seen:
        print("Duplicate:",i)
        break
    seen.add(i)

   