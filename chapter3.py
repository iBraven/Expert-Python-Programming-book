# ----Mutable and immutable----
# strings(str) and byte are immutable
# bytearray is mutable

string = 'string'  # define a string variable
print(string, type(string))  # print a string an its type

byte = b'string'  # define a byte type variable
print(byte, type(byte))  # print a byte an its type

byte_arr = bytearray(b'string')  # define a bytearray type variable
print(byte_arr, type(byte_arr), end='\n\n')  # print a bytearray an its type

byte_arr[0] = 48
# string[0] = 48        Not supported
# byte[0] = 48          Not supported


# ----Encode and Decode----

encoded = string.encode()  # String to Bytes
decoded = byte.decode(encoding='UTF-8', errors='strict')  # Bytes to string
decoded_arr = byte_arr.decode(encoding='UTF-8', errors='strict')  # bytearray to string
# using % formatting
print('Default arguments for encode is: encoding="utf-8" and errors="strict" for type %s' % type(string))
print('String to bytes: {}, type: {}'.format(encoded, type(encoded)))  # using format method
print(f'Bytes to string: {decoded}, type: {type(decoded)}')  # using f formatting
print('Bytearray to string: %s, type: %s' % (decoded_arr, type(decoded_arr)), end='\n\n')  # using % formatting

# ----Concatenate strings----
text = "This is chapter 3 of Python Expert Programming"
# split string
text_words = text.split(sep=' ')

# 2 methods to concatenate strings
concatenate_join = " ".join(text_words)
csv_text = str.join(', ', text_words)
print(concatenate_join)
print(csv_text)

# + operator isn`t efficient
concatenate_operator = ''
for word in text_words:
    concatenate_operator += word
print(concatenate_operator, end='\n\n')

# ----------Containers----------
# Lists
list_words = ['This', 'is', 'chapter', '3']
print('Length of the list: {}'.format(len(list_words)))
print(f'Print an item by indexing: "{list_words[2]}" has index {list_words.index("chapter")}', end='\n\n')

# iterate trough list
for item in list_words:
    # item is the list item
    # Do something
    break

for i in range(len(list_words)):
    # i is an index
    # list_words[i] is the item
    # Do something
    break

for i, item in enumerate(list_words):
    # get index and item at the same time
    # Do something
    break

# List comprehension

print('List comprehension is used for more readability')

# No comprehension
list_no_comprehension = []
for word in list_words:
    list_no_comprehension.append(word)

# Comprehension
list_comprehension = [word for word in list_words]

# list_comprehension and list_no_comprehension are the same
print(list_no_comprehension)
print(list_comprehension, end='\n\n')

# zip, enumerate

list_a = [2 * a + 3 for a in range(5)]
list_b = [(b + 5) / 3 + 2 for b in range(5)]

for item in zip(list_a, list_b):
    print(item)
# zip(*zip(lists)) returns de initial lists
for i, item in enumerate(list_a):
    print(f'index: {i}, value: {item}')

# ----------Dictionaries----------

dict_a = {0: 'a', 1: 'b', 2: 'c'}  # this is a dict
print(f'\n\n{dict_a}, {type(dict_a)}')
# Dictionaries are made by keys and values
print(f'Keys: {dict_a.keys()}, values: {dict_a.values()}')
# add item
dict_a[3] = 'd'
print(dict_a, dict_a[0], dict_a.get(1))  # access value by key
# Dict comprehension
dict_b = {i: 2 * i + (i + 5) // 2 for i in range(10)}
print(dict_b)

# ----------Sets----------
set_a = {'a', 'b', 'c'}  # create set
set_b = set(set_a)  # copy set
frozenset_a = frozenset(set_a)

print(set_a, type(set_a), set_b, type(set_b))
print(frozenset_a, type(frozenset_a))

# methods
set_a.remove('a')  # remove item in set (if item is not in set => err)
set_a.add('d')  # add item to set
for item in ['r', 't', 'e', 'q']:
    set_a.add(item)
set_a.discard('z')  # remove item in set (no err)
set_a.pop()  # remove last element

print(f'Initial: {set_b}, after: {set_a}')

# Other containers: tuple, namedtuple, counter, enum

# -----Advanced syntax----
# ---Iterators---

list_iter = ['a', 'b', 'e', 'ce', 'dar']
# iter -> create iterator obj
iter_li = iter(list_iter)
# next -> access next item from iterator
print(next(iter_li))  # print first item from iterator
for item in iter_li:
    print(item, end='')


# create class iterator
class IterClass:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        """Return iterator"""
        # self.start = 2
        # self.stop = 12
        return self

    def __next__(self):
        """Return next item"""
        if self.start >= self.stop:
            raise StopIteration
        self.start += 1
        return 3 * self.start + 1 / 4 * self.start ** 2 - 1 / 2 * self.stop


iter_obj = IterClass(2, 12)
print('\n', next(iter_obj))
for item in iter_obj:
    print(item)
# print(next(iter_obj))             This will raise StopIteration
for item in iter_obj:
    print(item)


# ----Generators----

def golden_ratio():
    """estimate golden ratio trough fibonacci's series"""
    a, b = 1, 1
    while True:
        yield b / a
        a, b = b, a + b


gen_fib = golden_ratio()
for i in range(20):
    print(next(gen_fib), end=', ')

# Create a list with generator and list comprehension
gen_fib = golden_ratio()
list_ratio = [next(gen_fib) for _ in range(15)]
print('\n', list_ratio)


def elephant_song(num_elephants):
    for i_elephants in range(num_elephants):
        answer = (yield)
        print(f'{i_elephants} grey elephant balancing\n'
              f'step on a piece of string\nThought it was such a wonderful stunt\n'
              f'That he called for another elephant')

    answer = (yield)
    print(f'{num_elephants} grey elephants balancing\n'
          f'Step by step on a piece of string\n'
          f'All of a sudden the piece of string broke\n'
          f'And down came all the elephant folk')


sing = elephant_song(7)
next(sing)
try:
    for i in range(8):
        sing.send('-')
except:
    print('The song has finished')


# ---Decorators---
class Decorators:
    @staticmethod
    def static_method():
        print('This is a static method with decorator')

    @classmethod
    def class_method(cls):
        print('this is a class method with decorator')

    def some_static_method():
        print("this is static method without decorators")

    some_static_method = staticmethod(some_static_method)


decorator_obj = Decorators()
decorator_obj.some_static_method()  # static method without decorator
decorator_obj.class_method()  # class method with decorator
Decorators.static_method()  # static method with decorator


def greeting(name: str):
    print(f'hi {name}')


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Function name: {func.__name__}')
        func(*args, **kwargs)

    return wrapper


# syntactic sugar
@decorator
def wupp():
    print(f'how are you?')


# decorate function
greeting = decorator(greeting)
# call functions
greeting('Luciano')
wupp()

