class Bucket: #classe dos buckets
    def __init__(self, bucket_size): #inicia com a tamanho de registros que o bucke suporta sem overflow
        self.bucket_size = bucket_size
        self.overflow = []
        self.records = [] #vetor de registros agrupados

    def is_empty(self) -> bool: #retorna se o bucket está vazio
        return len(self.records) == 0
    
    def is_full(self) -> bool: #retorna se o bucket está cheio 
        return len(self.records) >= self.bucket_size 
    
    def not_overflow(self) -> bool: #retorna se o bucket está sem overflow
        return len(self.records) <= self.bucket_size
    