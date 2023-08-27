import uuid
from domain.models.pedido import Pedido
from domain.models.produto import Produto


class PedidoRepository:
    def __init__(self, armazenamento_dados):
        self.armazenamento_dados = armazenamento_dados
        self.pedidos = {}

    def salvar_pedido(self, pedido, total):
        pedido_id = str(uuid.uuid4())  # Gera um ID único
        self.pedidos[pedido_id] = (pedido, total)
        self.armazenamento_dados.salvar_pedido(pedido_id, pedido, total)
        return pedido_id
    
    def encontrar_pedido_id(self, pedido):
        for pedido_id, (pedido_atual, _) in self.pedidos.items():
            if pedido == pedido_atual:
                return pedido_id
        return None

    def recuperar_pedido(self, pedido_id):
        pedido, _ = self.pedidos.get(pedido_id, (None, None))
        if pedido is None:
            return None
        return pedido

    def atualizar_pedido(self, pedido_id, novo_pedido):
        _, total = self.pedidos.get(pedido_id, (None, None))
        self.pedidos[pedido_id] = (novo_pedido, total)

    def obter_total_vendas(self):
        total_vendas = sum(total for _, total in self.pedidos.values())
        return total_vendas

    def obter_total_por_produto(self, pedido):
        total_por_produto = {}

        if not isinstance(pedido, Pedido):
            return "Objeto do tipo Pedido é esperado."

        for produto in pedido.produtos:
            if produto.nome in total_por_produto:
                total_por_produto[produto.nome] += produto.preco
            else:
                total_por_produto[produto.nome] = produto.preco

        return total_por_produto

    def aplicar_desconto(self, pedido_id, percentual):
        pedido = self.recuperar_pedido(pedido_id)
        if pedido:
            pedido.aplicar_desconto(percentual)
            self.atualizar_pedido(pedido_id, pedido)

    def aumentar_preco_produto(self, pedido_id, indice, percentual):
        pedido = self.recuperar_pedido(pedido_id)
        if pedido:
            pedido.aumentar_preco_produto(indice, percentual)
            self.atualizar_pedido(pedido_id, pedido)

    def adicionar_produto_especifico(self, pedido_id, produto):
        pedido = self.recuperar_pedido(pedido_id)
        if pedido:
            pedido.adicionar_produto_especifico(produto)
            self.atualizar_pedido(pedido_id, pedido)
    
    def listar_pedidos(self):
        pedidos = {}
        for pedido_id, (pedido, total) in self.pedidos.items():
            pedidos[pedido_id] = total
        return pedidos

    def produtos_disponiveis(self):
        produtos = [
            Produto("Camisa", 39.99),
            Produto("Calças", 69.99),
            Produto("Sapato", 129.99),
            Produto("Bolsa", 79.99),
            Produto("Óculos de Sol", 59.99),
            Produto("Chapéu", 29.99)
        ]
        return produtos
    
    def existe_pedido(self, pedido_id):
        return pedido_id in self.pedidos