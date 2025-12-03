a = int(input("Enter a value: "))

n = a if (a % 2 == 1) else (a - 1)

if n <= 0:
    print()  
else:
    print(*range(1, 2*n, 2), sep=", ")