Dana jest plansza postaci:
..a......b...e...c.d
01234567890123456789

gdzie:
a) idziesz pięć pól do przodu,
b) czekasz od 1 do 3 tur,
c) wracasz na start,
d) wygrywasz grę,
e) wpadłeś w pułapkę i tracisz turę. W kolejnych turach musisz uzyskać na kostce 
cztery oczka, aby wyrwać się z pułapki – w przeciwnym razie pozostajesz dalej w 
pułapce.

Implementacja:
- w każdej turze rzucić kostką czterościenną (liczba od 1 do 4 – można zmienić 
  zasady w przypadku wydłużenia mapy) i przenieść gracza o wybraną liczbę 
  pozycji,
- podjąć akcję stosowną do pola, na którym znajduje się gracz,
- sprawdzić warunki wygranej,
- wyświetlić informacje o wygranej gracza o danym numerze (bądź po prostu 
  gracza w przypadku gry jednoosobowej
