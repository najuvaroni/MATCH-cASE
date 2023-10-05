dia = str(input("Digite um dia da semana"))
match dia:
    case ("segunda"| "terça"| "quarta"| "quinta"| "sexta"):
           print(f"{dia} é dia útil")
    case("sábado"|"domingo"):
           print(f"{dia} é final de semana:  ")
    case _:
        print("não identificado")