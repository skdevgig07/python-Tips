from concurrent.futures import ThreadPoolExecutor
import time
import random

# ACTION#1
def soma(a, b):
    return a + b

# ACTION#2
def subtracao(a, b):
    return a - b

# ACTOR
class Mathematician:
    def __init__(self, msg = None):
        with ThreadPoolExecutor(max_workers=8) as executor:
            actions = (':soma', ':subtracao')

            b_soma = { }

            future = { }
            for _ in range(1000):
                r = random.choice(range(20,30))
                s = random.choice(range(20,100))
                future.update({(':soma', r, s): executor.submit(soma, r, s, b_soma)})

            [print(f'{k} => {v.result()}') for k, v in future.items()]
            print(len(b_soma))
                # future = executor.map(teste, range(35))


start = time.time()
Mathematician()
end = time.time()
print(end - start)
