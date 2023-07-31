"""
operadores aritmeticos

+
-
*
/
// -> divisão inteira
%  -> modulo
** -> exponenciação

"""

print(1+1)
print(1-1)
print(1*1)
print(1/1)
print(1.1//1)
print(13%3)
print(2**3)

"""
operadores de comparação

== -> igualdade
!= -> diferença
>  -> maior que
>= -> maior ou igual
<  -> menor que
<= -> menor ou igual
"""
saldo = 450
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)

"""
operadores de atribuição

=  -> atribuição simples
+= -> atribuição com adição
-=
*=
/=
**=
%=

"""

saldo = 500
print(saldo)

saldo += 200
print(saldo)

saldo -= 200
print(saldo)

saldo *= 2
print(saldo)

saldo /= 5
print(saldo)

saldo %= 3
print(saldo)

saldo **= 2
print(saldo)

"""
operadores logicos

and
or
not

"""

lista = []
print(not lista) #lista vazia é considerado False
print(not 1000 > 1500)
print(not "saque 1500;") #string com valor é considerada True
print(not "") #string vazia é considerado False

saldo = 1000
saque = 250
limite = 200
contaEspecial = True

print(saldo >= saque and saque <= limite or contaEspecial and saldo >= saque)
print((saldo >= saque and saque <= limite) or (contaEspecial and saldo >= saque))

"""
operadores de identidade 
são utilizados para comparar se dois objetos ocupam a mesma posição na memoria

is
is not

"""

curso = "Curso de Python"
nomeCurso = curso
saldo, limite = 200, 200

print(curso is nomeCurso)
print(curso is not nomeCurso)
print(saldo is limite)

"""
operadores de associação
são utilizados para verficar se um objeto está presente em uma sequencia

in
not in

"""

curso = "Curso de Python"
frutas = ['laranja', 'uva', 'limão']
saques = [1500, 100]

print("Python" in curso)
print("maçã" not in frutas)
print(200 in saques)