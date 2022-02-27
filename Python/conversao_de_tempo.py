"""
Desafio
Você terá o desafio de ler um valor inteiro,
que é o tempo de duração em segundos de um
determinado evento em uma loja, e informe-o
expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos),
convertido para horas:minutos:segundos, conforme exemplo fornecido.
"""

segundos = int(input())

resto = int(segundos % 3600)#TODO Implementar a formula para calcular os minutos.

horas = int(segundos / 3600) #TODO Implementar a formula para calcular as horas.
segundos = int(resto % 60)
minutos = int(resto / 60)

print("{}:{}:{}".format(horas, minutos, segundos))