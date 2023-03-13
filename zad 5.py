L1 = [[5,2,3],[22,5,6]]
for i in L1:
    najmniejsza = min(i)
    z = i.index(najmniejsza)
    i[0], i[z] = i[z], i[0]
print("Tablica po zmianach",L1)
