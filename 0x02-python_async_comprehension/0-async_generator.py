#!/usr/bin/env python3
'''Async Generator Module.
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates a sequence of 10 nums.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
