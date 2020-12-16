"""
Converting basic scrape to use
multiple processes.

```
$ ipython scrape-multiprocess.py
Finished in 22.3361 seconds.
```
"""

import time
import json
import requests

from multiprocessing import Pool

links_path = "test-links.json"
with open(links_path) as f:
    links = json.load(f)

def get_page(url: str) -> bytes:
    """Get the data"""
    return requests.get(url).content

def process_page(data: bytes) -> int:
    """Do something simple with the data"""
    return len(data)

def process_url(url: str) -> int:
    return process_page(get_page(url))

if __name__ == "__main__":
    start_time = time.perf_counter()
    with Pool() as P:
        P.map(process_url,links)
    end_time = time.perf_counter()
    print(f"Finished in {end_time-start_time:.4f} seconds.")
