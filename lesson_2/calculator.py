import json

def load_messages(language):
    with open('calculator_messages.json', 'r') as file:
        return json.load(file)[language]

def build_prompt(message, inc_newline=True):
    prompt = f'-> {message}'
    if inc_newline:
        prompt = prompt + '\n'
    return prompt

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def get_lang():
    language = input(build_prompt("Select language from: [en]"))
    while language not in ["en", ""]:
        language = input(
            build_prompt("Select language from: [en]")
        )
    return language or 'en'

def get_number(prompt_text):
    number = input(build_prompt(prompt_text))

    while invalid_number(number):
        number = input(
            build_prompt(MESSAGES["invalid_number"])
        )
    return number

def get_operation():
    operation = input(
        build_prompt(MESSAGES["what_operation"])
    )

    while operation not in ["1", "2", "3", "4"]:
        operation = input(
            build_prompt(MESSAGES["invalid_operation"])
        )
    return operation

def welcome():
    print(build_prompt(MESSAGES['welcome'], inc_newline=False))

def get_calculation_input():
    number1 = get_number(MESSAGES["first_number"])
    number2 = get_number(MESSAGES["second_number"])
    operation = get_operation()
    return (number1, number2, operation)

def do_calculation(number1, number2, operation):
    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            if float(number2) == 0.0:
                output = MESSAGES['division_by_zero']
            else:
                output = float(number1) / float(number2)
    return output

def display_calculation_result(output):
    msg = MESSAGES["calculation_result"].format(output=output)
    print(build_prompt(msg, inc_newline=False))

def check_do_another():
    response = input(
        build_prompt(MESSAGES["do_another_calculation"])
    )
    return bool(response) and response[0].lower() == 'y'

def run_calculator():
    welcome()
    do_another_calculation = True
    while do_another_calculation:
        (number1, number2, operation) = get_calculation_input()
        output = do_calculation(number1, number2, operation)
        display_calculation_result(output)
        do_another_calculation = check_do_another()

lang = get_lang()
MESSAGES = load_messages(lang)
run_calculator()