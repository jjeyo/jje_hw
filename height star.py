height = 10
# 방법 1
for n in range(height, 0, -1):
    print("{:>10}".format("*"*n))
print()

for n in range(0, height, 1):
    print("{:^21}".format("*"*(2*n+1)))

for n in range(1, height, 1):
    print("{:^19}".format(" *"*n))

# 방법 2
for n in range(height):
    print(" "*n+"*"*(height-n))
print()

for n in range(height):
    print(" "*(height-n)+"*"*(2*n+1))

for n in range(height):
    print(" "*(height-n), "*"*(2*n+1), sep="")

for n in range(height-1):
    if n < 1:
        pass
    else:
        print(" "*(height-n-2) + " *"*(n+1))
