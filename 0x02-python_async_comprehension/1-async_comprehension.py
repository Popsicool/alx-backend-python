#!/usr/bin/env python3
'''
Async Comprehensions
'''


import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''
    async_comprehension
    '''
    result = []
    async for i in async_generator():
        result.append(i)
    return result