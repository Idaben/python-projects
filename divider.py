

#Kuha input
number0 = int(input("Enter the dividend.\n"))
number1 = int(input("Enter the divisor.\n"))
number3 = int()
print("\n")
#Subraction Counter Variable
quotient = 0

#Eto yung mismong operation
while number0 > 0:
    number0 -= number1
    print(number0)
    quotient += 1

#Display
print("\n")
print("The quotient is ", quotient)
