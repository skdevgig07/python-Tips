from concurrent.futures import ThreadPoolExecutor
import time
import random

# ACTION#1
def soma(a, b, interno):
    if (a, b) in interno:
        print('ret')
        return interno[(a, b)]
    return a + b

# ACTION#2
def subtrai(a, b, interno):
    if (a, b) in interno:
        print('ret')
        return interno[(a, b)]
    return a - b

start = time.time()

# ACTOR
with ThreadPoolExecutor(max_workers=8) as executor:

    b_soma = { }
    b_subtracao = { }

    future = { }

    for _ in range(1000):
        r = random.choice(range(100))
        s = random.choice(range(100))
        future.update({(':soma', r, s): executor.submit(soma, r, s, b_soma)})

    [print(f'{k} => {v.result()}') for k, v in future.items()]
        # future = executor.map(teste, range(35))

end = time.time()
print(end - start)
