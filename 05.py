login = str(input("Digite o seu login: "))
senha = str(input("Digite a sua senha: "))
match (login, senha):
    case ("admin", "admin_pass"):
        print("Logado com sucesso")
    case ("user", "user_pass"):
        print("Logado com sucesso")
    case ("guest", _):
        print("Logado com sucesso")
    case _:
        print("Erro")