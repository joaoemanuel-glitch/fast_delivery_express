# fast_delivery_express
Atividade Avaliativa - Programação Orientada a Objetos

Sistema desenvolvido em Python focado na aplicação dos pilares da Programação Orientada a Objetos (POO).

##  Funcionalidades do Sistema
- Cadastro e consulta de clientes por CPF.
- Cadastro de entregadores.
- Criação de pedidos com escolha de frete (Comum, Expressa e Premium).
- Atualização de status dos pedidos.

##  Conceitos Aplicados
- Herança: Classe Pessoa (superclasse) e classes Cliente e Entregador (subclasses).
- Abstração: Classe CalculoFrete
- Encapsulamento com propriedades privadas.
- Interfaces e uso de polimorfismo no cálculo do frete.
- Sistema divido em módulos e pacotes.

## Tecnologias utilizadas
- Python 3
- Git
- GitHub

##  Arquivos
- interfaces/calculo_frete_interface.py: Contém a classe abstrata CalculoFrete que contém o método obrigatório calcular_frete para calcular o frete.
- modelos/cliente.py: Contém a classe Cliente (subclasse que herda de Pessoa).
- modelos/entrega.py: Contém a classes EntregaComum, EntregaExpressa e EntregaPremiun, que utilizam polimorfismo no método calcular_frete.
- modelos/entregador.py: Contém a classe Entregador (subclasse que herda de Pessoa).
- modelos/pedido.py: Contém a classe Pedido.
- modelos/pessoa.py: Contém a classe Pessoa (superclasse).
- services/cliente_service.py: Cadastra e armazena os clientes na lista de pedidos, além das função de buscar por um cliente e de listar todos os clientes.
- services/entrega_service.py: Cadastra e armazena os entregadores na lista de entregadores, além da função de listar todos os entregadores e de escolha do tipo de entrega.
- services/pedido_service.py: Cadastra e armazena os pedidos na lista de pedidos, além das funções de buscar pelos pedidos pelo código e listá-los.
- util/formatador.py: Deixa as mensagens de dinheiro do frete padronizadas.
- util/menu.py: Contém as classes com todos os menus (Menu Principal, Menu de Clientes, Menu de Pedidos e Menu de Entregadores).
- util/validador.py: Faz validações dos dados que o usuário digita no terminal, garantindo que o programa não falhe (por exemplo, se o usuário digitar letras onde deveria ser um número).
- main.py: Código principal.

##  Execução
Usar o comando python main.py no terminal.