def fact(a):
    if (a == 1 or a == 0):
        return 1;
    else:
        return a * fact(a-1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {fact(num)}")