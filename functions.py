def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15


print(fahr_to_kelvin(25))


def first_function():
    pass


result = first_function()
print(result)


nums = [1, 3, 2, 6, 5]
odds = list(filter(lambda num: num % 2, nums))
evens = list(filter(lambda num: num % 2 == 0, nums))
print(odds)
print(evens)


def add(a, b):
    return a + b


print(add(43859, 3860))


def sub(a, b):
    return a - b
