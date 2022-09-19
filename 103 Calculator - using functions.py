#Calculator
#ADD
def add(n1, n2):
    return n1 + n2
#SUBTRACT
def subtract(n1, n2):
    return n1 - n2
#MULTIPLY
def multiply(n1, n2):
    return n1 * n2
#DIVIDE
def divide(n1, n2):
    return n1 / n2

# + - * / are the KEYS and add, sub, mul and div functions are the VALUES
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("Whats the first number?: ")) #the input we will pass through the function
num2 = int(input("Whats the second number?: ")) #the input we will pass through the function

for symbol in operations: #For + - * / in the dictionary operations:
    print(symbol) #prints: + - * / 
operation_symbol = input("Pick an operation from the line above: ") #selects a symbol from + - * / 

calculation_function = operations[operation_symbol] #if "+" is selected
# calculation_function = operations["+"]
# calculation_function = add
answer = calculation_function(num1, num2)
# answer = add(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")