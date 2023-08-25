class ArmazenamentoDados:
    def __init__(self):
        self.pedidos = {}

    def salvar_pedido(self, pedido_id, pedido, total):
        self.pedidos[pedido_id] = (pedido, total)
        with open(f"pedidos/pedido_{pedido_id}.txt", "w") as arquivo:
            arquivo.write(f"Pedido:\n{pedido}\nTotal: R${total:.2f}\n\n")
        print("Pedido salvo com sucesso.")

    def recuperar_pedido(self, pedido_id):
        pedido, _ = self.pedidos.get(pedido_id, (None, None))
        return pedido

    def obter_total_vendas(self):
        total_vendas = sum(total for _, total in self.pedidos.values())
        return total_vendas

    def obter_total_por_produto(self):
        total_por_produto = {}
        for pedido, _ in self.pedidos.values():
            for produto in pedido.produtos:
                if produto.nome in total_por_produto:
                    total_por_produto[produto.nome] += produto.preco
                else:
                    total_por_produto[produto.nome] = produto.preco
        return total_por_produto

    def aplicar_desconto(self, pedido_id, percentual):
        pedido = self.recuperar_pedido(pedido_id)
        if pedido:
            for produto in pedido.produtos:
                produto.desconto(percentual)
            self.pedidos[pedido_id] = (pedido, pedido.calcular_total())

    def aumentar_preco_produto(self, pedido_id, indice, percentual):
        pedido = self.recuperar_pedido(pedido_id)
        if pedido:
            produto = pedido.produtos[indice]
            produto.aumentar_preco(percentual)
            self.pedidos[pedido_id] = (pedido, pedido.calcular_total())

    def adicionar_produto_especifico(self, pedido_id, produto):
        pedido = self.recuperar_pedido(pedido_id)
        if pedido:
            pedido.adicionar_produto(produto)
            self.pedidos[pedido_id] = (pedido, pedido.calcular_total())

    def listar_pedidos(self):
        pedidos = {}
        for pedido_id, (pedido, total) in self.pedidos.items():
            pedidos[pedido_id] = (pedido, total)
        return pedidos