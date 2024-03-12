operand_one = 0.0
operand_two = 0.0
sum = 0.0
difference = 0.0
quotient = 0.0
remainder = 0.0
product = 0.0

operand_one = float(input("enter 1st mumber:"))
operand_two = float(input("enter 2nd number:"))
sum = operand_one+operand_two
sum = round(sum, 1)
print("added together:", sum)

# operand_one = int(input("enter first number:"))
# operand_two = int(input("enter 2nd number:"))
difference = operand_one-operand_two
difference = round(difference, 1)
print("subtract together:", difference)

product = operand_one*operand_two
product = round(product, 1)
print("multiplied together:", product)

# operand_one = int(input("enter first number:"))
# operand_two = int(input("enter 2nd number:"))
quotient = operand_one//operand_two
quotient = round(quotient, 1)
print("quotient together:", quotient)

# operand_one = int(input("enter first number:"))
# operand_two = int(input("enter 2nd number:"))
remainder = operand_one%operand_two
remainder = round(remainder, 1)
print("remainder together:", remainder)
