#p4a3
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by 0!")
#print separation
print()
#p4a4
try:
    print(x) #change out x with other things that might cause an error as well
except ZeroDivisionError:
    print("Cannot divide by 0!")
except NameError:
    print("A variable was used before assignment")
