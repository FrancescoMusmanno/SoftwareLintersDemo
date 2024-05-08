# In base a una condizione stampa un colore
def definisci_colore():
    condizione = True
    if condizione:
        print("rosso")
    else:
        print("blu")


# In base a un parametro stampa un numero
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
