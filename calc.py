from cgi import print_form


def calculator(first, second, operator):
    while True: 
        if operator == "+":
            first + second 
            return first + second
        elif operator == "-":
            first - second
            return first - second
        elif operator == "/":
            first/second
            return first/second
        elif operator == "*":
            first*second
            return first*second
        else:
            operator = input("operator is invalid, please enter a suitable operator: ") 

        
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
operator = input("Please enter your operator: ")


print(f'The result of {first} {operator} {second} = {calculator(first, second, operator)}')



    

