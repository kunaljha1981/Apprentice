
t = [2, 30, 456, 764, 30, 40]
for p in enumerate(t):
    print(p)

for p, v in enumerate(t):
    print(f'{p}, {v}')

print(t[-1])
print(t[1: -1])
print(t[:]) #For shallow copy
print(t.copy()) #For deep copy
print(t.index(30))
print(t.index(30))

print(t)
del t[3]
print(t)
t.remove(456)
print(t)
t.insert(1, 456)
t.insert(2, 764)
print(t)
t.extend([1, 2])
print(sorted(t))
print(reversed(t))
print(t)
t.reverse()
print(t)
t.sort(reverse=True)
print(t)

phonetic = dict(a='alfa', b='bravo', c='charlie', d='delta', e='echo', f='foxtrot')
print(phonetic)
print(phonetic.copy())

names_and_ages = [ ('Alice', 32), ('Bob', 48), ('Charlie', 28),
                     ('Daniel', 33) ]
print(dict(names_and_ages))
phonetic.update(dict(names_and_ages))
print(phonetic)

from pprint import pprint as pp
pp(phonetic)

k = {2, 4, 7}
k.add(9)
k.update([11, 13, 14])
k.remove(4)
print(k)

country_to_capital = { 'United Kingdom': 'London', 'Brazil': 'Brasília', 'Morocco': 'Rabat', 'Sweden': 'Stockholm' }
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
print(capital_to_country)

words = ["hi", "hello", "foxtrot", "hotel"]
print({ x[0]: x for x in words })
