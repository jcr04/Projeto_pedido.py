from domain.models.pedido import Pedido
from domain.models.produto import Produto
from application.controller.pedido_controller import PedidoController
from domain.services.pedido_service import PedidoService
from domain.repository.pedido_repository import PedidoRepository
from infrastructure.storage.armazenamento_dados import ArmazenamentoDados

def mostrar_menu():
    print("========== MENU DE OPÇÕES ==========")
    print("1. Processar Pedido")
    print("2. Exibir Resumo de Pedido")
    print("3. Exibir Total de Vendas")
    print("4. Exibir Total por Produto")
    print("5. Aplicar Desconto")
    print("6. Aumentar Preço do Produto")
    print("7. Adicionar Produto ao Pedido")
    print("8. Aplicar Promoção")
    print("9. Listar Pedidos")
    print("0. Sair")
    print("=====================================")

def main():
    armazenamento = ArmazenamentoDados()
    pedido_repository = PedidoRepository(armazenamento)
    pedido_service = PedidoService(pedido_repository)
    pedido_controller = PedidoController(pedido_service)

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pedido_controller.exibir_produtos_disponiveis()  # Mostra os produtos disponíveis
            produtos_escolhidos = []
            while True:
                escolha_produto = input("Escolha um produto (ou '0' para finalizar): ")
                if escolha_produto == "0":
                    break
                elif escolha_produto.isdigit():
                    index_produto = int(escolha_produto) - 1
                    if 0 <= index_produto < len(pedido_service.produtos_disponiveis()):
                        produtos_escolhidos.append(pedido_service.produtos_disponiveis()[index_produto])
                        print(f"{pedido_service.produtos_disponiveis()[index_produto].nome} adicionado ao pedido.")
                    else:
                        print("Escolha inválida.")
                else:
                    print("Escolha inválida.")
            
            if produtos_escolhidos:
                pedido = Pedido()
                for produto in produtos_escolhidos:
                    pedido.adicionar_produto(produto)
                pedido_controller.processar_pedido(pedido)  # Passe o pedido como argumento
                print("Pedido processado com sucesso!")
            else:
                print("Nenhum produto foi adicionado ao pedido.")


        elif opcao == "2":
            # Recuperar o pedido_id corretamente (pode ser solicitado ao usuário)
            pedido_id = input("Digite o ID do pedido: ")
            pedido = pedido_repository.recuperar_pedido(pedido_id)
            if pedido is not None:
                pedido_controller.exibir_resumo_pedido(pedido)
            else:
                print("Pedido não encontrado.")

        elif opcao == "3":
            pedido_controller.exibir_total_vendas()

        elif opcao == "4":
            # Recuperar o pedido_id corretamente (pode ser solicitado ao usuário)
            pedido_id = input("Digite o ID do pedido: ")
            pedido = pedido_repository.recuperar_pedido(pedido_id)
            if pedido is not None:
                pedido_controller.exibir_total_por_produto(pedido)
            else:
                print("Pedido não encontrado.")

        elif opcao == "5":
            pedido_id = input("Digite o ID do pedido: ")
            percentual = float(input("Digite o percentual de desconto: "))
            pedido_controller.aplicar_desconto(pedido_id, percentual)
            print("Desconto aplicado com sucesso!")

        elif opcao == "6":
            # Recuperar o pedido_id corretamente (pode ser solicitado ao usuário)
            pedido_id = input("Digite o ID do pedido: ")
            
            if pedido_repository.existe_pedido(pedido_id):
                indice = int(input("Digite o índice do produto: "))
                percentual = float(input("Digite o percentual de aumento: "))
                pedido_controller.aumentar_preco_produto(pedido_id, indice, percentual)
                print("Preço do produto aumentado com sucesso!")
            else:
                print("Pedido não encontrado.")

        elif opcao == "7":
            pedido_id = input("Digite o ID do pedido: ")
            produto_nome = input("Digite o nome do produto: ")
            produto_preco = float(input("Digite o preço do produto: "))
            produto = Produto(produto_nome, produto_preco)
            pedido_controller.adicionar_produto_ao_pedido(pedido_id, produto)
            print("Produto adicionado ao pedido com sucesso!")

        elif opcao == "8":
            pedido_id = input("Digite o ID do pedido: ")
            produto = input("Digite o nome do produto: ")
            novo_preco = float(input("Digite o novo preço: "))
            pedido_controller.aplicar_promocao(pedido_id, produto, novo_preco)
            print(f"Promoção aplicada com sucesso ao produto {produto}!")

        elif opcao == "9":
            pedido_controller.listar_pedidos()

        elif opcao == "0":
            break

if __name__ == "__main__":
    main()