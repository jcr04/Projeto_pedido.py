from application.controller.pedido_controller import PedidoController
from domain.services.pedido_service import PedidoService
from domain.repository.pedido_repository import PedidoRepository
from infrastructure.storage.armazenamento_dados import ArmazenamentoDados

armazenamento = ArmazenamentoDados()
pedido_repository = PedidoRepository(armazenamento)
pedido_service = PedidoService(pedido_repository)
pedido_controller = PedidoController(pedido_service)

pedido_controller.processar_pedido()
pedido_controller.exibir_resumo_pedido()
pedido_controller.exibir_total_vendas()
pedido_controller.exibir_total_por_produto()
pedido_controller.aplicar_desconto()
pedido_controller.aumentar_preco_produto()
