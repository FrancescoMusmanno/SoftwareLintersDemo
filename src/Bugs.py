# Stampa il risultato di 32+10
def stampa_42():
    number = "32"
    total = number + 10
    print(total)


# Calcola il MDC di due numeri
def calcola_mcd(a, b=42):
    while b:
        a, b = b, a % b
    print(a)


# Stampa il risultato di 32+10
stampa_42()

# Stampa il MCD di 21 e 42
calcola_mcd(2, 21, 42)
# Stampa il MCD di 2 e 42, senza specificare il 42
calcola_mcd()
