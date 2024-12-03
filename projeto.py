import re

# Lista para armazenar os contatos
contatos = []

# Função para validar telefone e formatá-lo para o padrão desejado
def formatar_telefone(telefone):
    # Remover todos os caracteres que não são números
    telefone = re.sub(r'\D', '', telefone)
    
    # Verificar se o telefone tem a quantidade correta de números
    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    else:
        return None

# Função para validar e-mail
def validar_email(email):
    return bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email))

# Função para adicionar um contato
def adicionar_contato():
    nome = input("Digite o nome do contato: ").strip()
    while not nome:
        print("Nome não pode estar em branco.")
        nome = input("Digite o nome do contato: ").strip()

    telefone = input("Digite o telefone (DDD + NÚMERO): ").strip()
    telefone_formatado = formatar_telefone(telefone)
    while not telefone_formatado:
        print("Telefone inválido. Por favor, insira um telefone válido (ex: 62999999999 ou 62 99999 9999).")
        telefone = input("Digite o telefone (DDD + NÚMERO): ").strip()
        telefone_formatado = formatar_telefone(telefone)

    email = input("Digite o e-mail: ").strip()
    while not validar_email(email):
        print("E-mail inválido.")
        email = input("Digite o e-mail: ").strip()

    contato = {'nome': nome, 'telefone': telefone_formatado, 'email': email}
    contatos.append(contato)
    print("Contato adicionado com sucesso!")

# Função para listar todos os contatos
def listar_contatos():
    if not contatos:
        print("Nenhum contato encontrado.")
        return
    for idx, contato in enumerate(contatos, 1):
        print(f"{idx}. Nome: {contato['nome']} | Telefone: {contato['telefone']} | E-mail: {contato['email']}")

# Função para pesquisar um contato por nome
def pesquisar_contato():
    nome_pesquisa = input("Digite o nome a ser pesquisado: ").strip().lower()
    encontrados = [contato for contato in contatos if nome_pesquisa in contato['nome'].lower()]
    
    if not encontrados:
        print("Nenhum contato encontrado com esse nome.")
        return
    
    for idx, contato in enumerate(encontrados, 1):
        print(f"{idx}. Nome: {contato['nome']} | Telefone: {contato['telefone']} | E-mail: {contato['email']}")

# Função para editar um contato existente
def editar_contato():
    listar_contatos()
    if not contatos:
        return
    
    try:
        indice = int(input("Escolha o número do contato que deseja editar: ")) - 1
        if indice < 0 or indice >= len(contatos):
            print("Contato não encontrado.")
            return
        
        contato = contatos[indice]
        print(f"Editando contato: {contato['nome']}")
        
        nome = input(f"Novo nome (atual: {contato['nome']}): ").strip()
        telefone = input(f"Novo telefone (atual: {contato['telefone']}): ").strip()
        telefone_formatado = formatar_telefone(telefone)
        while not telefone_formatado:
            print("Telefone inválido. Por favor, insira no formato correto.")
            telefone = input("Digite o telefone: ").strip()
            telefone_formatado = formatar_telefone(telefone)
        email = input(f"Novo e-mail (atual: {contato['email']}): ").strip()
        while not validar_email(email):
            print("E-mail inválido.")
            email = input("Digite o e-mail: ").strip()
        
        contato['nome'] = nome if nome else contato['nome']
        contato['telefone'] = telefone_formatado if telefone_formatado else contato['telefone']
        contato['email'] = email if email else contato['email']
        print("Contato atualizado com sucesso!")
    
    except ValueError:
        print("Opção inválida.")

# Função para remover um contato
def remover_contato():
    listar_contatos()
    if not contatos:
        return
    
    try:
        indice = int(input("Escolha o número do contato que deseja remover: ")) - 1
        if indice < 0 or indice >= len(contatos):
            print("Contato não encontrado.")
            return
        
        del contatos[indice]
        print("Contato removido com sucesso!")
    
    except ValueError:
        print("Opção inválida.")

# Função para exibir o menu
def exibir_menu():
    while True:
        print("\nGerenciador de Contatos")
        print("1 - Adicionar contato")
        print("2 - Listar todos os contatos")
        print("3 - Pesquisar contato por nome")
        print("4 - Editar contato existente")
        print("5 - Remover contato")
        print("6 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            pesquisar_contato()
        elif opcao == '4':
            editar_contato()
        elif opcao == '5':
            remover_contato()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
if __name__ == "__main__":
    exibir_menu()
