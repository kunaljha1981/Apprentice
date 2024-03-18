def gen123():
    yield 1
    yield 2
    yield 3

g=gen123()
print(g)
print(next(g))
print(next(g))

for v in gen123():
    print(v)

def take(count, iterable):
    """Take items from the front of an iterable.

    Args:
        count: The maximum number of items to retrieve.
        iterable: The source of the items.

    Yields:
        At most 'count' items from 'iterable'.
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

items = [2, 4, 6, 8, 10]
for item in take(3, items):
    print(item)


def distinct(iterable):
    """Return unique items by eliminating duplicates.

    Args:
        iterable: The source of the items.

    Yields:
        Unique elements in order from 'iterable'.
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


items = [5, 7, 7, 6, 5, 5]
for item in distinct(items):
    print(item)

items = [3, 6, 6, 2, 1, 1]
for item in take(3, distinct(items)):
    print(item)

def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


#for x in lucas(): #infinite
    #print(x)

#Generator expressions
ten_squares = (x*x for x in range(1, 11))
print(list(ten_squares))
print(list(ten_squares)) #generator objects run only once

print(sum(x*x for x in range(1, 10000001)))

print(sum(x*x for x in range(1, 10000001) if x % 2 == 0))