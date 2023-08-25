from application.controller.pedido_controller import PedidoController
from domain.models.produto import Produto
from domain.services.pedido_service import PedidoService
from domain.repository.pedido_repository import PedidoRepository
from infrastructure.storage.armazenamento_dados import ArmazenamentoDados

armazenamento = ArmazenamentoDados()
pedido_repository = PedidoRepository(armazenamento)
pedido_service = PedidoService(pedido_repository)
pedido_controller = PedidoController(pedido_service)

pedido_id = pedido_controller.processar_pedido()
pedido_controller.exibir_resumo_pedido(pedido_id)
pedido_controller.exibir_total_vendas()
pedido_controller.exibir_total_por_produto()
pedido_controller.aplicar_desconto(pedido_id, 10)
pedido_controller.aumentar_preco_produto(pedido_id, 0, 5)
pedido_controller.adicionar_produto_ao_pedido(pedido_id, Produto("Sapato", 149.99))
pedido_controller.aplicar_promocao(pedido_id, "Sapato", 129.99)
pedido_controller.listar_pedidos()
