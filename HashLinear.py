from operator import mod
from posixpath import split
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
      
        if (pos >= self.next):
            if len(self.buckets[pos].records) < (self.bucket_size):
                if key in self.buckets[pos].records:
                    print('Chave já existe!')
                    return
                self.buckets[pos].records.append(record) 
           
            elif(pos > self.next and self.buckets[pos].is_full()):
                if not key in self.buckets[pos].records:
                    self.buckets[pos].records.append(record)
                    self.buckets[pos].overflow = True
            
                self.buckets.append(Bucket(self.bucket_size))
                self.split_bucket(self.next)
                self.next += 1

            elif pos == self.next and self.buckets[pos].is_full():
                self.buckets.append(Bucket(self.bucket_size))
                self.split_bucket(self.next)
                pos = self.h_level(key, self.level + 1)
                self.buckets[pos].records.append(record)
                self.next += 1

            if self.next == self.current_buckets():
                self.level += 1
                self.next = 0

        elif pos < self.next:
            pos = self.h_level(key, self.level + 1)
            if len(self.buckets[pos].records) < self.bucket_size:
                if key in self.buckets[pos].records:
                    print('Chave já existe!')
                    return
                self.buckets[pos].records.append(record) 
            
            elif len(self.buckets[pos].records) == self.bucket_size:
                if not key in self.buckets[pos].records:
                    self.buckets[pos].records.append(record)
                    self.buckets[pos].overflow = True
            
                self.buckets.append(Bucket(self.bucket_size))
                self.split_bucket(self.next)
                self.next += 1

                if self.next == self.current_buckets():
                    self.level += 1
                    self.next = 0
                
           
    def split_bucket(self, posatual): #Mando a posição do bucket que encheu e o record
        i = 0
        while i < len(self.buckets[posatual].records):
            k = self.buckets[posatual].records[i]
            pos = self.h_level(k, self.level + 1) #mudar o k para k[0]
            if pos != posatual:
                self.buckets[pos].records.append(self.buckets[posatual].records.pop(i)) 
            else:
                i += 1
            if len(self.buckets[posatual].records) <= self.bucket_size:
                self.buckets[posatual].overflow = False

        
    def print_hash(self):
        for i in range(len(self.buckets)):
          #  if(not self.buckets[i].is_empty()):
                print(self.buckets[i].records)
                #print('bucket overflow', self.buckets[i].overflow)