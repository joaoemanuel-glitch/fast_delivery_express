from services.cliente_service import ClienteService # Importa a classe ClienteService
from services.pedido_service import PedidoService # Importa a classe PedidoService
from services.entrega_service import EntregaService # Importa a classe EntregaService
from util.validador import Validador # Importa a classe Validador do pacote validador.py
from util.formatador import Formatador # Importa a classe Formatador do pacote formatador.py
from util.menu import Menu # Importa a classe Menu

def main():
    # Instanciando os serviços que vão gerenciar os dados
    s_cliente = ClienteService()
    s_pedido = PedidoService()
    s_entrega = EntregaService()

    # Esse laço de repetição vai ser interrompido quando o usuário digitar 0 no menu principal para sair do sistema
    while True:
        Menu.limpar_tela() # Chama limpar tela
        opcao = Menu.principal() # Chama o menu principal

        # Menu dos clientes
        if opcao == "1":
            # Esse laço de repetição vai ser interrompido quando o usuário digitar 0 no menu de clientes para voltar ao menu principal
            while True:
                Menu.limpar_tela() # Chama limpar tela
                op_cli = Menu.clientes()
                
                if op_cli == "1": # Opção para cadastro de clientes
                    nome = input("Nome: ")
                    cpf = input("CPF: ")
                    tel = input("Telefone: ")
                    end = input("Endereço: ")
                    
                    # Validação para evitar campos nulos
                    if nome and cpf:
                        s_cliente.cadastrar_cliente(nome, cpf, tel, end)
                        print("Cliente cadastrado com sucesso!")
                    else:
                        print("Nome e CPF são obrigatórios.")
                    input("\nPressione Enter para voltar")

                elif op_cli == "2": # Opção para listar clientes
                    print("\n--- Lista de Clientes ---")
                    for c in s_cliente.listar_todos():
                        print(c) # Chama automaticamente o __str__ de Cliente
                    input("\nPressione Enter para voltar")

                elif op_cli == "3": # Opção para buscar por um cliente
                    cpf = input("Digite o CPF para busca: ")
                    cli = s_cliente.buscar_por_cpf(cpf)
                    if cli:
                        print(f"\nEncontrado: {cli}")
                    else:
                        print("Cliente não cadastrado.")
                    input("\nPressione Enter para voltar")

                elif op_cli == "0": # Opção para voltar pro menu principal
                    break

        # Menu de Entregadores
        elif opcao == "2":
            # Esse laço de repetição vai ser interrompido quando o usuário digitar 0 no menu de entregadores para voltar ao menu principal
            while True:
                Menu.limpar_tela() # chama lipar tela
                op_ent = Menu.entregadores() # chama o menu de entregadores

                if op_ent == "1": # Opção para cadastrar um entregador
                    nome = input("Nome do Entregador: ")
                    cpf = input("CPF: ")
                    tel = input("Telefone: ")
                    veiculo = input("Veículo : ")
                    cnh = input("Número da CNH: ")

                    if nome and cpf and cnh:
                        # Chamando o método dentro de entrega_service
                        s_entrega.cadastrar_entregador(nome, cpf, tel, veiculo, cnh)
                        print("Entregador cadastrado com sucesso!")
                    else:
                        print("Nome, CPF e CNH são obrigatórios.")
                    input("\nPressione Enter para continuar...")

                elif op_ent == "2": # Opção para listar os entregadores
                    print("\n--- Lista de Entregadores ---")
                    # Buscando a lista de dentro de entrega_service
                    entregadores = s_entrega.listar_todos_entregadores()
                    if not entregadores:
                        print("Nenhum entregador cadastrado.")
                    for e in entregadores:
                        print(f"{e.nome} | CPF: {e.cpf} | Veículo: {e.veiculo} | CNH: {e.cnh}")
                    input("\nPressione Enter para continuar...")

                elif op_ent == "0": # Voltar ao menu principal
                    break
        
        # Menu dos pedidos
        elif opcao == "3":
            # Esse laço de repetição vai ser interrompido quando o usuário digitar 0 no menu de pedidos para voltar ao menu principal
            while True:
                Menu.limpar_tela()
                op_ped = Menu.pedidos()

                if op_ped == "1": # Opção de criar pedidos
                    cpf = input("CPF do Cliente: ")
                    cli = s_cliente.buscar_por_cpf(cpf)
                    
                    # Um pedido precisa obrigatoriamente de um cliente real cadastrado
                    if not cli:
                        print("Cliente não localizado! Cadastre o cliente primeiro.")
                        input("\nPressione Enter para voltar")
                        continue

                    cod = input("Código do Pedido: ")
                    # utilizando o validador
                    peso = Validador.validar_numero_positivo(input("Peso (kg): "))
                    dist = Validador.validar_numero_positivo(input("Distância (km): "))
                    
                    if peso == 0.0 or dist == 0.0:
                        print("Inválido! Peso e Distância precisam ser números maiores que zero!")
                        input("\nPressione Enter para voltar")
                        continue
                    
                    print("1- Comum | 2- Expressa | 3- Premium")
                    t_opcao = input("Tipo de Entrega: ")
                    
                    tipo_envio = EntregaService.criar_tipo_entrega(t_opcao)

                    if tipo_envio:
                        pedido = s_pedido.criar_pedido(cod, cli, peso, dist, tipo_envio)
                        # utilizando o formatador
                        frete_formatado = Formatador.formatar_moeda(pedido.valor_frete)
                        print(f"Pedido criado! Valor do Frete calculado: {frete_formatado}")
                    else:
                        print("Tipo de entrega inválido.")
                    input("\nPressione Enter para voltar")

                elif op_ped == "2": # Opção de listar pedidos
                    print("\n--- Lista de Pedidos ---")
                    for p in s_pedido.listar_todos():
                        # utilizando o formatador
                        frete_formatado = Formatador.formatar_moeda(p.valor_frete)
                        print(f"Cód: {p.codigo} | Cliente: {p.cliente.nome} | Frete: {frete_formatado} | Status: [{p.status}]")
                    input("\nPressione Enter para voltar")

                elif op_ped == "3": # Opção de atualizar status
                    cod = input("Digite o código do pedido: ")
                    p = s_pedido.buscar_por_codigo(cod)
                    
                    if p:
                        print(f"Status atual: {p.status}")
                        print("1- Em preparação | 2- Saiu para entrega | 3- Entregue | 4- Cancelado")
                        st = input("Escolha o novo status: ")
                        
                        # Dicionário de de-para para mapear a string correta
                        status_opcoes = {"1": "Em preparação", "2": "Saiu para entrega", "3": "Entregue", "4": "Cancelado"}
                        
                        if st in status_opcoes:
                            p.status = status_opcoes[st] # Atualiza via propriedade setter
                            print("Status atualizado com sucesso!")
                        else:
                            print("Opção inválida.")
                    else:
                        print("Pedido não encontrado.")
                    input("\nPressione Enter para voltar")

                elif op_ped == "0": # Opção para voltar pro menu principal
                    break

        elif opcao == "0": # Sair dos sistema
            print("Saindo do sistema...")
            break

if __name__ == "__main__":
    main()