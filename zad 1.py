import math

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))
if a!=0:
    delta = b*b-4*a*c
else:
    print("to nie moze byc rownanie kwadratowe")
if delta>0:
    x1 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)
    print("x1 =",x1)
    print("x2 =",x2)
elif delta==0:
    x1 = -b/(2*a)
    print("x1 = ",round(x1,2))
else:
    print("Brak rozwiazan")
