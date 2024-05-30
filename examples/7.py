import asyncio
import time


async def wait() -> None:
    await asyncio.sleep(1)
    print('done')


async def main() -> None:
    asyncio.create_task(wait())


start = time.time()

asyncio.run(main())

print(time.time() - start)
