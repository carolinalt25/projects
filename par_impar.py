#faça um programa que leia uma lista de números inteiros e verifique se o número é par ou ímpar,
# se for par, escreva na tela "PAR", se for ímpar, escreve "ÍMPAR"


#definir tamanho da lista
tamanho = int(input("Digite o tamanho da sequência de números: "))

#contador
i = 0

#parâmetro de números digitados para definir se número é par ou ímpar
num = 1

while i < tamanho:   #enquanto contador for menor que o tamanho definido pelo inicializador, rodar esse loop
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:     #se o resto do número for 0, o número é par
        print("par")
    else:               #ao contrário, o número é impar
        print("ímpar")
    i = i + 1