from math import sin, log, radians
def onp(wyrazenie):
    stos = []
    wyrazenie = wyrazenie.split()
    for znak in wyrazenie:
        if znak.isdigit():
            stos.append(znak)
        else:
            b = float(stos.pop())
            try:    
                a = float(stos.pop())
            except:
                a = 1
            if znak == "+":
                stos.append(a+b)
            if znak == "-":
                stos.append(a-b)
            if znak == "*":
                stos.append(a*b)
            if znak == "/":
                stos.append(a/b)
            if znak == "^":
                stos.append(a**b)
            if znak == "sqrt":
                stos.append(b**(1/float(a*2)))
            if znak == "sin":
                stos.append(sin(radians(b)))
            if znak == "log":
                stos.append(log(b,a*10))
    wynik = float(stos[0])  
    return wynik

print(onp("1 5 9 * + 2 - sin 1 1 8 / - ^ * 7 sqrt 6 1 log + / 3 1 2 / sqrt *"))