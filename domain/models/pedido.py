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
        pedido_atual = self.pedido_service.recuperar_pedido_atual()

        if pedido_atual:
            print("Resumo do Pedido:")
            print(f"Pedido ID: {pedido_atual.id}")
            print("Produtos:")
            for i, produto in enumerate(pedido_atual.produtos, start=1):
                print(f"{i}. {produto.nome} - Preço: R${produto.preco:.2f}")

            total = pedido_atual.calcular_total()
            print(f"Total do Pedido: R${total:.2f}")
        else:
            print("Nenhum pedido em andamento.")

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
        
    def calcular_total_com_desconto(self, percentual):
        total = self.calcular_total()
        return total - total * percentual / 100
    
    def aplicar_desconto_global(self, percentual):
        for produto in self.produtos:
            produto.aplicar_desconto(percentual)

    def calcular_total_com_desconto_global(self, percentual):
        total_com_desconto = self.calcular_total() * (1 - percentual / 100)
        return total_com_desconto

    def produtos_em_promocao(self):
        return [produto for produto in self.produtos if produto.esta_em_promocao()]