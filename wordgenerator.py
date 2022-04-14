from itertools import product

from string import ascii_lowercase
keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]

p = '-_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
keywords = [''.join(i) for i in product(p, repeat = 3)]
