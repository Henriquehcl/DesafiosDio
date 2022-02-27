"""
Escreva um programa que leia 2 valores X e Y e
que imprima todos os valores entre eles cujo resto
da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos
inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo,
sempre em ordem crescente.
"""

x = int(input())
y = int(input())

if x > y:
    a = y
    b = x

if x <= y:
    a = x
    b = y
a = a + 1
while a < b:
    if a % 5 == 2 or a % 5 == 3:
        print(a)
    a = a + 1
