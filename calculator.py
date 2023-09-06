import math
print("""            
select '1' for addition operation
select '2' for subtraction operation
select '3' for division operation
select '4' for multiplication operation
select '5' for square root operation
select '6' for finding the exponent operation
select '7' for factorial operation
select '8' for absolute value operation
select '9' for finding the nearest whole numbers ta a decimal number """)
number = int(input("Select the number of the task you want to:"))
total = 0
first_number = 0
multiplications_ = 1
first_input = 1
if number == 1:
    # it doesn't matter how many times you enter a number thanks to split
    numbers_to_add = input("Enter the numbers , leaving one space between each.:").split()
    for i in numbers_to_add:
        total += int(i)
    print(total)
elif number == 2:
    # it doesn't matter how many times you enter a number thanks to split
    subtraction = input("Enter the numbers, leaving one space between each.:").split()
    for j in subtraction:
        first_number = int(j) * 2
        break
    for p in subtraction:
        first_number -= int(p)
    print(first_number)
elif number == 3:
    # it doesn't matter how times you enter a number thanks to split
    division = input("Enter the numbers, leaving one space between each.:").split()
    for e in division:
        first_input = int(e) * int(e)
        break
    for w in division:
        first_input /= int(w)
    print(first_input)
elif number == 4:
    # it doesn't matter how times you enter a number thanks to split :)
    multiplication = input("Enter the numbers, leaving one space between each.").split()
    for g in multiplication:
        multiplication *= int(g)
    print(multiplication)
elif number == 5:
    square_root = input("Enter the number you want to use for the operation:")
    print(math.pow(int(square_root), 0.5))
elif number == 6:
    base, exponent = input("""Enter the numbers, leaving one space between each.
    first-base second-exponent:""").split()
    print(math.pow(int(base), int(exponent)))
elif number == 7:
    factorial = input("Enter the number you want to use for the operation:")
    print(math.factorial(int(factorial)))
elif number == 8:
    absolute_value = input("Enter the number you want to use for the operation:")
    print(math.fabs(int(absolute_value)))
elif number == 9:
    rounding = input("Enter the number you want to use for the operation:")
    print("floor is", math.floor(float(rounding)), "ceil is", math.ceil(float(rounding)))
