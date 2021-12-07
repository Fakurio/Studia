#program sprawdza czy wprowadzone liczby spełnią sudoku
rozmiar = 9

def wczytaj(sudoku):
    for i in range(rozmiar):
        n = input("Podaj cały rząd: ")
        n = ",".join(n)
        n = n.split(",")
        if len(n)!=9:
            return 1
        k = 0
        for j in range(rozmiar):
            if int(n[k]) > 9 or int(n[k]) < 1:
                return 1
            sudoku[i][j] = int(n[k])
            k += 1
         
def check(sudoku):
    numbers_count_row = [0 for i in range(rozmiar)]
    numbers_count_col = [0 for i in range(rozmiar)]
    numbers_count_square = [0 for i in range(rozmiar)]
    flag = 0

    for i in range(rozmiar):    #sprawdzenie czy w każdym wierszu i kolumnie znajdują się cyfry 1-9
        for j in range(rozmiar):
            numbers_count_row[sudoku[i][j]-1] += 1
            numbers_count_col[sudoku[j][i]-1] += 1
        if 0 in numbers_count_row or 0 in numbers_count_col:
            flag = 1
            break

    for i in range(3,9,3):  #sprawdzenie czy w każdym kwadracie 3x3 znajdują się cyfry 1-9
        for j in range(i):
            for k in range(i):
                numbers_count_square[sudoku[j][k]-1] += 1
        if 0 in numbers_count_square:
            flag = 1
            break

    if flag:
        print("Złe sudoku")
    else:
        print("Dobre sudoku")

sudoku = [[0 for i in range(rozmiar)] for i in range(rozmiar)]
if wczytaj(sudoku):
    print("Błędne dane")
else:
    check(sudoku)