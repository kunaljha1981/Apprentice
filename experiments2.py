a = 500
b = 1000
print(id(a))
print(id(b))
print(a is b)
a = b
print(id(a))
print(id(b))
print(a is b)
print(id(None))


def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner('Hello')
banner('Hello', '*')


def add_spam(menu=[]):
    menu.append("spam")
    return menu


print(add_spam())
print(add_spam())
print(add_spam())
