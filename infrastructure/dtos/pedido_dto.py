class PedidoDTO:
    def __init__(self, pedido, total):
        self.pedido = pedido
        self.total = total
        
    def exibir_informacoes(self):
        return f"Pedido ID: {self.pedido_id}\n{self.pedido}\nTotal: R${self.total:.2f}"