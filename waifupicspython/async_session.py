"""
MIT License

Copyright (c) 2022-present Scrumpy

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
import random
from typing import List, Union

from ._defaults import API_URL, VALID_SFW_REQUESTS, VALID_NSFW_REQUESTS


class WaifuAsync:

    """
    Represents a way to interact with the waifu.pics API asynchronously.
    """

    def __init__(self):
        self._session = None

    @property
    def _client_session(self) -> aiohttp.ClientSession:
        """Returns the aiohttp.ClientSession() value, creating a new one if None/closed."""

        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()

        return self._session

    async def _get_data(
        self, category: str, nsfw: bool = False, exclude: list = None, data_type: str = "url"
    ) -> Union[List, str]:
        """Get data from api

        Args:
            category (str): image category (see <VALID_SFW_REQUESTS>)
            nsfw (bool, optional): if True returns nsfw. Defaults to False.
            exclude (list, optional): image urls to not receive. Defaults to None.
            data_type (str, optional): data to fetch "files" or "url". Defaults to "url".

        Returns:
            List | str: returning a list of files or url
        """

        exlude = [] if exclude == None else exclude
        json_request_headers = {"exclude": exclude}

        type_parameter = "nsfw" if nsfw else "sfw"
        session = self._client_session

        # Many requires a post instead of get
        async with session.post(f"{API_URL}/many/{type_parameter}/{category}", json=json_request_headers) as request:
            request.raise_for_status()  # Raising an aiohttp error if status code not 2xx
            json_body = await request.json()
            return json_body[data_type]

    async def _request_one(self, category: str, nsfw: bool = False, exclude: list = None) -> str:
        """Returns the data from the WaifuPics API (when many=False)."""

        return self._get_data(category, nsfw, exclude, data_type="url")

    async def _request_many(self, category: str, nsfw: bool = False, exclude: list = None) -> list:
        """Returns the data from the WaifuPics API (when many=True)."""

        return self._get_data(category, nsfw, exclude, data_type="files")

    async def _get_image_url(self, category: str, many: bool = False, exclude: list = None, nsfw: bool = False) -> str:
        """Get image url

        Args:
            category (str): image category (see <VALID_SFW_REQUESTS>)
            many (bool, optional): if True returns many urls (↓30). Defaults to False.
            exclude (list, optional): image urls to not receive. Defaults to None.
            nsfw (bool, optional): if True returns nsfw. Defaults to False.

        Raises:
            ValueError: raises when category is invalid (see <VALID_SFW_REQUESTS>)

        Returns:
            str: image url
        """

        VALID_REQUESTS = VALID_NSFW_REQUESTS if nsfw else VALID_SFW_REQUESTS

        if category.lower() not in VALID_REQUESTS:
            raise ValueError(f"Invalid SFW category, must be one of: {VALID_REQUESTS}")

        if category.lower() == "random":
            category = random.choice(VALID_REQUESTS)

        if many:
            return await self._request_many(category=category, nsfw=False, exclude=exclude)

        return await self._request_one(category=category, nsfw=False, exclude=exclude)

    async def sfw(self, category: str, many: bool = False, exclude: list = None) -> Union[str, list]:
        """Request a SFW image from the waifu.pics API.

        Args:
            category (:obj:`str`): What category of image do you want to request.
            many (:obj:`bool`, optional): Do you want to recieve 30 images instead of one?
            exclude (:obj:`list`, optional): Image URLs to NOT recieve from the API.

        Returns:
            str: An image URL of the requested type.
        """

        return await self._get_image_url(category, many, exclude, nsfw=False)

    async def nsfw(self, category: str, many: bool = False, exclude: list = None) -> Union[str, list]:
        """Request a NSFW image from the waifu.pics API.

        Args:
            category (:obj:`str`): What category of image do you want to request.
            many (:obj:`bool`, optional): Do you want to recieve 30 images instead of one?
            exclude (:obj:`list`, optional): Image URLs to NOT recieve from the API.

        Returns:
            str: An image URL of the requested type.
        """

        return await self._get_image_url(category, many, exclude, nsfw=True)
