#!/usr/bin/env python3
'''
Let's execute multiple coroutines at the same time with async
'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Let's execute multiple coroutines at the same time with async
    '''
    ran = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        ran.append(task)
    return [await r for r in asyncio.as_completed(ran)]
