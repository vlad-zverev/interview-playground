import asyncio
import time


async def run(i) -> None:
    await asyncio.sleep(1)

    if i == 5:
        raise RuntimeError()

    return i + 1


async def main() -> None:
    results = await asyncio.gather(
        *[run(i) for i in range(10)],
    )

    for i in results:
        print(i)


start = time.time()

asyncio.run(main())

print(time.time() - start)
