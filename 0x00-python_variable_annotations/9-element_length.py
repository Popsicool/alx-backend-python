#!/usr/bin/env python3
'''
Python - Variable Annotations
'''


from typing import Tuple, List, Sequence


def element_length(lst: List[Sequence]) -> Tuple[Sequence, int]:
    '''
    Python - Variable Annotations
    '''
    return [(i, len(i)) for i in lst]
