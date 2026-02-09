
n = int(input("Enter a number: "))  # shows prompt in terminal
count = 0

print("Factors of", n, "are:")
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
        print(i, end=" ")

print("\nTotal number of factors:", count)

