"""
MIT License

Copyright (c) 2022-present Scrumpy (Jay)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import aiohttp
from .variables import *

class Waifu:
    def __init__(self):
        pass
    
    async def _request(self, category: str, nsfw: bool=False, exclude: list=[]):
        type_parameter = 'nsfw' if nsfw else 'sfw'
        request_headers = {"exclude": exclude}
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{API_URL}/{type_parameter}/{category}', json=request_headers) as request:
                json_body = await request.json()
                return json_body

    async def _request_many(self, category: str, nsfw: bool=False, exclude: list=[]):
        type_parameter = 'nsfw' if nsfw else 'sfw'
        request_headers = {"exclude": exclude}
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{API_URL}/many/{type_parameter}/{category}', json=request_headers) as request:
                json_body = await request.json()
                return json_body

    async def sfw(self, category, many: bool=False, exclude: list=[]):
        if category.lower() not in VALID_SFW_REQUESTS: return f"Invalid SFW category, must be one of: {VALID_SFW_REQUESTS}"
        if not many: return await self._request(category=category, nsfw=False, exclude=exclude)
        else: return await self._request_many(category=category, nsfw=False, exclude=exclude)

    async def nsfw(self, category, many: bool=False, exclude: list=[]):
        if category.lower() not in VALID_NSFW_REQUESTS: return f"Invalid NSFW category, must be one of: {VALID_NSFW_REQUESTS}"
        if not many: return await self._request(category=category, nsfw=True, exclude=exclude)
        else: return await self._request_many(category=category, nsfw=True, exclude=exclude)