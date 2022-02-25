# -*- coding: utf-8 -*-

class Bucket:#classe dos buckets
    def __init__(self, bucket_size):
        self.bucket_size = bucket_size
        self.overflow = False
        self.records = []#valores

    def is_empty(self) -> bool:
        return len(self.records) == 0
    
    def is_full(self) -> bool:
        return len(self.records) >= self.bucket_size 