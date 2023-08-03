#Maiuscula, minuscula e titulo

curso = "python"

print(curso.upper())
print(curso.lower())
print(curso.title())

#eliminando espaços em branco

curso = "   Python "

print(curso.strip())
print(curso.lstrip())
print(curso.rsplit())

# junções e centralização

nome = input("Insira seu nome: ")
print(nome.center(10,"#"))
print(".".join(nome))

# interpolação de strings
# 3 formas = %, format e f

nome = "João"
idade = 20
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalha conmo %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem))

nome = "João"
idade = 20
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalha conmo {} e estou matriculado no curso de {}".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalha conmo {1} e estou matriculado no curso de {0}".format(linguagem, profissao, idade, nome))
