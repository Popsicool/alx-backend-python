#!/usr/bin/env python3
'''
Run time for four parallel comprehensions
'''


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Run time for four parallel comprehensions
    '''
    start = time.perf_counter()
    task = []
    for _ in range(4):
        task.append(async_comprehension())
    await asyncio.gather(*task)
    end = time.perf_counter() - start
    return end
