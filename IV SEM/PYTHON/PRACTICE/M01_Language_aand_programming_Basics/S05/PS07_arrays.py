'''
import numpy as np

arr=np.array([10,20,30])
print(arr)

print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.mean(arr))
print("Even numbers list is:",np.arange(2,10,2))
print("odd numbers list is:",np.arange(1,10,2))


n = int(input("Enter the size"))
ele = list(map(int,input().split()))
print("Array Ele are:",np.array(ele))

#given an integer array nums return the third distinct max numbers in the array.if the third max does not exist,return the maximum number in python
nums = list(map(int,input("Enter nums").split()))
if len(set(nums)) >=3:
    print(sorted(set(nums))[-3])
else:
    print(max(nums))
'''
#monotonic array

def isMonotonic(nums):
    inc = True
    dec = True

    for i in range(1,len(nums)):
        if nums[i] > nums[i+ 1]:
            inc  = False
        if nums[i] < nums[i + 1]:
            dec  = False
    if inc or dec:
        print("Monotonic Array")
    else:
        print("not monotonic array")
