from domain.models.pedido import Pedido

class PedidoController:
    def __init__(self, pedido_service):
        self.pedido_service = pedido_service

    def processar_pedido(self):
        pedido = Pedido()
        produto = input("Digite o nome do produto a ser adicionado ao pedido: ")
        pedido.adicionar_produto(produto)
        self.pedido_service.processar_pedido(pedido)
        print("Pedido processado com sucesso!")

    def exibir_resumo_pedido(self):
        # Chamada para exibir resumo do pedido
        pass

    def exibir_total_vendas(self):
        # Chamada para exibir total de vendas
        pass

    def exibir_total_por_produto(self):
        # Chamada para exibir total de vendas por produto
        pass

    def aplicar_desconto(self):
        # Chamada para aplicar desconto a produtos no pedido
        pass

    def aumentar_preco_produto(self):
        # Chamada para aumentar preço de um produto
        pass

    def adicionar_produto_ao_pedido(self):
        # Chamada para adicionar um produto específico a um pedido
        pass
