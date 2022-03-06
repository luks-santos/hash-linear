from Bucket import Bucket
from sys import getsizeof

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
        vet_ = [1] * qty_fields 
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
            if self.buckets[pos].there_is_key(key): 
                return  #Não insere se já existir chave igual
               
            self.buckets.append(Bucket(self.bucket_size)) #cria novo bucket
            self.split_bucket(self.next) #faz o split no bucket apontado por próximo
            pos = self.h_level(key, self.level + 1) #calcula nova pos h(level + 1 )
            self.buckets[pos].records.append(record) #insere novo registro na posição correta
            self.next += 1 
            self.new_round() #verifica se next ultrapassou bucket do h(level)
            return

        elif pos < self.next: #verifica se bucket a receber a chave ja sofreu split
            pos = self.h_level(key, self.level + 1) #recalcula posição

        if not self.buckets[pos].is_full(): #verifica se buckets não se encontra cheio
            if self.buckets[pos].there_is_key(key):
                return #Não insere se já existir chave igual
            self.buckets[pos].records.append(record) #caso contrario apenas insere

        elif self.buckets[pos].is_full(): #verifica se bucket se encontra cheio
            if self.buckets[pos].there_is_key(key):
                return #Não insere se já existir chave igual

            self.buckets[pos].records.append(record)#adiciono registro no bucket
            self.buckets[pos].overflow = True #marco overflow
            self.buckets.append(Bucket(self.bucket_size)) #insere novo bucket
            self.split_bucket(self.next) #faz split com o bucket apontado por next
            self.next += 1 #atualiza next
            self.new_round() #verifica se next ultrapassou bucket do h(level)
                
    def split_bucket(self, current_pos): #Mando a posição do bucket que encheu e o record
        i = 0
        while i < len(self.buckets[current_pos].records): #pecorre todos registros do vetor
            record = self.buckets[current_pos].records[i] 
            pos = self.h_level(record[0], self.level + 1) #pega a nova posição do registro usando h(level + 1)
            if pos != current_pos: #se a posição do registro mudou, excluiu na posição antiga adiciona na posição nova
                self.buckets[pos].records.append(self.buckets[current_pos].records.pop(i)) 
                #obs não é encessario atualizar o i quando se deleta pois ja decrementa uma posição 
            else:
                i += 1 #caso contrário apenas atualiza o i
        if self.buckets[current_pos].not_overflow(): #verifica se não possui overflow
            self.buckets[current_pos].overflow = False

    def search(self, key): #busca um registro pela chave
        pos = self.h_level(key, self.level) #calcula possivel posição do registro
        if pos < self.next: #verifica se registro esta nos bucket h(level)
            pos = self.h_level(key, self.level + 1) #recalcula pos para h(level + 1)

        for i, record in enumerate(self.buckets[pos].records):
            if key == record[0]: #arrumar k para k[0]
                return i, self.buckets[pos]

        return None, None #retorna nuo se não encontrar o registro
    
    def delete(self, key):
        i, bucket = self.search(key) #busca o registro pela chave
        if bucket: #se encontrou o registro deleta
            bucket.records.pop(i)
            if bucket.not_overflow(): #verifica existencia de overflow
                bucket.overflow = False
    
    def print_hash(self): 
        for i in range(len(self.buckets)):
            if self.buckets[i].overflow:
                print(self.buckets[i].records, end=' -> overflow\n')
            else:
                print(self.buckets[i].records)
            