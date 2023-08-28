class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.historico_precos = [preco]  # Inicialize com o preço atual
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
        
    def esta_em_promocao(self):
        return self.preco < self.preco_original

    def exibir_informacoes_promocao(self):
        return f"{self.nome} - R${self.preco:.2f} (Preço original: R${self.preco_original:.2f})"
    
    def adicionar_preco_ao_historico(self, novo_preco):
        self.historico_precos.append(novo_preco)
    
# criando novos produtos        
produto_camisa = Produto("Camisa", 39.99)
produto_calcas = Produto("Calças", 69.99)
produto_sapato = Produto("Sapato", 129.99)
produto_bolsa = Produto("Bolsa", 79.99)
produto_oculos = Produto("Óculos de Sol", 59.99)
produto_chapeu = Produto("Chapéu", 29.99)