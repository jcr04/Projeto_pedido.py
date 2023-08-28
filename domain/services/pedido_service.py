from domain.models.pedido import Pedido
from domain.repository.pedido_repository import PedidoRepository

class PedidoService:
    def __init__(self, pedido_repository):
        self.pedido_repository = pedido_repository
        self.pedidos_processados = []

    def processar_pedido(self, pedido):
        total = pedido.calcular_total()
        pedido_id = self.pedido_repository.salvar_pedido(pedido.exibir_pedido(), total)
        self.pedidos_processados.append(pedido_id)  # Adiciona o ID à lista
        return pedido_id

    def exibir_resumo_pedido(self, pedido):
        pedido_id = self.pedido_repository.encontrar_pedido_id(pedido)
        if pedido_id is None:
            return "Pedido não encontrado."
        return pedido.exibir_resumo()

    def exibir_total_vendas(self):
        return self.pedido_repository.obter_total_vendas()

    def exibir_total_por_produto(self, pedido_id):
        pedido = self.pedido_repository.recuperar_pedido(pedido_id)

        if pedido is None:
            return "Pedido não encontrado."

        return self.pedido_repository.obter_total_por_produto(pedido)

    def aplicar_desconto(self, pedido_id, percentual):
        pedido = self.pedido_repository.recuperar_pedido(pedido_id)
        
        if pedido is None:
            return "Pedido não encontrado."
        
        pedido.aplicar_desconto(percentual)
        self.pedido_repository.atualizar_pedido(pedido_id, pedido)

    def aumentar_preco_produto(self, pedido_id, indice, percentual):
        pedido = self.pedido_repository.recuperar_pedido(pedido_id)
            
        if pedido:
            pedido.aumentar_preco_produto(indice, percentual)
            self.pedido_repository.atualizar_pedido(pedido_id, pedido)
        else:
            print("Pedido não encontrado.")

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

    def produtos_disponiveis(self):
        return self.pedido_repository.produtos_disponiveis()
    
    def recuperar_pedido(self, pedido_id):
        return self.pedido_repository.recuperar_pedido(pedido_id)
    
    def produtos_em_promocao(self):
        produtos_em_promocao = []
        for pedido_id, (pedido, _) in self.pedido_repository.pedidos.items():
            produtos_em_promocao.extend(pedido.produtos_em_promocao())
        return produtos_em_promocao
    
    def calcular_receita_total(self):
        return self.pedido_repository.obter_total_vendas()

    def obter_produtos_mais_vendidos(self, quantidade=5):
        pedidos = self.pedido_repository.listar_pedidos()
        produtos_vendidos = {}

        for pedido_id, _ in pedidos.items():
            pedido = self.pedido_repository.recuperar_pedido(pedido_id)
            
            if isinstance(pedido, Pedido):  # Verifica se o pedido é um objeto Pedido
                for produto in pedido.produtos:
                    if produto.nome in produtos_vendidos:
                        produtos_vendidos[produto.nome] += 1
                    else:
                        produtos_vendidos[produto.nome] = 1

        produtos_mais_vendidos = sorted(produtos_vendidos.items(), key=lambda x: x[1], reverse=True)
        return produtos_mais_vendidos[:quantidade]