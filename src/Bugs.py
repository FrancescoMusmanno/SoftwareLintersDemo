def aggiungi_42(x):
    number = "42"
    total = number + x
    print(total)


def calcola_mcd(a, b=42):
    while b:
        a, b = b, a % b
    print(a)


# Stampare il risultato di 0+42
aggiungi_42(0)

# Stampare il MCD di 21 e 42
calcola_mcd(2, 21, 42)
# Stampare il MCD di 2 e 42, senza specificare il 42
calcola_mcd()
