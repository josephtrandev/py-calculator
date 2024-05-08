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

def sub_num(total, num):
    total = num[0]
    for n in num[1:]:
        total -= Decimal(n)
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

def sub_init():
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
                total = sub_num(total, num)
                print(total)
            if not num:
                print("No numbers to subtract.")
                num_input = 0
        else:
            cls()
            print("'" + str(num_input) + "'" + " is not a valid input")
            num_input = 0

op_input = 0
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
op_input = input("Choose an operation (1-3): ")

if int(op_input) == 1:
    cls()
    add_init()
elif int(op_input) == 2:
    cls()
    sub_init()