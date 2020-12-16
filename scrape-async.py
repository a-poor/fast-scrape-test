"""
Converting basic scrape to use
multiple processes.

```
$ ipython scrape-multiprocess.py
Finished in 149.1805 seconds. * NOTE: This doesn't seem right
```
"""

import time
import json
import requests

import asyncio
import aiohttp

links_path = "test-links.json"
with open(links_path) as f:
    links = json.load(f)

async def process_url(url: str) -> int:
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as resp:
            return await resp.read()

async def scrape_pages(links: list):
    [await process_url(url) for url in links]

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    start_time = time.perf_counter()

    loop.run_until_complete(scrape_pages(links))

    end_time = time.perf_counter()
    print(f"Finished in {end_time-start_time:.4f} seconds.")
