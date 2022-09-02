#indicadores de passagem
#indicadores que dizem que determinado indicador é verdadeiro ou não
#dizer se a sequencia de números está em ordem decrescente ou não.
#definir critério de parada

decrescente = True
anterior = int(input("Digite o primeiro número da sequência: "))

valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite o próximo número da sequência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print("A sequência está em ordem decrescente!")
else:
    print("A sequência não está em ordem decrescente :( ")
