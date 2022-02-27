
# WaifuPicsPython

An asynchronous Python API wrapper for https://waifu.pics.


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)


### Code example
```python
from WaifuPicsPython import Waifu
import asyncio

async def your_function():
    megumin_image_url = await Waifu().sfw('megumin')
    # returns 1 url as a string
    waifu_images = await Waifu().sfw('waifu', many=True)
    # returns 30 urls in a list
    lewd_waifu = await Waifu().nsfw('wafiu')
    # returns 1 nsfw waifu url as a string
    lewd_nekos = await Waifu().nsfw('neko', many=True)
    # returns 30 nsfw neko urls in a list

asyncio.run(your_function())
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