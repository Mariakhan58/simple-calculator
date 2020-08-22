# Program to make a simple calculator

# This function adds two numbers
def Calculate():

    def add(a, b):
        return a+b

    # This function subtracts two numbers
    def subt(a, b):
        return a-b

    # This function multiplies two numbers
    def mult(a, b):
        return a*b

    #This function divides two numbers
    def div(a, b):
        return a/b

    print('Operations this calculator can perform:')
    print('a. Addition')
    print('b. Subtraction')
    print('c. Multiplication')
    print('d. Division')

    while True:
        operation = input('\nEnter the option for the operation you want to perform (a/b/c/d): ')
        if operation in ('a','b','c','d'):
            number1 = float(input('Enter first number: '))
            number2 = float(input('Enter second number: '))

            if operation == 'a':
                print(number1, ' + ', number2, ' = ', add(number1, number2))

            if operation == 'b':
                print(number1, ' - ', number2, ' = ', subt(number1, number2))

            if operation == 'c':
                print(number1, ' * ', number2, ' = ', mult(number1, number2))

            if operation == 'd':
                print(number1, ' / ', number2, ' = ', div(number1, number2))
            break

        else:
            print("Invalid choice")

Calculate()




