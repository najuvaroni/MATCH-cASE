animal = str(input("Digite um animal: "))
match animal:
    case ("vaca"|"galinha"|"ovelha"):
           print(f" possui {animal} na fazendinha ")
    case _:
        print("Animal desconhecido")
