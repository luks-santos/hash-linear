# Hash Linear

- Implementação Hash Linear utilizando python, para disciplina de banco de dados II

# Introdução

Para utilização do código implementado há duas possiveis maneiras.

- 1º [Inserção](###inserção), [deleção](###deleção) e [busca por igualdade](###busca)
- 2º [Caso de testes automatizado](###caso de testes automatizado)

# Como usar

Para realizar ambos casos de testes deve ser execultado o arquivo main.py, seja por linha de comando ou por alguma IDE. Após isso deverá ser informado a quantidade de bukets iniciais, tamanho da página e quantidade de campos do registro (recomendado 4 buckets, 1024 bytes e 5 campos), em seguida um menu com os possiveis comandos será exibido, para cada opção há instruções de como realizar inserções, deleções e busca por igualdade. 

### Inserção

Para inserir um registro, pressione a opção 1, em seguida realize os seguintes passos:

- Informe o registro com a quantidade de campos passados na inicialização da árvore separados por virgula.
  
        Ex: Uma árvore com registros de 5 campos, digite no input: 78, 96, 4, 56, 8 (Lembre-se o primeiro número será a chave do registro). 

### Deleção 

Para remover um registro, pressione a opção 2, em seguida realize os seguintes passos:

- Informe a key (primeiro número do registro).
       
        Ex: Uma árvore com um registro de 5 campos: [78, 96, 4, 56, 8], digite 78.

### Busca

Possui 1 opções de busca:

- 1º Busca por igualdade, pressione a opção 3 e Informe a key (primeiro número do registro).

### Print

Para mostrar os buckets do hash, pressione a opção 4.
Buckets com overflow são sinalizados com '-> overflow'
        
### Caso de testes automatizado

Precisa ser usado um arquivo do tipo .csv, o código para ler o arquivo é baseado no csv gerado pela ferramenta [SIOgen](https://ribeiromarcos.github.io/siogen/).

No codigo fonte se necessario mudar o nome do arquivo para outros testes. 

- Basta pressionar a opção 5 e utilizar as opções listadas acima, como inserção, deleção, busca, print.













