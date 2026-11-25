import sys

# a = int("257")
# b = int("257")
# print(a is b)

print("This numbers in hash")
hesh = [i for i in range(-500, 500) if (sys.getrefcount(i) > 4)]

print(hesh)