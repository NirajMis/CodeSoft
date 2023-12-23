# # # number = 12345
# # # first_digit = number % 10 ^ 4
# # # print(first_digit)
# # # the reverse number
# # # a = int(input("4 digit a"))
# # # reversed_a = int(str(a)[::-1])
# # # print("reversed number", reversed_a)
# # # number = int(input("Enter a 4-digit number: "))
# # # reversed_number = int(str(number)[::-1])
# # # print("Reversed number:", reversed_number)
# # # Swap using third variable
# # # a = 20
# # # b = 30
# # # temp = a
# # # a = b
# # # b = temp
# # # a = 5
# # # b = 10

# # # print("Before swapping:")
# # # print("a =", a)
# # # print("b =", b)

# # # temp = a
# # # a = b
# # # b = temp

# # # print("\nAfter swapping:")
# # # print("a =", a)
# # # print("b =", b)
# # # Demonstrate macro definition
# # # def repeat_func(n)
# # def repeat_func(n):
# #     def decorator_func(func):
# #         def wrapper(*args, **kwargs):
# #             for _ in range(n):
# #                 result = func(*args, **kwargs)
# #             return result
# #         return wrapper
# #     return decorator_func

# # @repeat_func(3)
# # def greet(name):
# #     print(f"Hello, {name}!")

# # greet("Niraj")

# def find_max_min(arr):
#     maximum = minimum = arr[0]  # Step 2

#     for num in arr[1:]:  # Step 3
#         if num > maximum:
#             maximum = num  # Step 4a
#         if num < minimum:
#             minimum = num  # Step 4b

#     return maximum, minimum  # Step 5
up 

# Find Missing Number in Array
arr1 = list(
    map(int, input("Enter space-separated elements of the array: ").split()))
n = len(arr1) + 1
a = min(arr1)  # arr1[0]
for i in range(a, a + n + 1):
    if i not in arr1:
        print("Missing Number:", i)
        break
