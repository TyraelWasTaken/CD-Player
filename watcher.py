from typing import Union
from fastapi import FastAPI
import asyncio
from subprocess import call
import json


async def main():
    await asyncio.sleep(5)
    lval = ''
    while True:
        with open('info.json', 'r+', encoding = 'utf-8') as info:
            cmi = json.load(info)
        if lval != cmi:
            print(cmi)
        lval = cmi
        await asyncio.sleep(1)

asyncio.run(main())