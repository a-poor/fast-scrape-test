"""
Simple, synchronous scrape of 200 urls
using requests library.

```
$ ipython scrape-basic.py
Finished in 137.8513 seconds.
```
"""

import time
import json
import requests

links_path = "test-links.json"
with open(links_path) as f:
    links = json.load(f)

def get_page(url: str) -> bytes:
    """Get the data"""
    return requests.get(url).content

def process_page(data: bytes) -> int:
    """Do something simple with the data"""
    return len(data)

if __name__ == "__main__":
    start_time = time.perf_counter()
    for url in links:
        p = get_page(url)
        process_page(p)
    end_time = time.perf_counter()
    print(f"Finished in {end_time-start_time:.4f} seconds.")
