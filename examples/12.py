from threading import Thread
from multiprocessing import Process, freeze_support
import asyncio
import random
import time

N = 1_000_000
S = 5


def run(m: int) -> None:
    v = 0
    for i in range(1_000_000):
        v += i * random.randint(1, m)  # very important calculations


def t() -> None:
    for _ in range(S):
        t = Thread(target=run, args=(10,))
        t.start()

    start = time.time()

    t.join()

    print("t", time.time() - start)


def p() -> None:
    for _ in range(S):
        p = Process(target=run, args=(10,))
        p.start()

    start = time.time()

    p.join()

    print("p", time.time() - start)


async def a() -> None:
    async def call(m: int) -> None:
        run(m)

    start = time.time()

    await asyncio.gather(*[call(10) for _ in range(S)])

    print("a", time.time() - start)


if __name__ == "__main__":
    freeze_support()

    t()
    p()
    asyncio.run(a())
