import os #biblioteca para interagir com o sistema operacional
import platform #módulo para verificação do sistema operacional

AGENDA = {}


def mostrar_contatos():
    if AGENDA:
        limpar_tela()
        for contato in AGENDA:
            print('Nome:', contato)
            print('Telefone:',AGENDA[contato]['telefone'])
            print('E-mail:',AGENDA[contato]['email'])
            print('Endereço:',AGENDA[contato]['endereco'])
            print('')
    else:             
        print('Agenda vazia')


def buscar_contato(contato):
    try:
        limpar_tela()
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('E-mail:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
    except KeyError as error:
        limpar_tela()
        print(f'O contato {contato} não existe')
    except Exception as error:
        limpar_tela()
        print('Ocorreu um erro inesperado')
        print(error)


def ler_detalhes_contato():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereço do contato: ')
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):     
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print(f'Contato {contato} adicionado/editado com sucesso')
    # print("Contato {} adicionado com sucesso" .format(contato))
   

def excluir_contato(contato):
    try:
        limpar_tela()
        AGENDA.pop(contato)
        salvar()
        print(f'Contato {contato} excluido com sucesso!')       
    except KeyError as error:
        limpar_tela()
        print(f'O contato {contato} não existe')
    except Exception as error:
        limpar_tela()
        print('Ocorreu um erro inesperado')
        print(error)


def exportar_contatos(nome_do_arquivo):
    try:
        limpar_tela()
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato}, {telefone}, {email}, {endereco},\n')
        print('Agenda exportada com sucesso!')
    except Exception as error:
        limpar_tela()
        print('Algum erro ocorreu ao exportar contatos')
        print(error)


def importar_contatos(nome_do_arquivo):
    try:
        limpar_tela()
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.split(',')
                if len(detalhes) >= 4:
                    nome = detalhes[0]
                    telefone = detalhes[1]
                    email = detalhes[2]
                    endereco = detalhes[3]

                    AGENDA[nome] = {
                        'telefone': telefone,
                        'email': email,
                        'endereco': endereco,
                    }
                else:
                    print(f'A linha não contém informações suficientes: {linha}')
    except FileNotFoundError:
        limpar_tela()
        print('Arquivo não encontrado')
    except Exception as error:
        limpar_tela()
        print('Algum erro inesperado ocorreu')
        print(error)


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        limpar_tela()
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.split(',')
                
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                'telefone': telefone,
                'email': email,
                'endereco': endereco,
                }
        print(f'Database carregado com sucesso! {len(AGENDA)} contatos no total.')        
    except FileNotFoundError:
        limpar_tela()
        print('Arquivo não encontrado')
    except Exception as error:
        limpar_tela()
        print('Algum erro inesperado ocorreu')
        print(error)


def limpar_tela():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
    else:
        print("Sistema operacional não suportado.")


def imprimir_menu():
    print('---------------------------------------')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Adicionar contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos CSV')
    print('0 - Sair do programa')
    print('---------------------------------------')
    

# INÍCIO DO PROGRAMA
carregar()
while True:
    imprimir_menu()

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato que deseja buscar: ')
        buscar_contato(contato)
    elif opcao == '3':
        limpar_tela()
        contato = input('Digite o nome do contato para adicionar: ')

        try:
            AGENDA[contato]
            print('Contato já existente')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        limpar_tela()
        contato = input('Digite o nome do contato para editar: ')

        try:
            existente = AGENDA[contato]
            limpar_tela()
            print('Editando contato:', contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print(f'O contato {contato} não existe')

    elif opcao == '5':
        contato = input('Digite o nome do contato que deseja excluir: ')
        excluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        print('Saindo do programa')
        break
    else:
        print('Opção inválida')