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
        if (pos >= self.next and len(self.buckets[pos].records) < self.bucket_size):
            #verificar se não está cheio e não possui key igual no bucket
            self.buckets[pos].records.append(record) 
        
        #if pos == self.next:
            #verificar se é necessário essa condição
    
        elif pos < self.next:
            pos  = self.h_level(key, self.level + 1)
        
        elif(pos >= self.next and len(self.buckets[pos].records) == self.bucket_size):
            print("Encheu o bucket")
            print("proximo: ",self.next)
            self.next += 1
            print("posicao: ",self.next)
            print("proximo: ",self.next)
            self.buckets.append(Bucket(self.bucket_size))
            #implementar a divisão de buckets
            self.split_bucket(pos, record)


    def split_bucket(self, posatual,record): #Mando a posição do bucket que encheu e o record
        for i in range(self.bucket_size):
            print("i: ",i)
            print("key: ",self.buckets[posatual].records[i])
            print("mod: ", self.h_level(self.buckets[posatual].records[i],self.level+1))
            pos = self.h_level(self.buckets[posatual].records[i],self.level+1)
            
            self.buckets[pos].records.append(self.buckets[posatual].records[i]) 

            if(self.h_level(self.buckets[posatual].records[i],self.level+1) != posatual):
                #criar um vetor para receber as posições dos que serão incluidos no ultimo bucket, para remover do que estavam 
                print(i)
            print("ok")
        #self.buckets[novaposicao].append(record) 
        

    def print_hash(self):
        for i in range(len(self.buckets)):
            if(not self.buckets[i].is_empty()):
                print(self.buckets[i].records)