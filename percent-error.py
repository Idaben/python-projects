exp = float(input("Enter the Experimental Value\n"))
acp = float(input("Enter the Accepted or Actual Value\n"))


dif = ((exp - acp)/acp)
if dif < 0:
    dif = dif*-1
else:
    dif = dif*1

final_value = dif*100

print(".\n")
print(".\n")
print(".\n")
print(".\n")

print(final_value,)
