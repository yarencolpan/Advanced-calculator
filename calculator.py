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
b = int(input("Select the number of the task you want to:"))
t = 0
h = 0
hh = 1
z = 1
if b == 1:
    # it doesn't matter how times you enter a number thanks to split :)
    a = input("Enter the numbers you want to use for the operation, leaving one space between each.:").split()
    for i in a:
        t += int(i)
    print(t)
elif b == 2:
    # it doesn't matter how times you enter a number thanks to split :)
    aa = input("Enter the numbers you want to use for the operation, leaving one space between each.:").split()
    for j in aa:
        h = int(j) * 2
        break
    for p in aa:
        h -= int(p)
    print(h)
elif b == 3:
    # it doesn't matter how times you enter a number thanks to split :)
    aaa = input("Enter the numbers you want to use for the operation, leaving one space between each.:").split()
    for e in aaa:
        z = int(e) * int(e)
        break
    for ee in aaa:
        z /= int(ee)
    print(z)
elif b == 4:
    # it doesn't matter how times you enter a number thanks to split :)
    aaa = input("Enter the numbers you want to use for the operation, leaving one space between each.").split()
    for ii in aaa:
        hh *= int(ii)
    print(hh)
elif b == 5:
    bbb = input("Enter the number you want to use for the operation:")
    print(math.pow(int(bbb), 0.5))
elif b == 6:
    ll, m = input("""Enter the numbers you want to use for the operation, leaving one space between each.
    first-number second-exponent:""").split()
    print(math.pow(int(ll), int(m)))
elif b == 7:
    gg = input("Enter the number you want to use for the operation:")
    print(math.factorial(int(gg)))
elif b == 8:
    u = input("Enter the number you want to use for the operation:")
    print(math.fabs(int(u)))
elif b == 9:
    uu = input("Enter the number you want to use for the operation:")
    print("floor is", math.floor(float(uu)), "ceil is", math.ceil(float(uu)))
