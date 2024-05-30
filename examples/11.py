import asyncio
import time


event = asyncio.Event()


def create() -> None:
    asyncio.create_task(wait())


async def wait() -> None:
    await asyncio.sleep(1)
    event.set()


async def main() -> None:
    create()
    await event.wait()


start = time.time()

asyncio.run(main())

print(time.time() - start)
