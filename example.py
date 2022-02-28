from WaifuPicsPython import Waifu
import asyncio

async def your_function():
    wafiu_pics = Waifu()
    megumin_image_url = await wafiu_pics.sfw('megumin')
    # returns 1 url as a string
    waifu_images = await wafiu_pics.sfw('waifu', many=True)
    # returns 30 urls in a list
    lewd_waifu = await wafiu_pics.nsfw('wafiu')
    # returns 1 nsfw waifu url as a string
    lewd_nekos = await wafiu_pics.nsfw('neko', many=True)
    # returns 30 nsfw neko urls in a list

asyncio.run(your_function())