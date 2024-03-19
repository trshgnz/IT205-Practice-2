num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the limit:"))


t = [q for q in range(num3) if q % num1 == 0 or q  % num2 == 0]
q = sum(t)

print (f"The sum of multiples of {num1} or {num2} up to {num3} is {q}.")