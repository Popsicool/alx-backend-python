#!/usr/bin/env python3
'''
Python - Variable Annotations
'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Python - Variable Annotations
    '''
    return tuple([k, (v * v)])
