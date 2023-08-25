class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_informacoes(self):
        return f"{self.nome} - R${self.preco:.2f}"

    def __str__(self):
        return self.nome

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco

    def desconto(self, percentual):
        self.preco -= self.preco * percentual / 100

    def aumentar_preco(self, percentual):
        self.preco += self.preco * percentual / 100

    def aplicar_promocao(self, nova_preco):
        self.preco = nova_preco
# criando novos produtos        
produto_camisa = Produto("Camisa", 39.99)
produto_calcas = Produto("Calças", 69.99)
produto_sapato = Produto("Sapato", 129.99)
produto_bolsa = Produto("Bolsa", 79.99)
produto_oculos = Produto("Óculos de Sol", 59.99)
produto_chapeu = Produto("Chapéu", 29.99)