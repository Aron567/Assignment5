n = int(input("Enter the length of the sequence: ")) # Do not change this line
x = 0
a = 1
b = 2
c = 3

for i in range(n):
    if x < 3:
        x += 1
        print(x)

    elif x >= 3:
        x = a + b + c
        a = b
        b = c
        c = x 
        print(x)

