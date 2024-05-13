from decimal import Decimal
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def is_number(s):
    try:
        # Check if it's an integer
        int(s)
        return True
    except ValueError:
        try:
            # Check if it's a decimal
            float(s)
            return True
        except ValueError:
            return False

def format_num(total):
    normalized = total.normalize()
    sign, digits, exponent = normalized.as_tuple()
    if exponent > 0:
        return Decimal((sign, digits + (0,) * exponent, 0))
    else:
        return normalized

def add_num(total, num):
    for n in num:
        total += Decimal(n)
    return format_num(total)

def subtract_num(total, num):
    total = num[0]
    for n in num[1:]:
        total -= Decimal(n)
    return format_num(total)

def multiply_num(total, num):
    total = num[0]
    for n in num[1:]:
        total = total * Decimal(n)
    return format_num(total)

def divide_num(total, num):
    total = num[0]
    for n in num[1:]:
        total = total / Decimal(n)
    return format_num(total)

def print_curr(num, operation):
    print_string = ""
    for i, n in enumerate(num):
        if (i > 0):
            if (operation == 'ADD'):
                print_string += " + "
            elif (operation == 'SUBTRACT'):
                print_string += " - "
            elif (operation == 'MULTIPLY'):
                print_string += " * "
            elif (operation == 'DIVIDE'):
                print_string += " / "
        print_string += str(n)
    print(print_string)

def add_init():
    num = []
    num_input = 0
    total = Decimal(0)
    operation = 'ADD'
    while is_number(num_input):
        print_curr(num, operation)
        print("Press enter to exit")
        num_input = input("Enter number to add:")
        if is_number(num_input):
            cls()
            num.append((Decimal(num_input)))
        elif str(num_input) == '':
            if num:
                total = add_num(total, num)
                print(total)
            else:
                print("No numbers to add.")
                num_input = 0
        else:
            cls()
            print("'" + str(num_input) + "'" + " is not a valid input")
            num_input = 0

def subtract_init():
    num = []
    num_input = 0
    total = Decimal(0)
    operation = 'SUBTRACT'
    while is_number(num_input):
        print_curr(num, operation)
        print("Press enter to exit")
        num_input = input("Enter number to subtract:")
        if is_number(num_input):
            cls()
            num.append((Decimal(num_input)))
        elif str(num_input) == '':
            if num:
                total = subtract_num(total, num)
                print(total)
            if not num:
                print("No numbers to subtract.")
                num_input = 0
        else:
            cls()
            print("'" + str(num_input) + "'" + " is not a valid input")
            num_input = 0

def multiply_init():
    num = []
    num_input = 0
    total = Decimal(0)
    operation = 'MULTIPLY'
    while is_number(num_input):
        print_curr(num, operation)
        print("Press enter to exit")
        num_input = input("Enter number to multiply: ")
        if is_number(num_input):
            cls()
            num.append((Decimal(num_input)))
        elif str(num_input) == '':
            if num:
                total = multiply_num(total, num)
                print(total)
            if not num:
                print("No numbers to multiply.")
                num_input = 0
        else:
            cls()
            print("'" + str(num_input) + "'" + " is not a valid input")
            num_input = 0

def divide_init():
    num = []
    num_input = 0
    total = Decimal(0)
    operation = 'DIVIDE'
    while is_number(num_input):
        print_curr(num, operation)
        print("Press enter to exit")
        num_input = input("Enter number to divide: ")
        if is_number(num_input):
            cls()
            num.append((Decimal(num_input)))
        elif str(num_input) == '':
            if num:
                total = divide_num(total, num)
                print(total)
            if not num:
                print("No numbers to divide.")
                num_input = 0
        else:
            cls()
            print("'" + str(num_input) + "'" + " is not a valid input")
            num_input = 0

def main():
    op_input = 0
    while op_input == 0:
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Multiply")
        print("4 - Divide")
        op_input = str(input("Choose an operation (1-4): "))

        if (op_input) == '1':
            cls()
            add_init()
        elif (op_input) == '2':
            cls()
            subtract_init()
        elif (op_input) == '3':
            cls()
            multiply_init()
        elif (op_input) == '4':
            cls()
            divide_init()
        else:
            cls()
            print(str(op_input) + " is not a valid input")
            op_input = 0

if __name__ == "__main__":
    cls()
    main()