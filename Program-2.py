a = int(input("Enter a value: "))

for i in range(a):
    if i == a - 1:
        print(2*i + 1)        
    else:
        print(2*i + 1, end=", ")
