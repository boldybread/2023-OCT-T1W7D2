# Take 3 numbers from the user, a, b, & c
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# is a > b?
if a > b:
    # if a > c?
    if a > c:
        # display a
        print(a)
    # else
    else:
        # display c
        print(c)
# else 
else:
    # if b > c
    if b > c:
        # display b
        print(b)
    #else
    else: 
        # display c
        print(c)