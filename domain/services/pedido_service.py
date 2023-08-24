from domain.models.pedido import Pedido
from infrastructure.storage.armazenamento_dados import ArmazenamentoDados

class PedidoService:
    def __init__(self, pedido_repository):
        self.pedido_repository = pedido_repository

    def processar_pedido(self, pedido):
        total = pedido.calcular_total()
        self.pedido_repository.salvar_pedido(pedido.exibir_pedido(), total)

    def exibir_resumo_pedido(self, pedido):
        # Chamada para exibir resumo do pedido
        pass

    def exibir_total_vendas(self):
        # Chamada para exibir total de vendas
        pass

    def exibir_total_por_produto(self):
        # Chamada para exibir total de vendas por produto
        pass

    def aplicar_desconto(self, percentual):
        # Chamada para aplicar desconto a produtos no pedido
        pass

    def aumentar_preco_produto(self, indice, percentual):
        # Chamada para aumentar preço de um produto
        pass
