from Bucket import Bucket
from sys import getsizeof, maxsize

class HashLinear:
    def __init__(self, qty_buckets, len_page, qty_fields): #recebe a quantidade de buckets iniciais n0, tamanho da página e campos
        self.qty_buckets_n0 = qty_buckets
        self.bucket_size = self.__bucket_size(len_page, qty_fields)
        self.buckets = [] #vetor de buckets
        self.level = 0 #nivel do hash
        self.next = 0 #proximo bucket a sofrer divisão

        for _ in range(qty_buckets): #cria a quantidade de cuket n0 vazio
            self.buckets.append(Bucket(self.bucket_size))

    def __bucket_size(self, len_page, qty_fields): # retorna a tamanho de registros do bucket de acordo com tamanho da página
        vet_ = [maxsize] * qty_fields 
        print(len_page//getsizeof(vet_))
        return len_page//getsizeof(vet_) 

    def current_buckets(self) -> int: #retorna a quantidade de buckets de acordo com nível da arvore e buckets iniciais
        return (self.qty_buckets_n0 * 2**(self.level))

    def h_level(self, key, level) -> int: #retorna o local/posição que o registro ficara, de acordo com a rodada e level 
        if self.level == level:
            return key % self.current_buckets()
        elif level == self.level + 1:
            return key % (2 * self.current_buckets())

    def new_round(self): #inicia um novo round, aumentando level da arvore e iniciando next do 0
        if self.next == self.current_buckets():
            self.level += 1
            self.next = 0

    def insert(self, key, record):
        pos = self.h_level(key, self.level) #calcula a posição que o registro pode ser inserido
        if pos == self.next and self.buckets[pos].is_full(): # verifica se o local que o cuket será inserido, sofrerá divisão
   
            self.buckets.append(Bucket(self.bucket_size)) #cria novo bucket
            self.split_bucket(self.buckets[self.next], self.next, 0) #faz o split no bucket apontado por próximo
            #pos = self.h_level(key, self.level + 1)
            self.insert(key, record)
            return

        elif pos < self.next: #verifica se bucket a receber a chave ja sofreu split
            pos = self.h_level(key, self.level + 1) #recalcula posição

        if not self.buckets[pos].is_full(): #verifica se buckets não se encontra cheio
            self.buckets[pos].records.append(record) #caso contrario apenas insere

        elif self.buckets[pos].is_full(): #verifica se bucket se encontra cheio
            print('NEXT: ', self.next)
            if not len(self.buckets[pos].overflow):
                over = Bucket(self.bucket_size)
                over.records.append(record)
                self.buckets[pos].overflow.append(over)

            else:
                flag = False
                for i, b in enumerate(self.buckets[pos].overflow):
                    if not b.is_full(): 
                        b.records.append(record)
                        flag = True
                        break
                    
                if not flag:
                    over = Bucket(self.bucket_size)
                    over.records.append(record)
                    self.buckets[pos].overflow.append(over)
            
            self.buckets.append(Bucket(self.bucket_size)) #insere novo bucket
            self.split_bucket(self.buckets[self.next], self.next, 0) #faz split com o bucket apontado por next
            self.next += 1 #atualiza next
            self.new_round() #verifica se next ultrapassou bucket do h(level)
                
    def split_bucket(self, bucket, current_pos, k): #Mando a posição do bucket que encheu e o record
        i = 0
        while i < len(bucket.records): #pecorre todos registros do vetor
            record =  bucket.records[i] 
            pos = self.h_level(record[0], self.level + 1) #pega a nova posição do registro usando h(level + 1)
            if pos != current_pos: #se a posição do registro mudou, excluiu na posição antiga adiciona na posição nova
                self.buckets[pos].records.append(bucket.records.pop(i)) 
                #obs não é encessario atualizar o i quando se deleta pois ja decrementa uma posição 
            else:
                i += 1 #caso contrário apenas atualiza o i
        if len(bucket.overflow):
            return self.split_bucket(bucket.overflow[k], current_pos, k+1)

    def search(self, key): #busca um registro pela chave
        pos = self.h_level(key, self.level) #calcula possivel posição do registro
        if pos < self.next: #verifica se registro esta nos bucket h(level)
            pos = self.h_level(key, self.level + 1) #recalcula pos para h(level + 1)

        for i, record in enumerate(self.buckets[pos].records):
            if key == record[0]: #arrumar k para k[0]
                return i, self.buckets[pos]

        if len(self.buckets[pos].overflow):
            for b in self.buckets[pos].overflow:
                for j, record in enumerate(b.records):
                     if key == record[0]:
                       return j, b

        return None, None #retorna nuo se não encontrar o registro
    
    def delete(self, key):
        i, bucket = self.search(key) #busca o registro pela chave
        if bucket: #se encontrou o registro deleta
            bucket.records.pop(i)
          
    
    def print_hash(self): 
        for i in range(len(self.buckets)):
            if len(self.buckets[i].overflow):
                print(i ,' - ',self.buckets[i].records, end=' -> ')
                for b in self.buckets[i].overflow:
                     print(b.records, end=' -> ')

                print()
            else:
                print(i ,' - ', self.buckets[i].records)
            