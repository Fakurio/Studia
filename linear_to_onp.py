def to_onp(wyrazenie):
    operatory = {
        '+' : 1, 
        '-' : 1, 
        '*' : 2, 
        '/' : 2,
        '^' : 3,
        'sqrt': 3,
        'sin' : 4,
        'log' : 4
    }
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
                wynik += stos.pop() + " "
                i -= 1
            stos.pop()
        else:
            i = len(stos)-1
            while i>-1 and stos[i] in operatory.keys():
                if operatory[stos[i]] >= operatory[znak]:
                    wynik += stos.pop() + " "
                i -= 1
            stos.append(znak)
    i = len(stos)-1
    while stos and i>-1:
        wynik += stos.pop() + " "
        i -= 1
    return wynik

print(to_onp("( ( sin ( 1 + 5 * 9 - 2 ) * 1 ^ ( - ( 1 / 8 ) ) ) ) / ( sqrt 7 + log 6 1 ) * ( 3 sqrt ( 1 / 2 ) )"))
#print(to_onp("( ( 1 + 3 ) * 2 - 12 ) / 4"))
