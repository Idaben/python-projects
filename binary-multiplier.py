import math

a = float(input("Enter multiplicand\n"))
if a < 16:
    b = float(input("Enter multiplier\n"))
else:
    print("Must be a 4-bit binary number\n")

if b < 16:
    sum = 0
    print(sum)
    count = 0

    while True:
            if count == b:
             break
            else:
                count = count +1
                sum = sum +a
                print(sum)

else:print("Must be a 4 bit binary")

print("The final answer is", sum)
