cor= str(input("Digite uma cor: "))
match cor:
    case "vermelho":
        print("Cor vermelha")
    case "azul":
        print("Azul")
    case "verde":
        print("Cor verde")
    case _:
        print("Cor desconhecida")
