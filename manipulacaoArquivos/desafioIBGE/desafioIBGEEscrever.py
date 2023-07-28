import csv
from urllib import request

def readNwrite(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1')
        print('Download completo')

        with open('desafio-ibge.txt', 'w') as arquivo:
            writer = csv.writer(arquivo)

            for cidade in csv.reader(dados.splitlines()):
                cidadeEscrita = f'{cidade[8]}: {cidade[3]}'
                print(cidadeEscrita)
                writer.writerow([cidadeEscrita])

        print('Escrito no txt com sucesso!')

if __name__ == '__main__':
    readNwrite(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
