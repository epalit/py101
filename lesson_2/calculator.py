def build_prompt(message, inc_newline=True):
    prompt = f'-> {message}'
    if inc_newline is True:
        prompt = prompt + '\n'
    return prompt

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def get_number():
    number = input(build_prompt("What's the first number?"))

    while invalid_number(number):
        number = input(
            build_prompt("Hmm... that doesn't look like a valid number.")
        )
    return number

def get_operation():
    operation = input(
        build_prompt("""What operation would you like to perform?
    1) Add 2) Subtract 3) Multiply 4) Divide""")
    )

    while operation not in ["1", "2", "3", "4"]:
        operation = input(
            build_prompt('You must choose 1, 2, 3, or 4')
        )
    return operation

def welcome():
    print(build_prompt("Welcome to Calculator!", inc_newline=False))

def get_calculation_input():
    number1 = get_number()
    number2 = get_number()
    operation = get_operation()
    return (number1, number2, operation)

def do_calculation(number1, number2, operation):
    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)
    return output

def display_calculation_result(output):
    print(build_prompt(f"The result is: {output}", inc_newline=False))

def check_do_another():
    response = input(
        build_prompt("Would you like to do another calculation? (Yes or No)")
    )
    while response not in ["Yes","No"]:
        response = input(
            build_prompt('You must choose Yes or No')
        )
    return True if response == 'Yes' else False

def run_calculator():
    welcome()
    do_another_calculation = True
    while do_another_calculation:
        (number1, number2, operation) = get_calculation_input()
        output = do_calculation(number1, number2, operation)
        display_calculation_result(output)
        do_another_calculation = check_do_another()

run_calculator()