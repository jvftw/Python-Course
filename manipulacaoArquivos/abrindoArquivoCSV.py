arquivo = open('manipulacaoArquivos/dados.csv')
dados = arquivo.read()
for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()
