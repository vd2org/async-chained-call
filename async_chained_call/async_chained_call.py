# Copyright (C) 2022 by Vd.
#
# This file is part of AsyncChainedCallWrapper, a small library that allows you to make chained calls of asynchronous
# functions.
#
# AsyncChainCall is released under the MIT License (see LICENSE).


from functools import wraps
from inspect import isawaitable
from typing import Type, Callable, Tuple, Dict


class AsyncChainedCallWrapper:
    __WRAPPER_ATTR = "__ASYNC_CHAINED_CALL_WRAPPER__"

    def __init__(self, obj: Type, func: Callable, args: Tuple, kwargs: Dict):
        self.__obj = obj
        self.__func = func
        self.__args = args
        self.__kwargs = kwargs
        self.__nested = None
        self.__is_awaited = False

    def __await__(self):
        if self.__is_awaited:
            raise RuntimeError("cannot reuse already awaited coroutine")

        self.__is_awaited = True

        async def call():
            if self.__nested:
                await self.__nested

            res = self.__func(*self.__args, **self.__kwargs)
            res = await res if isawaitable(res) else res

            if res is not None and res != self.__obj:
                raise ValueError(f'Chained methods must return self or None: {self.__func}')

        return call().__await__()

    def __getattr__(self, attr: str):
        f = getattr(self.__obj, attr)

        if not hasattr(f, self.__WRAPPER_ATTR):
            raise AttributeError(f'Unsupported chained call! You must wrap this method too: {f}')

        @wraps(f)
        def inner(*args, **kwargs):
            wrapper = f(*args, **kwargs)
            wrapper.__set_nested_wrapper(self)
            return wrapper

        return inner

    def __set_nested_wrapper(self, nested: bool):
        if self.__nested:
            raise ValueError('Nested cannot be set twice!')

        self.__nested = nested

    def __del__(self):
        if not self.__is_awaited:
            raise RuntimeWarning(f"coroutine '{self.__func}' was never awaited!")

    @classmethod
    def wrap(cls, f: Callable):
        @wraps(f)
        def inner(*args, **kwargs):
            return cls(args[0], f, args, kwargs)

        setattr(inner, cls.__WRAPPER_ATTR, True)

        return inner
