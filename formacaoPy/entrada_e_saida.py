
# entrada -> input = le dados da entrada e converte em string

nome = input("informe seu nome: ") #o input irá se tornar no valor da variavel nome

# saida -> print = exibe dados na saída
# tem um argumento varargs e 4 args opcionais sep end file e flush
# todos os objetos serao convertidos em string, separados por sep e terminados em end

nome = "João"
sobrenome = "Monteiro"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep=" + ")
