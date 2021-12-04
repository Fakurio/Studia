def to_onp(wyrazenie):
    operatory = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}
    stos = []
    wynik = ""
    wyrazenie = wyrazenie.split()
    for znak in wyrazenie:
        if znak.isdigit():
            wynik += znak + " "
        elif znak == "(":
            stos.append(znak)
        elif znak == ")":
            i = len(stos)-1
            while stos[i]!="(" and i>-1:
                wynik += stos[i] + " "
                del stos[i]
                i -= 1
            del stos[i]
        else:
            i = len(stos)-1
            while i>-1 and stos[i] in ("*/+-"):
                if operatory[stos[i]] >= operatory[znak]:
                    wynik += stos[i] + " "
                    del stos[i]
                i -= 1
            stos.append(znak)
    i = len(stos)-1
    while stos and i>-1:
        wynik += stos[i] + " "
        i -= 1
    return wynik

print(to_onp("( ( 2 + 7 ) / 3 + ( 14 − 3 ) * 4 ) / 2"))
