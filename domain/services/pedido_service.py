from domain.models.pedido import Pedido
from domain.repository.pedido_repository import PedidoRepository

class PedidoService:
    def __init__(self, pedido_repository):
        self.pedido_repository = pedido_repository

    def processar_pedido(self, pedido):
        total = pedido.calcular_total()
        pedido_id = self.pedido_repository.salvar_pedido(pedido.exibir_pedido(), total)
        return pedido_id

    def exibir_resumo_pedido(self, pedido_id):
        pedido = self.pedido_repository.recuperar_pedido(pedido_id)
        
        if pedido is None:
            return "Pedido não encontrado."
        
        return pedido.exibir_resumo()

    def exibir_total_vendas(self):
        return self.pedido_repository.obter_total_vendas()

    def exibir_total_por_produto(self):
        return self.pedido_repository.obter_total_por_produto()

    def aplicar_desconto(self, pedido_id, percentual):
        pedido = self.pedido_repository.recuperar_pedido(pedido_id)
        pedido.aplicar_desconto(percentual)
        self.pedido_repository.atualizar_pedido(pedido_id, pedido)

    def aumentar_preco_produto(self, pedido_id, indice, percentual):
        pedido = self.pedido_repository.recuperar_pedido(pedido_id)
        pedido.aumentar_preco_produto(indice, percentual)
        self.pedido_repository.atualizar_pedido(pedido_id, pedido)

    def adicionar_produto_ao_pedido(self, pedido_id, produto):
        pedido = self.pedido_repository.recuperar_pedido(pedido_id)
        pedido.adicionar_produto_especifico(produto)
        self.pedido_repository.atualizar_pedido(pedido_id, pedido)
    
    def aplicar_promocao(self, pedido_id, produto, novo_preco):
        pedido = self.pedido_repository.recuperar_pedido(pedido_id)
        for p in pedido.produtos:
            if p.nome == produto:
                p.aplicar_promocao(novo_preco)
        self.pedido_repository.atualizar_pedido(pedido_id, pedido)

    def listar_pedidos(self):
        return self.pedido_repository.listar_pedidos()
