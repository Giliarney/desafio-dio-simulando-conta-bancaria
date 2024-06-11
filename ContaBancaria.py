import getpass
import time

def cadastrar():
    #Lista para armanzenar os cadastros dos usuarios
    usuario = {}
    AGENCIA = "067-8"
    CONTA = 1000

    nome = str(input("Digite seu nome: "))
    sobrenome = str(input("Digite seu sobrenome: "))
    senha_usuario = str(input("Escolha uma senha: "))
    CONTA = CONTA + 1

    #Cocatenando os valor para formar o nome completo do usuario
    nomeCompleto = nome + " " + sobrenome
    
    #Inserindo o cadastro na lista "usuario"
    usuario['nome_completo'] = nomeCompleto
    usuario['agencia'] = AGENCIA
    usuario['conta'] = CONTA
    usuario['saldo'] = 0.0
    usuario['senha'] = senha_usuario

    return usuario

def logar(usuario):
    #limitando o numero de tentativas a acesso a conta
    contador = 0
    while contador < 3:
        agencia = input("Informe o número da agência: ")
        conta = int(input("Informe o número da conta: "))
        senha = getpass.getpass("Digite sua senha: ")

        if usuario['agencia'] == agencia and usuario['conta'] == conta and usuario['senha'] == senha:
            print("Login bem-sucedido!\n")
            pagina_inicial_banco()
        else:
            contador += 1
            if contador == 3:
                print("\n Sinto muito você ultrapassou o limite de erros e sua conta foi bloqueada por questões de segurança, vá até a agência mais próxima para solicitar o desbloqueio.")
                break
            print('\nInformações incorretas. Verifique as informações digitadas e tente novamente.\n')
            continue
      
def pagina_inicial_banco():
#funcao da paginal inicial quando loga no site
    print('''
    1 - Sacar
    2 - Depositar
    3 - Ver Saldo
    4 - Sair
    ''')
    #loop para solicitar o usuario preencher novamente caso erre as opcoes aceitas
    while True:
        escolhaLogin = int(input('Por favor escolha uma das opções acima: '))

        if escolhaLogin == 1:
            sacar(usuario)
        elif escolhaLogin == 2:
            depositar(usuario)
        elif escolhaLogin == 3:
                print(f'O seu saldo atual é: {usuario["saldo"]}')
        elif escolhaLogin == 4:
            print(f'Até a próxima {usuario["nome_completo"]}')
            break  
        else:
            print('Opção inválida, por favor selecione uma das opções fornecidas!')
        
def depositar(usuario):
    #funcao para depositar dinheiro
    deposito = float(input('Por favor digite o valor do depósito: '))

    usuario['saldo'] += deposito

    print(f'Depósito de R${deposito:.2f} realizado com sucesso.')

    #loop para que o usuario informe se quer voltar para tela inicial do banco e executar outra operacao
    while True:
        resposta = input("Voltar para a tela inicial? (Sim/Nao): ")
        if resposta.lower() == "sim":
            logar(usuario)
        elif resposta.lower() == "nao": 
            print(f"Até a próxima {usuario['nome_completo'[0:1]]}")
        else: 
            print("Por favor selecione uma opção válida!")

def sacar(usuario):
    #funcao para sacar dinheiro
    saque = float(input('Por favor digite o valor do saque: '))
    #verificando se o valor do saque e maior que o do saldo disponivel
    if saque <= usuario['saldo']:
        usuario['saldo'] -= saque
        print(f'Saque de R${saque:.2f} realizado com sucesso.')
    else:
        print('Saldo insuficiente.')

    #loop para que o usuario informe se quer voltar para tela inicial do banco e executar outra operacao
    while True:
        resposta = input("Voltar para a tela inicial? (Sim/Nao): ")
        if resposta.lower() == "sim":
            logar(usuario)
        elif resposta.lower() == "nao":
            print(f"Até a próxima {usuario['nome_completo'[0:1]]}")
        else:
            print("Por favor selecione uma opção válida!")

#=========================================== Acima são as funções ======================================================

#definindo que o banco ainda nao tem clientes
usuario = None

#loop para caso o usuario digite algum opcao nao aceita pelo sistema, ele solicita que o usuario que digite novamente
while True:
    idade_do_usuario = int(input("Por favor informe sua idade: "))
    if idade_do_usuario < 18:
        print("Você não tem idade suficiente para criar uma conta")
        break
    else:
        print("Redirecionando para página incial...")
        time.sleep(2)
    print('\nSeja Bem-Vindo ao banco DIO!')
    print('============================')
    print('''
    1 - Login
    2 - Cadastrar
        ''')
    escolhaInicio = int(input('Por favor escolha uma das opções acima: '))
    if escolhaInicio == 1:
        if usuario:
            logar(usuario)
            break
        else:
            print('Nenhum usuário cadastrado. Por favor, cadastre-se primeiro.\n')
    elif escolhaInicio == 2:
        usuario = cadastrar()
        print(f'''Usuário cadastrado com sucesso! 
Sua agencia é: {usuario["agencia"]}
Sua conta é: {usuario["conta"]}
            ''')
            
        #depois do cadastro solicita ao usuario se ele quer voltar a tela inicial para que possa efetuar o login
        resposta = input("Voltar para a tela inicial? (Sim/Nao): ")
        if resposta.lower() == "sim":
            continue
        elif resposta.lower() == "nao":
            print(f"\nAté a próxima, {usuario['nome_completo'][0:1]}\n")
            break
        else:
            print("Opção inválida, por favor responda 'Sim' ou 'Nao'.")
    else:
        print("Opção inválida, escolha uma das opções fornecidas!\n")
