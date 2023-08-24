class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        total = sum(produto.preco for produto in self.produtos)
        return total

    def exibir_pedido(self):
        return "\n".join(str(produto) for produto in self.produtos)

    def exibir_resumo(self):
        # Implementação para exibir um resumo do pedido
        pass  # Você deve adicionar a implementação real aqui

    def atualizar_produto(self, indice, novo_produto):
        self.produtos[indice] = novo_produto
    
    def calcular_total_por_produto(self):
        total_por_produto = {}
        for produto in self.produtos:
            if produto.nome in total_por_produto:
                total_por_produto[produto.nome] += produto.preco
            else:
                total_por_produto[produto.nome] = produto.preco
        return total_por_produto
    
    def aplicar_desconto(self, percentual):
        for produto in self.produtos:
            produto.desconto(percentual)
    
    def aumentar_preco_produto(self, indice, percentual):
        produto = self.produtos[indice]
        produto.aumentar_preco(percentual)
    
    def adicionar_produto_especifico(self, produto):
        self.produtos.append(produto)