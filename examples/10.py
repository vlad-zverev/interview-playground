import asyncio
import time

semaphore = asyncio.Semaphore(10)


async def do() -> None:
    async with semaphore:
        await asyncio.sleep(0.1)


async def main() -> None:
    await asyncio.gather(
        *[do() for _ in range(100)],
    )


start = time.time()

asyncio.run(main())

print(time.time() - start)
