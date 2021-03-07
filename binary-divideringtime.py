

#Tamang kuha lang ng inputs
number0 = int(input("Enter a 4-bit number.\n"),2)
number1 = int(input("Enter a 4-bit number.\n"),2)
print("\n")

#Convert yung input to integer para mas madali
print("In integer form, those digits are...\n")
int(number0)
int(number1)
print(number0)
print(number1)
print("\n")

#Subraction Counter Variable
quotient = 0

#Eto yung mismong operation
while number0 > 0:
    number0 -= number1
    print(number0)
    quotient += 1

#Display ng final answers
print("\n")
print("The product is ", quotient)

number4 = ('{:b}'.format(quotient))
print("The product in binary is ",number4)
