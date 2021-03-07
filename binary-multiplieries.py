

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

#Tamang repeated addition
print("solution...")
number3 = int()

while number1 > 0:
    number3 += number0
    print(number0,"+")
    number1 -= 1

#Display ng final answers
print("\n")
print("The product is ", number3)

number4 = ('{:b}'.format(number3))
print("The product in binary is ",number4)
