import time
import asyncio

async def fun1(x):
    print(x**2)
    time.sleep(3)
    print('fun1 завершена')


async def fun2(x):
    print(x**0.5)
    time.sleep(3)
    print('fun2 завершена')


async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    await task1
    await task2

print(type(fun1))

print(type(fun1(4)))