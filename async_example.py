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

import asyncio

from WaifuPicsPython import WaifuAsync

async def your_function():
    wafiu_pics = WaifuAsync()
    megumin_image_url = await wafiu_pics.sfw('megumin')
    # returns 1 url as a string
    waifu_images = await wafiu_pics.sfw('waifu', many=True)
    # returns 30 urls in a list
    random_sfw_image = await wafiu_pics.sfw('random')
    # returns 1 random sfw image
    lewd_waifu = await wafiu_pics.nsfw('waifu')
    # returns 1 nsfw waifu url as a string
    lewd_nekos = await wafiu_pics.nsfw('neko', many=True)
    # returns 30 nsfw neko urls in a list
    random_nsfw_images = await wafiu_pics.nsfw('random', many=True)
    # returns 30 random nsfw images

asyncio.run(your_function())