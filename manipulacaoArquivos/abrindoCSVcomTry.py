try:
    arquivo = open('manipulacaoArquivos/dados.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

finally:
        arquivo.close()
        print('Arquivo fechado')

if arquivo.closed:
        print('Arquivo fechado com sucesso')