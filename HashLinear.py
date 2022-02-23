from operator import mod
from Bucket import Bucket

class HashLinear:
    def __init__(self, qty_buckets, bucket_size):
        self.qty_buckets_n0 = qty_buckets
        self.bucket_size = bucket_size
        self.buckets = []
        self.level = 0
        self.next = 0

        for _ in range(qty_buckets):
            self.buckets.append(Bucket(bucket_size))

    def current_buckets(self) -> int:
        return (self.qty_buckets_n0 * 2**(self.level))

    def h_level(self, key, level) -> int:
        if self.level == level:
            return key % self.current_buckets()
        elif level == self.level + 1:
            return key % (2 * self.current_buckets())

    def insert(self, key, record):
        pos = self.h_level(key, self.level)
        if pos > self.next:
            #verificar se não está cheio e não possui key igual no bucket
            self.buckets[pos].append(record) 
        
        #if pos == self.next:
    
        #elif pos < self.next:
            pos = pos = self.h_level(key, self.level + 1)