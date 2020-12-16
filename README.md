# Testing Webscraping Speedups

_by Austin Poor_

## About

I wanted to compare different methods for parallelizing the web-scraping process
using tools like asynchronous code, multiple threads, multiple processes, and
the python library [Ray distributed](https://ray.io/).

The test links I'm using to scrape, come from [Project Gutenberg](https://www.gutenberg.org/policy/robot_access.html) – there are 200 links that I've pre-scraped and saved to the file [test-links.json](./test-links.json).

## Results

| Method | Speed (seconds) |
|--------|-------|
| [Basic (benchmark)](./scrape-basic.py) | 137.8513 |
| [Multithread](./scrape-multithread.py) | 12.4605 |
| [Multiprocess](./scrape-multiprocess.py) | 22.3361 |
| [Ray](./scrape-ray.py) | 18.8434 |
| [AsyncIO](./scrape-async.py) |  |
