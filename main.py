def programa_principal():
    run = 1

    while run == 1:

        opc = input("(A)dicionar Produto\n Modulo de (V)enda\n (R)emover Produto\n a(T)ualizar\n_")

        if opc == "A":
            # TODO Adição de produtos
            pass
        elif opc == "V":
            # TODO Venda de produtos
            pass
        elif opc == "R":
            # TODO Remoção de produtos
            pass
        elif opc == "T":
            # TODO Atualização de produtos
            pass
        else:
            print("Opção inválida, finalizando o programa")
            run = -1


if __name__ == "__main__":
    programa_principal()
