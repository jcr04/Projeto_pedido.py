from domain.models.pedido import Pedido
from domain.models.produto import Produto

class PedidoController:
    def __init__(self, pedido_service):
        self.pedido_service = pedido_service

    def processar_pedido(self):
        pedido = Pedido()
        produto_nome = input("Digite o nome do produto a ser adicionado ao pedido: ")
        produto_preco = float(input("Digite o preço do produto: "))
        produto = Produto(produto_nome, produto_preco)
        pedido.adicionar_produto(produto)
        self.pedido_service.processar_pedido(pedido)
        print("Pedido processado com sucesso!")

    def exibir_resumo_pedido(self, pedido):
        resumo = self.pedido_service.exibir_resumo_pedido(pedido)
        print(resumo)

    def exibir_total_vendas(self):
        total = self.pedido_service.exibir_total_vendas()
        print(f"Total de Vendas: R${total:.2f}")

    def exibir_total_por_produto(self, pedido_id):
        total_por_produto = self.pedido_service.exibir_total_por_produto(pedido_id)
        for produto, total in total_por_produto.items():
            print(f"{produto}: R${total:.2f}")

    def aplicar_desconto(self, pedido_id, percentual):
        self.pedido_service.aplicar_desconto(pedido_id, percentual)
        print("Desconto aplicado com sucesso!")

    def aumentar_preco_produto(self, pedido_id, indice, percentual):
        self.pedido_service.aumentar_preco_produto(pedido_id, indice, percentual)
        print("Preço do produto aumentado com sucesso!")

    def adicionar_produto_ao_pedido(self, pedido_id, produto):
        self.pedido_service.adicionar_produto_ao_pedido(pedido_id, produto)
        print("Produto adicionado ao pedido com sucesso!")
    
    def aplicar_promocao(self, pedido_id, produto, novo_preco):
        self.pedido_service.aplicar_promocao(pedido_id, produto, novo_preco)
        print(f"Promoção aplicada com sucesso ao produto {produto}!")

    def listar_pedidos(self):
        pedidos = self.pedido_service.listar_pedidos()
        for pedido_id, total in pedidos.items():
            print(f"Pedido ID: {pedido_id} - Total: R${total:.2f}")
