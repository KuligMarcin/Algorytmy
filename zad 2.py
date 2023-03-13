n = int(input("Podaj liczbe elementow ciagu: "))
if n>0:
    i = 0
    ile_u = 0
    for i in range(n):
        ai = int(input("Podaj element ciagu "))
        if ai<0:
            ile_u += 1
        else:
            i += 1
    print("Ilosc liczb ujemnych ",ile_u )
else:
    print("Liczba musi byc wieksza od 0  ")
