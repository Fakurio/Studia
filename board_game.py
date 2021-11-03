from random import randint

def rzut():
    a = randint(1,4)
    return a

def ruch(pozycja,p2,nr,nr_2):
    pozycja = pozycja + rzut()
    if pozycja == a:
        print("\nGracz nr"+str(nr)+" przesuwa sie o 5 pól do przodu")
        pozycja += 5
    if pozycja == b:
        tura = randint(1,3)
        print("\nGracz nr"+str(nr)+" czeka tyle tur: "+str(tura))
        for i in range(tura):
            ruch(p2,pozycja,nr_2,nr)
    if pozycja == c:
        print("\nGracz nr"+str(nr)+" wraca na Start")
        pozycja = 0
    if pozycja == e:
        print("\nGracz nr"+str(nr)+" wpada w pułapkę")
        while rzut()!=4:
            ruch(p2,pozycja,nr_2,nr)

    return pozycja, p2
    

plansza = [i for i in range(20)]
a = plansza[2]
b = plansza[9]
c = plansza[17]
d = plansza[19]
e = plansza[13]

g1_pozycja = 0
g2_pozycja = 0

while True:
    g1_pozycja, g2_pozycja = ruch(g1_pozycja,g2_pozycja,1,2)
    print("G1 pozycja: "+str(g1_pozycja),end="\t")
    if g1_pozycja >= 19:
        print("\nGracz 1 wygrał")
        break
    g2_pozycja, g1_pozycja = ruch(g2_pozycja,g1_pozycja,2,1)
    print("G2 pozycja: "+str(g2_pozycja))
    if g2_pozycja >= 19:
        print("\nGracz 2 wygrał")
        break

    # p2_position, p1_position = movement(p2_position,p1_position,2,1)
    # print("P2 position: "+str(p2_position))
    # if p2_position >= 19:
    #     print("\nGracz 2 wygrał")
    #     break