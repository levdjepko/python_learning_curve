def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {}
operations["+"] = add
operations["-"] = substract
operations["*"] = multiply
operations["/"] = divide


n1 = float(input("First number: \n"))
operator = input("Operation: + - / * \n")
n2 = float(input("Second number: \n"))

result = operations[operator](n1, n2)
print(result)
# todo: add the logic to make it work inside the loop
