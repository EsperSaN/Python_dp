#!/usr/bin/python3

arr1 = [2, 8, 9, 48, 8, 22, -12, 2]
arr2 = set()
for num in arr1 :
    if num > 5 :
        arr2.add(num+2)
print(arr1)
print(arr2)