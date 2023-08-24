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
