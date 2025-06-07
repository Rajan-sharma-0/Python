# Q : Make a claculater

print("Welcome to my calculater")

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
operater = input("Select the operater (+, -, *, /): ")



if operater == "+":
    result = n1 + n2
    print(result)
elif operater == '-':
    result = n1 - n2
    print(result)
elif operater == '*':
    result = n1 * n2
    print(result)
elif operater == '/':
    result = n1 / n2
    print(result)

