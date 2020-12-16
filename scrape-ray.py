"""
Converting basic scrape to use
the ``ray`` library.

```
$ ipython scrape-ray.py
Finished in 18.8434 seconds.
```
"""

import time
import json
import requests

import ray

links_path = "test-links.json"
with open(links_path) as f:
    links = json.load(f)

@ray.remote
def get_page(url: str) -> bytes:
    """Get the data"""
    return requests.get(url).content

@ray.remote
def process_page(data: bytes) -> int:
    """Do something simple with the data"""
    return len(data)

ray.init()

if __name__ == "__main__":
    start_time = time.perf_counter()

    responses = [get_page.remote(url) for url in links]
    data = [process_page.remote(p) for p in responses]
    ray.get(data)

    end_time = time.perf_counter()
    print(f"Finished in {end_time-start_time:.4f} seconds.")
