def definisci_colore():
    condizione = True
    if condizione:
        print("rosso")
    else:
        print("blu")


def numero_colore(parametro):
    risultato = 0
    try:
        print("rosso")
    except ValueError:
        pass
    else:
        if parametro:
            raise ValueError()
    finally:
        if parametro:
            raise
        else:
            risultato = 1
    print(risultato)


definisci_colore()
numero_colore(True)
