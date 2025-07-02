# Multi-threaded Web Scraper with Rate Limiting
import requests
from concurrent.futures import ThreadPoolExecutor
import time, random
urls = [f"https://example.com/page/{i}" for i in range(1, 101)]