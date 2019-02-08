#!/usr/bin/python3
# -*- coding: utf-8 -*-

import aiohttp
import asyncio
import json


async def fetch(session, url):
    async with session.get(url) as response:
        print(dir(response))

        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, "http://localhost:8080")

        r_dict = json.loads(response)

        if r_dict["status"] == "success":
            print(r_dict["endpoints"])
        else:
            print(r_dict["reason"])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
