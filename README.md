# WaifuPicsPython

An asynchronous & synchronous Python API wrapper for https://waifu.pics.


`pip install WaifuPicsPython`


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)


### Asynchronous Code Example
```python
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
```

### Synchronous Code Example
```python
from WaifuPicsPython import WaifuSync

def your_function():
    wafiu_pics = WaifuSync()
    megumin_image_url = wafiu_pics.sfw('megumin')
    # returns 1 url as a string
    waifu_images = wafiu_pics.sfw('waifu', many=True)
    # returns 30 urls in a list
    random_sfw_image = wafiu_pics.sfw('random')
    # returns 1 random sfw image
    lewd_waifu = wafiu_pics.nsfw('waifu')
    # returns 1 nsfw waifu url as a string
    lewd_nekos = wafiu_pics.nsfw('neko', many=True)
    # returns 30 nsfw neko urls in a list
    random_nsfw_images = wafiu_pics.nsfw('random', many=True)
    # returns 30 random nsfw images

your_function()
```

## Categories List

### SFW
```
  'waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 
  'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 
  'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 
  'nom', 'bite', 'glomp', 'slap', 'kill', 'kick', 'happy', 
  'wink', 'poke', 'dance', 'cringe'
```

### NSFW
```
  'waifu', 'neko', 'trap', 'blowjob'
```
