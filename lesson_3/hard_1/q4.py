def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False

    while dot_separated_words:
        word = dot_separated_words.pop()
        if not 0 <= int(word) <= 255:
            return False

    return True

print(is_dot_separated_ip_address("10.4.5.1"))
