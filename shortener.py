import hashlib

class URLShortener:
    def __init__(self):
        self.urls = {}

    def shorten(self, long_url):
        short_url = hashlib.md5(long_url.encode()).hexdigest()[:6]
        self.urls[short_url] = long_url
        return short_url

    def expand(self, short_url):
        return self.urls.get(short_url, "URL не знайдено")    
