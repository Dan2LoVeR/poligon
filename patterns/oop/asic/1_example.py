import asyncio
import time

async def fun1(x):
    print(f'fun1: {x**2}')
    await asyncio.sleep(3)
    print('fun1 done')

async def fun2(x):
    print(f'fun2: {x**0.5}')
    await asyncio.sleep(3)
    print('fun2 done')

async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    await task1
    await task2

print('Start:', time.strftime('%X'))
asyncio.run(main())
print('End:', time.strftime('%X'))