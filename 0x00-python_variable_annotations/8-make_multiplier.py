#!/usr/bin/env python3
'''
Python - Variable Annotations
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Python - Variable Annotations
    '''
    def mul(a: float) -> float:
        return (a * multiplier)
    return mul
