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


def my_functions(*args):
    print(type(args))
    for arg in args:
        print(arg)


my_functions(1, 2, 'SEI')


def dev_skills(dev_name, *args):
    dev = {'name': dev_name, 'skills': []}
    for skill in args:
        dev['skills'].append(skill)
    return dev


print(dev_skills('Booker', 'HTML', 'CSS', 'JavaScript',
      'Python', 'React', 'Express', 'MongoDB', ))


def dev_skills(dev_name, *args):
    dev = {'name': dev_name, 'skills': list(args)}
    return dev


print(dev_skills('Booker', 'HTML', 'CSS'))


def dev_skills(dev_name, **kwargs):
    dev = {'name': dev_name, 'skills': kwargs}
    return dev


print(dev_skills('Booker', HTML=5, CSS=3, JavaScript=4, React=5, Python=2))


def arg_demo(pos1, pos2, *args, **kwargs):
    print(f'Positional params: {pos1}, {pos2}')
    print('*args:')
    for arg in args:
        print(' ', arg)
    print('**kwargs:')
    for keyword, value in kwargs.items():
        print(f' {keyword}: {value}')


arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')


def get_category(points):
    if points > 900:
        return 'Gold Member'
    elif points > 800:
        return 'Silver Member'
    else:
        return 'Bronze Member'


print(get_category(950))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(add(1, 2, 3, 4, 5))
