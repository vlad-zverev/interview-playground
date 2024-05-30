import asyncio
import time


async def run_some_risky(i) -> None:
    await asyncio.sleep(1)

    if i == 5:
        raise RuntimeError()


async def main() -> None:
    await asyncio.gather(
        *[run_some_risky(i) for i in range(10)],
    )


start = time.time()

asyncio.run(main())

print(time.time() - start)
