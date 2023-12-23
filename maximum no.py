# Taking input of five numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))


max_num = num1

if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
if num4 > max_num:
    max_num = num4
if num5 > max_num:
    max_num = num5

print("The maximum number is:", max_num)
