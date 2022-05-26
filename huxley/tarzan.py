vidaInimigo = int(input())
vigor = int(input())
arma = input().strip().lower()
if arma == "pedra":
    while vigor >= 13:
        vidaInimigo -=15
        vigor -=13
        if vigor == 0:
            print("Tarzan nao foi capaz de derrotar o invasor... Ele foi capturado")
            break
        if vidaInimigo <= 0:
            print("Tarzan venceu o invasor e o expulsou de sua floresta")
            break
    if vigor <13 and vidaInimigo > 0:
        print("Tarzan nao foi capaz de derrotar o invasor... Ele foi capturado")
elif arma == "graveto":
    while vigor >= 8:
        vidaInimigo -=10
        vigor -=8
        if vigor == 0:
            print("Tarzan nao foi capaz de derrotar o invasor... Ele foi capturado")
            break
        if vidaInimigo <= 0:
            print("Tarzan venceu o invasor e o expulsou de sua floresta")
            break
    if vigor < 8 and vidaInimigo > 0:
        print("Tarzan nao foi capaz de derrotar o invasor... Ele foi capturado")
else:
    print("Tarzan nao consegue lutar sem armas... Ele foi capturado")