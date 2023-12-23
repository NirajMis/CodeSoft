
# numbers = []
# for i in range(5):
#     num = int(input("Enter number " + str(i+1) + ": "))
#     numbers.append(num)
# max_num = numbers[0]
# min_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num

# print("Maximum number:", max_num)
# print("Minimum number:", min_num)
# 5, 3, 9, 2, 8
# : Find the second largest element in an array.
# ○ Logic: Initialize two variables to store the largest and second-largest
# elements and iterate through the array.
# ○ Sample Input: [7, 3, 9, 2, 8]
# ○ Expected Output: Second Largest: 8
# #Find the Maximum and Minimum Elements:
# arr = list(map(int, input("Enter space-separated elements of the array: ").split()))
# arr.sort()
# a = arr[0]
# b = arr[-1]
# print("minimum number is ", a , "maximum number is ", b)




# #Remove Duplicates from Unsorted Array:
# arr = list(map(int, input("Enter space-separated elements of the array: ").split()))
# sets = set(arr)
# print(sets)

# #Intersection of Two Arrays:
# arr1 = list(map(int, input("Enter space-separated elements of the array: ").split()))
# arr2 = list(map(int, input("Enter space-separated elements of the array: ").split()))
# set1 = set(arr1)
# set2 = set(arr2)
# for i in set1:
#     for j in set2:
#         if i == j:
#             print("Intersection of Two Arrays element are : ", i)

# # Print given statement
# print("Hello, World!")

# # Declare & print variables
# a = 5
# b = 10
# print("Value of a:", a)
# print("Value of b:", b)

# # find sum of two numbers
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of a:"))
# sum=a+b
# print("sum:",sum)

# #difference of two number
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of a:"))
# diff=a-b
# print("difference:",diff)

# #multiplication of numbers
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of a:"))
# mul=a*b
# print("multiplication:",mul)

# #division of two numbers
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of a:"))
# div=a/b
# print("multiplication:",div)

# #find last digit number
# a=int(input("Enter the value of a:"))
# last_digit= a%10
# print("last digit:",last_digit)

# #Add two digits(last 2 digits) of a number
# a=input("Enter a number:")
# last_digit=print("last digit:",a[-1])
# second_last_digit=print("2nd last digit:",a[-2])
# sum=int(a[-1])+int(a[-2])
# print(sum)

# #Add two digits of a number
# a = int(input("Enter a number: "))
# sum = 0
# while a > 0:
#     temp = a % 10
#     sum = sum + temp
#     a = a // 10
# print(sum)

# # Find the Kth Largest Element:
# arr = list(map(int, input("Enter space-separated elements of the array: ").split()))
# arr.sort(reverse = True)
# k = int(input("enter the value of k: "))
# print(arr[k-1])

# #Intersection of Three Arrays:
# arr1 = list(map(int, input("Enter space-separated elements of the array: ").split()))
# arr2 = list(map(int, input("Enter space-separated elements of the array: ").split()))
# arr3= list(map(int, input("Enter space-separated elements of the array: ").split()))
# set1 = set(arr1)
# set2 = set(arr2)
# set3 = set(arr3)
# for i in set1:
#     for j in set2:
#         for k in set3:
#             if i == j == k:
#                 print(i)

# # Find Missing Number in Array
# arr1 = list(map(int, input("Enter space-separated elements of the array: ").split()))
# n = len(arr1) + 1
# a = min(arr1) #arr1[0]
# for i in range(a, a + n + 1):
#     if i not in arr1:
#         print("Missing Number:", i)
#         break

# # Reverse a List
# arr = list(map(int, input("Enter space-separated elements of the array: ").split()))
# arr.reverse()
# print(arr)
a = 73928
largest_a = a % 10
print("the second largest no", largest_a)
print("The value reprentation",a)