with open('manipulacaoArquivos/dados.csv') as arquivo:
    with open('manipulacaoArquivos/dados.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo já foi fechado')