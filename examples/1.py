import asyncio
import time

semaphore = asyncio.Semaphore(10)


async def main() -> None:
    for _ in range(20):
        async with semaphore:
            await asyncio.sleep(0.1)


start = time.time()

asyncio.run(main())

print(time.time() - start)
