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

print('Start:', time.strftime('%X'))

loop = asyncio.get_event_loop()
task1 = loop.create_task(fun1(4))
task2 = loop.create_task(fun2(4))

loop.run_until_complete(asyncio.wait([task1, task2]))
print('End:', time.strftime('%X'))