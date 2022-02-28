from Bucket import Bucket
from sys import getsizeof
class HashLinear:
    def __init__(self, qty_buckets, len_page, qty_fields):
        self.qty_buckets_n0 = qty_buckets
        self.bucket_size = self.__bucket_size(len_page, qty_fields)
        self.buckets = []
        self.level = 0
        self.next = 0

        for _ in range(qty_buckets):
            self.buckets.append(Bucket(self.bucket_size))

    def __bucket_size(self, len_page, qty_fields):
        vet_ = [1] * qty_fields 
        return len_page//getsizeof(vet_) 

    def current_buckets(self) -> int:
        return (self.qty_buckets_n0 * 2**(self.level))

    def h_level(self, key, level) -> int:
        if self.level == level:
            return key % self.current_buckets()
        elif level == self.level + 1:
            return key % (2 * self.current_buckets())

    def new_round(self):
        if self.next == self.current_buckets():
            self.level += 1
            self.next = 0

    def insert(self, key, record):
        pos = self.h_level(key, self.level)
        if pos == self.next and self.buckets[pos].is_full():
            for rec in self.buckets[pos].records:
                if key == rec[0]:
                    return
            self.buckets.append(Bucket(self.bucket_size))
            self.split_bucket(self.next)
            pos = self.h_level(key, self.level + 1)
            self.buckets[pos].records.append(record)
            self.next += 1
            self.new_round()
            return

        elif pos < self.next:
            pos = self.h_level(key, self.level + 1)

        if not self.buckets[pos].is_full():
            for rec in self.buckets[pos].records:
                if key == rec[0]:
                    return
            self.buckets[pos].records.append(record) 

        elif self.buckets[pos].is_full():
            for rec in self.buckets[pos].records:
                if key == rec[0]:
                    return
            self.buckets[pos].records.append(record)
            self.buckets[pos].overflow = True
            self.buckets.append(Bucket(self.bucket_size))
            self.split_bucket(self.next)
            self.next += 1
            self.new_round()
                
    def split_bucket(self, current_pos): #Mando a posição do bucket que encheu e o record
        i = 0
        while i < len(self.buckets[current_pos].records):
            record = self.buckets[current_pos].records[i]
            pos = self.h_level(record[0], self.level + 1) #mudar o k para k[0]
            if pos != current_pos:
                self.buckets[pos].records.append(self.buckets[current_pos].records.pop(i)) 
            else:
                i += 1
        if self.buckets[current_pos].not_overflow():
            self.buckets[current_pos].overflow = False

    def search(self, key):
        pos = self.h_level(key, self.level)
        if pos < self.next:
            pos = self.h_level(key, self.level + 1)

        for i, record in enumerate(self.buckets[pos].records):
            if key == record[0]: #arrumar k para k[0]
                return i, self.buckets[pos]

        return None, None
    
    def delete(self, key):
        i, bucket = self.search(key)
        if bucket:
            bucket.records.pop(i)
            if bucket.not_overflow():
                bucket.overflow = False
    
    def print_hash(self):
        for i in range(len(self.buckets)):
            if self.buckets[i].overflow:
                print(self.buckets[i].records, end=' -> overflow\n')
            else:
                print(self.buckets[i].records)