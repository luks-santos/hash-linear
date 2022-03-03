from HashLinear import HashLinear
import time

def main():
    n = int(input('Digite a quantidade de buckets inicial n0: '))
    len_page = int(input('Digite o tamanho da página em bytes: '))
    qty_fields = int(input('Digite a quantidade de campos do registro: '))
    hash = HashLinear(n, len_page, qty_fields)
 
    while(True):     
        print('\n1. Inserir registro')
        print('2. Remover registro')
        print('3. Buscar registro por igualdade')
        print('4. Mostrar Hash')
        print('5. Executar casos de teste')
        print('0. Sair')
        n = int(input('Digite uma opção: '))
        
        if n == 1:
            record = [int(x) for x in input('Informe o registro completo com todos os campos:').split(',')]
            if len(record) == qty_fields:
                hash.insert(record[0], record)
            else:
              print('Tamanho de campos no registro não corresponde com o informado.')

        elif n == 2:
           key = int(input('Digite a chave do registro para ser removido: '))
           hash.delete(key)

        elif n == 3:
            key = int(input('Digite a chave para ser buscado o registro: '))
            i, rec = hash.search(key)
            if rec:
                print(rec[i])

        elif n == 4:
            hash.print_hash()

        elif n == 5:
            file = open('10000dpadraodetestes.csv', 'r')
            start = time.time()
            for row in file:
                record = row.split(',')
                if(record[0] == '+'):
                    record = [int(x) for x in record[1:]]
                    hash.insert(record[0], record)
                elif(record[0] == '-'):
                    record = [int(x) for x in record[1:]]
                    hash.delete(record[0])
                end = time.time()
            file.close()
            print(end - start)
        else:
            break

if __name__ == '__main__':
    main()
