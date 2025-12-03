class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower() 

    def compute(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "sub":
            return self.a - self.b
        elif self.operation == "mul":
            return self.a * self.b
        elif self.operation == "div":
            if self.b == 0:
                return "Error: Division by zero not allowed"
            return self.a / self.b
        else:
            return "Invalid operation"


a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
operation = input("Enter operation (add, sub, mul, div): ")

calc = Calculator(a, b, operation)
result = calc.compute()

print("Result:", result)