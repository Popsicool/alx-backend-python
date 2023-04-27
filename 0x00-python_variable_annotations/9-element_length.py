#!/usr/bin/env python3
'''
Python - Variable Annotations
'''


from typing import Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    '''
    Python - Variable Annotations
    '''
    return [(i, len(i)) for i in lst]
