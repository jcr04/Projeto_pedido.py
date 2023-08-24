# Projeto de Gerenciamento de Pedidos
O projeto é um sistema de gerenciamento de pedidos, onde os clientes podem adicionar produtos a um carrinho de compras, processar o pedido e aplicar descontos ou aumentar preços aos produtos. O sistema possui uma arquitetura em camadas, onde diferentes responsabilidades são separadas em módulos distintos. Além disso, também utiliza os princípios de Design Orientado a Domínio (DDD) para organizar os componentes do sistema.

# Arquitetura em Camadas
A arquitetura em camadas divide o sistema em três camadas principais:
### Interface do Usuário (pedido_controller.py)
Esta camada lida com a interação do usuário. Ela recebe os inputs do usuário, como produtos a serem adicionados ao carrinho, e exibe informações relevantes. Ela encapsula a interação direta com o usuário.
### Lógica de Negócios (pedido.py, pedido_service.py)
Aqui reside a lógica que governa o comportamento do sistema. A classe Pedido contém métodos para adicionar produtos, calcular totais, aplicar descontos e aumentar preços. O PedidoService lida com as operações de negócio, como processar o pedido, exibir resumos e cálculos relacionados aos pedidos.
### Armazenamento de Dados (pedido_repository.py, armazenamento_dados.py)
Essa camada é responsável pelo armazenamento e persistência de dados. O PedidoRepository lida com operações de armazenamento específicas dos pedidos, enquanto a classe ArmazenamentoDados lida com a escrita e recuperação de dados em um arquivo de texto.
# Princípios de Projeto Aplicados
### Modularidade
O projeto está estruturado em módulos distintos, como PedidoController, PedidoService, PedidoRepository, etc. Cada módulo possui uma responsabilidade específica e encapsula seu comportamento. Isso torna o código mais organizado, fácil de manter e escalável.
### Ocultação da Informação
Os detalhes de implementação são ocultados do mundo exterior por meio de interfaces claras. Cada camada (Interface do Usuário, Lógica de Negócios, Armazenamento de Dados) define suas próprias interfaces e expõe apenas os métodos essenciais para as outras camadas interagirem.
### Independência Funcional
Cada camada funciona independentemente das outras. Isso significa que a Interface do Usuário não precisa conhecer os detalhes internos da Lógica de Negócios ou do Armazenamento de Dados. Isso facilita a manutenção e permite a substituição de uma camada sem afetar as outras.
### Design Orientado a Domínio (DDD)
O projeto incorpora conceitos do DDD, como a divisão em Domínios (produtos, pedidos), Repositórios (PedidoRepository) e Serviços (PedidoService). Isso ajuda a refletir de forma mais fiel a estrutura do negócio no código.
### Coerência e Coesão
As classes em cada camada têm responsabilidades bem definidas e coesas. Isso resulta em um código mais legível, fácil de entender e de manter.

Em resumo, o projeto ilustra a aplicação de uma arquitetura em camadas combinada com os princípios de projeto de modularidade, ocultação da informação e independência funcional. Esses elementos trabalham juntos para criar um sistema mais organizado, flexível e escalável, capaz de evoluir de acordo com as mudanças nos requisitos do negócio. 
