num = int(input("Digite um número inteiro: "))
match num:
    case 1:
        print("número 01")
    case 2:
        print("número 02")
    case 3:
        print("número 03")
    case _:
        print("Outro número")