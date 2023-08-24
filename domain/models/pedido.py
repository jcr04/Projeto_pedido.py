class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        # Implementação do cálculo do total do pedido
        pass  # Você deve adicionar a implementação real aqui

    def exibir_pedido(self):
        return "\n".join(str(produto) for produto in self.produtos)

    def exibir_resumo(self):
        # Implementação para exibir um resumo do pedido
        pass  # Você deve adicionar a implementação real aqui

    def atualizar_produto(self, indice, novo_produto):
        # Implementação para atualizar um produto no pedido
        pass  # Você deve adicionar a implementação real aqui
    
    def calcular_total_por_produto(self):
        # Implementação para calcular o total por produto
        pass
    
    def aplicar_desconto(self, percentual):
        # Implementação para aplicar desconto a todos os produtos do pedido
        pass
    
    def aumentar_preco_produto(self, indice, percentual):
        # Implementação para aumentar o preço de um produto no pedido
        pass
    
    def adicionar_produto_especifico(self, produto):
        # Implementação para adicionar um produto específico ao pedido
        pass