# Multi-threaded Web Scraper with Rate Limiting
import requests
from concurrent.futures import ThreadPoolExecutor
import time, random
urls = [f"https://example.com/page/{i}" for i in range(1, 101)]
def fetch(url):
    time.sleep(random.uniform(0.5, 2))  # Rate limiting
    try:
        response = requests.get(url, timeout=10)
        print(f"{url}: {response.status_code}")
    except requests.RequestException as e:
        print(f"Failed: {url}, {e}")

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(fetch, urls)