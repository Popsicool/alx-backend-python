#!/usr/bin/env python3
'''
Python - Variable Annotations
'''


from typing import Mapping, TypeVar, Any, Union, Optional


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    '''
    Python - Variable Annotations
    '''
    if key in dct:
        return dct[key]
    else:
        return default
