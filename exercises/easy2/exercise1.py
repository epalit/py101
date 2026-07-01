def greetings(name, details):
    fullname = " ".join(name)
    title = details['title']
    occupation = details['occupation']

    return f'Hello, {fullname}! Nice to have a {title} {occupation} around.'
