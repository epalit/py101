def display_msg(msg):
    print(f"==> {msg}")

def get_number(position):
    return float(input(f"==> Enter the {position} number: "))

def arithmetic():
    num1 = get_number('first')
    num2 = get_number('second')

    display_msg(f"{num1} + {num2} = {num1 + num2}")
    display_msg(f"{num1} - {num2} = {num1 - num2}")
    display_msg(f"{num1} * {num2} = {num1 * num2}")
    display_msg(f"{num1} / {num2} = {num1 / num2}")
    display_msg(f"{num1} // {num2} = {num1 // num2}")
    display_msg(f"{num1} % {num2} = {num1 % num2}")
    display_msg(f"{num1} ** {num2} = {num1 ** num2}")

arithmetic()
