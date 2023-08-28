from domain.models.pedido import Pedido
from domain.models.produto import Produto

class PedidoController:
    def __init__(self, pedido_service):
        self.pedido_service = pedido_service

    def processar_pedido(self, pedido):
        self.pedido_service.processar_pedido(pedido)  # Passe o pedido como argumento
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
        pedido = self.pedido_repository.recuperar_pedido(pedido_id)
        for p in pedido.produtos:
            if p.nome == produto:
                p.adicionar_preco_ao_historico(p.preco)  # Adicione o preço anterior ao histórico
                p.aplicar_promocao(novo_preco)
        self.pedido_repository.atualizar_pedido(pedido_id, pedido)
        print(f"Promoção aplicada com sucesso ao produto {produto}!")

    def listar_pedidos(self):
        pedidos = self.pedido_service.listar_pedidos()
        for pedido_id, total in pedidos.items():
            print(f"Pedido ID: {pedido_id} - Total: R${total:.2f}")
            
    def exibir_produtos_disponiveis(self):
        produtos = self.pedido_service.produtos_disponiveis()
        for i, produto in enumerate(produtos, start=1):
            print(f"{i}. {produto.nome} - R${produto.preco:.2f}")
    
    def exibir_pedidos_processados(self):
        for pedido_id in self.pedido_service.pedidos_processados:
            print(f"Pedido ID: {pedido_id} - Produtos: {self.pedido_service.exibir_resumo_pedido(pedido_id)}")
            
    def exibir_produtos_do_pedido(self, pedido_id):
        pedido = self.pedido_service.recuperar_pedido(pedido_id)
        if pedido:
            print("Produtos do pedido:")
            for i, produto in enumerate(pedido.produtos, start=1):
                print(f"{i}. {produto.nome} - Preço: R${produto.preco:.2f}")
        else:
            print("Pedido não encontrado.")
            
    def exibir_produtos_em_promocao(self):
        produtos_em_promocao = self.pedido_service.produtos_em_promocao()
        if produtos_em_promocao:
            print("Produtos em promoção:")
            for produto in produtos_em_promocao:
                print(produto.exibir_informacoes_promocao())
        else:
            print("Nenhum produto em promoção.")
            
    def exibir_historico_preco_produto(self, produto):
        produto = self.encontrar_produto_por_nome(produto)
        if produto:
            print(f"Histórico de Preços para {produto.nome}:")
            for i, preco in enumerate(produto.historico_precos, start=1):
                print(f"{i}. R${preco:.2f}")
        else:
            print("Produto não encontrado.")

    def encontrar_produto_por_nome(self, nome_produto):
        for produto in self.pedido_service.produtos_disponiveis():
            if produto.nome == nome_produto:
                return produto
        return None
    
    def exibir_relatorio_vendas_diarias(self):
        # Obter a lista de pedidos
        pedidos = self.pedido_service.listar_pedidos()

        # Criar um dicionário para armazenar as vendas por dia
        vendas_diarias = {}

        for pedido_id, _ in pedidos.items():
            pedido = self.pedido_service.recuperar_pedido(pedido_id)
            if pedido:
                data_pedido = pedido.data_pedido  # Suponha que a classe Pedido tenha um atributo data_pedido
                dia = data_pedido.strftime("%Y-%m-%d")  # Formatando a data para YYYY-MM-DD

                if dia in vendas_diarias:
                    vendas_diarias[dia] += pedido.calcular_total()
                else:
                    vendas_diarias[dia] = pedido.calcular_total()

        # Exibir o relatório de vendas diárias
        print("Relatório de Vendas Diárias:")
        for dia, total_vendas in vendas_diarias.items():
            print(f"{dia}: R${total_vendas:.2f}")
        
    def exibir_produtos_mais_vendidos(self):
        produtos_mais_vendidos = self.pedido_service.obter_produtos_mais_vendidos()
        print("Produtos Mais Vendidos:")
        for produto, quantidade in produtos_mais_vendidos:
            print(f"{produto}: {quantidade} unidades")

    def exibir_receita_total(self):
        receita_total = self.pedido_service.calcular_receita_total()
        print(f"Receita Total: R${receita_total:.2f}")
        
    