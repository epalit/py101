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

print(build_prompt("Welcome to Calculator!", inc_newline=False))

number1 = input(build_prompt("What's the first number?"))

while invalid_number(number1):
    number1 = input(
        build_prompt("Hmm... that doesn't look like a valid number.")
    )

number2 = input(build_prompt("What's the second number?"))

while invalid_number(number2):
    number2 = input(
        build_prompt("Hmm... that doesn't look like a valid number.")
    )

operation = input(
    build_prompt("""What operation would you like to perform?
1) Add 2) Subtract 3) Multiply 4) Divide""")
)

while operation not in ["1", "2", "3", "4"]:
    operation = input(
        build_prompt('You must choose 1, 2, 3, or 4')
    )

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

print(build_prompt(f"The result is: {output}", inc_newline=False))
