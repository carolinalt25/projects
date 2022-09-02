# Programa: Filas.py
# Descrição: Prova P2 - Exercício 002_
#                FIFO - First in First Out
#Por meio de uma estrutura do tipo Fila, organize os pedidos em uma lanchonete chamada “XBurgão” em
#que a ordem dos pedidos pagos no caixa seja a ordem de atendimento na cozinha e
#também a ordem de chamado para que o cliente venha buscar seu lanche pronto. O número do
#pedido do cliente deverá ser exibido em um painel.
#Obs: Todas as mensagens de aviso ao cliente devem ser emitidas pelo sistema, ou seja, pedido feito,
#encaminhado à cozinha e pedido concluído com a exibição do número no painel.
# Author: Ana Carolina Lopes Teixeira
# Data: 17 de junho de 2021

class Fila:


    def __init__(self):
        self.fila = []

    def inserir (self,n):
        self.fila.append(n)

    def excluir (self):
        if not self.vazia():
            return self.fila.pop(0)

    def vazia(self):
        return self.tamanho()==0

    def exibirFila(self):
        print(self.fila)

    def tamanho(self):
        return len(self.fila)

clientes = Fila()

print("\n\nX-Burgão,tenha um excelente dia! Os seguintes pedidos fizeram pagamento no caixa:\n")
clientes.inserir(10)
clientes.inserir(11)
clientes.inserir(12)
clientes.inserir(13)
clientes.inserir(14)
clientes.inserir(15)
clientes.inserir(16)
clientes.inserir(17)
clientes.inserir(18)
clientes.exibirFila()

while not clientes.vazia():
    print(f'\nPedido feito e encaminhado para preparo. Há {clientes.tamanho()} pedidos encaminhados à cozinha e aguardando preparo')
    clientes.exibirFila()
    print(f'Pedido Concluído,cliente: {clientes.excluir()} favor retirar seu pedido no balcão.')


if (clientes.vazia() == False):
    print(f'Pedido feito e encaminhado para preparo. Há {clientes.tamanho()} pedidos encaminhados à cozinha e aguardando preparo')
else:
    print(f'\n\n>>>Não há mais pedidos em espera.<<<')

