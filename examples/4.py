import random

data = [i for i in range(10_000_000)]

n = random.randint(0, 20_000_000)

print(n in data)
