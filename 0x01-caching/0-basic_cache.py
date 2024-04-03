#!/usr/bin/python3
""" Basic Cache Doc """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ class documenation """
    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        if key:
            return self.cache_data.get(key)
        else:
            return None
