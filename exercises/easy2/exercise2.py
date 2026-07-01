def get_name():
    return input("What is your name? ")

def greet():
    name = get_name()
    if name.endswith('!'):
        print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
    else:
        print(f"Hello {name}.")

greet()
