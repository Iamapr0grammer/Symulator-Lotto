from random import randint
import re

#informacja czy program sam wylosował liczby, czy wybrał je gracz
samolosowanie = 0

#zmienne pomocnicze:
v1 = 50
v2 = 50
v3 = 50
v4 = 50
v5 = 50
v6 = 50

# wzór, upewniający się, że użytkownik wpisujący inne znaki niż liczby nie posypie programu:
wzor = r"[1234567890]"

#pobieranie imienia od użytkownieka:
imie = input("Witaj w symulatorze gry w Lotto! Jak masz na imię? ")

# płeć użytkownika:
plec = 0

#sprawdzanie płci użytkownika:
if re.match("^[A-Za-z]*a$", imie):
    plec = 1

raport = "Podaj swoją pierwszą liczbę do lotto w zakresie od 1 do 49: "

c3 = input("Czy chcesz samodzielnie wybrać liczby? jeśli tak, wpisz literkę t, w przeciwnym wypadku wpisz cokolwiek, a program wylosuje liczby za Ciebie ")

#pobieranie 6 cyfr od użytkownika:
if c3 == ("t") or c3 == ("T"):
    while int(v1) < 1 or int(v1) > 49:
        v1 = input(raport)
        rent = (re.findall(wzor, v1))
        if len(rent) == 1:
            rent1 = rent[0]
            v1 = int(rent1)
        if len(rent) == 2:
            rent1 = rent[0] + rent[1]
            v1 = int(rent1)
        if len(rent) > 2 or len(rent) == 0:
            v1 = 50

    raport = "Podaj swoją drugą liczbę do lotto w zakresie od 1 do 49: "

    while int(v2) < 1 or int(v2) > 49 or int(v2) == int(v1):
        v2 = input(raport)
        rent = (re.findall(wzor, v2))
        if len(rent) == 1:
            rent1 = rent[0]
            v2 = int(rent1)
        if len(rent) == 2:
            rent1 = rent[0] + rent[1]
            v2 = int(rent1)
        if len(rent) > 2 or len(rent) == 0:
                v2 = 50
        if v2 == v1:
            raport = "Wybrane liczby nie mogą się powtarzać: "
        if v2 != v1:
            raport = "Podaj swoją trzecią liczbę do lotto w zakresie od 1 do 49: "

    raport = "Podaj swoją trzecią liczbę do lotto w zakresie od 1 do 49: "

    while int(v3) < 1 or int(v3) > 49 or int(v3) == int(v2) or int(v3) == int(v1):
        v3 = input(raport)
        rent = (re.findall(wzor, v3))
        if len(rent) == 1:
            rent1 = rent[0]
        if len(rent) == 2:
            rent1 = rent[0] + rent[1]
        v3 = int(rent1)
        if len(rent) > 2 or len(rent) == 0:
            v3 = 50
        if v3 == v1 or v3 == v2:
            raport = "Wybrane liczby nie mogą się powtarzać: "
        if v3 != v1 and v3 != v2:
            raport = "Podaj swoją trzecią liczbę do lotto w zakresie od 1 do 49: "

    raport = "Podaj swoją czwartą liczbę do lotto w zakresie od 1 do 49: "

    while int(v4) < 1 or int(v4) > 49 or int(v4) == int(v1) or int(v4) == int(v2) or int(v4) == int(v3):
        v4 = input(raport)
        rent = (re.findall(wzor, v4))
        if len(rent) == 1:
            rent1 = rent[0]
        if len(rent) == 2:
            rent1 = rent[0] + rent[1]
        v4 = int(rent1)
        if len(rent) > 2 or len(rent) == 0:
            v4 = 50
        if v4 == v1 or v4 == v2 or v4 == v3:
            raport = "Wybrane liczby nie mogą się powtarzać: "
        if v4 != v1 and v4 != v2 and v4 != v3:
            raport = "Podaj swoją czwartą liczbę do lotto w zakresie od 1 do 49: "

    raport = "Podaj swoją piątą liczbę do lotto w zakresie od 1 do 49: "

    while int(v5) < 1 or int(v5) > 49 or int(v5) == int(v1) or int(v5) == int(v2) or int(v5) == int(v3) or int(v5) == int(v4):
        v5 = input(raport)
        rent = (re.findall(wzor, v5))
        if len(rent) == 1:
            rent1 = rent[0]
        if len(rent) == 2:
            rent1 = rent[0] + rent[1]
        v5 = int(rent1)
        if len(rent) > 2 or len(rent) == 0:
            v5 = 50
        if v5 == v1 or v5 == v2 or v5 == v3 or v5 == v4:
            raport = "Wybrane liczby nie mogą się powtarzać: "
        if v5 != v1 and v5 != v2 and v5 != v3 and v5 != v4:
            raport = "Podaj swoją piątą liczbę do lotto w zakresie od 1 do 49: "

    raport = "Podaj swoją szóstą liczbę do lotto w zakresie od 1 do 49: "

    while int(v6) < 1 or int(v6) > 49 or int(v6) == int(v1) or int(v6) == int(v2) or int(v6) == int(v3) or int(v6) == int(v4) or int(v6) == int(v5):
        v6 = input(raport)
        rent = (re.findall(wzor, v6))
        if len(rent) == 1:
            rent1 = rent[0]
        if len(rent) == 2:
            rent1 = rent[0] + rent[1]
        v6 = int(rent1)
        if len(rent) > 2 or len(rent) == 0:
            v6 = 50
        if v6 == v1 or v6 == v2 or v6 == v3 or v6 == v4 or v6 == v5:
            raport = "Wybrane liczby nie mogą się powtarzać: "
        if v6 == v1 and v6 == v2 and v6 == v3 and v6 == v4 and v6 == v5:
            raport = "Podaj swoją szóstą liczbę do lotto w zakresie od 1 do 49: "

else:
    # program losuje liczby samodzielnie, pamiętając, że liczby nie mogą się powtarzać:
    v1 = randint(1,49)
    v2 = randint(1,49)
    while v2 == v1:
        v2 = randint(1, 49)
    v3 = randint(1,49)
    while v3 == v2 or v3 == v1:
        v3 = randint(1, 49)
    v4 = randint(1,49)
    while v4 == v3 or v4 == v2 or v4 == v1:
        v4 = randint(1, 49)
    v5 = randint(1,49)
    while v5 == v4 or v5 == v3 or v5 == v2 or v5 == v1:
        v5 = randint(1, 49)
    v6 = randint(1,49)
    while v6 == v5 or v6 == v4 or v6 == v3 or v6 == v2 or v6 == v1:
        v6 = randint(1, 49)
    # oraz zapamiętuje, że były wylosowane:
    samolosowanie = 1


# licznik wysłanych losowań lotto
timer = 0

# zmienne pomocniczne, które będą miały zmienną wartość wylosowanych przez lotto liczb w różnych edycjach:
b1 = 1
b2 = 2
b3 = 3
b4 = 4
b5 = 5
b6 = 6

# zmienna, która będzie liczyć ile liczb się zgadza, gdy zmienna (gg) ma wartość 6, oznacza to, że wszystkie liczby zostały zgadnięte, i następuje wygrana w lotto
gg = 0

# pomocnicze zmienne, które będą miały przypisaną wartość 1 albo 0, zależnie od tego, czy wylosowana w loterii liczba zgadza się z liczbą, wybraną przez użytkownika
h1 = 0
h2 = 0
h3 = 0
h4 = 0
h5 = 0
h6 = 0

# lista "prawda" są to wszystkie liczby użytkownika połączone w jedną listę dla wygody programisty
prawda = [v1, v2, v3, v4, v5, v6]

# "fals" jest to lista liczb, obecnie wylosowanych przez loterię lotto
fals = [b1, b2, b3, b4, b5, b6]


# informacyjnie napisanie użytkownikowi jakie wybrał liczby, albo poinformowanie jakie liczby zopstały dla użytkownika wybrane, jeśli program zrobił to samodzielnie:
if samolosowanie == 0:
    print("Twoje wybrane liczby to: ")
else:
    print("Program wylosował dla Ciebie poniższe liczby:")
print(prawda)

print()

# pętla while będzie się wykonywać tak długo, aż zmienna gg nie będzie wynosiła 6. Zmienna gg wynosi 6 tylko, kiedy zostanie wylosowane 6 liczb wybranych przez użytkownika.
while gg != 6:
    timer += 1
    if timer % 1000000 == 0:
        if timer == 1000000:
            print("Program dalej pracuje, obecnie wysłaono:", int(timer/1000000), " milion losów")
            print("Twoje wybrane liczby : ", (prawda))
            print("Podczas kiedy ostatnia edycja lotto miała wylosowane te liczby: ", berg)
            c3 = timer * (2.3 / 365)
            print("Jak narazie czekasz na wygraną", int(c3),"lat, regularnie 3 razy w tygodniu wysyłając lotto z tymi samymi liczbami")
            print()
        if timer == 2000000 or timer == 3000000 or timer == 4000000:
            print("Program dalej pracuje, obecnie wysłaono:", int(timer / 1000000), " miliony losów")
            print("Twoje wybrane liczby : ", (prawda))
            print("Podczas kiedy ostatnia edycja lotto miała wylosowane te liczby: ", berg)
            c3 = timer * (2.3 / 365)
            print("Jak narazie czekasz na wygraną", int(c3),"lat, regularnie 3 razy w tygodniu wysyłając lotto z tymi samymi liczbami")
            print()
        if timer > 4000000:
            print("Program dalej pracuje, obecnie wysłaono:", int(timer/1000000), " milionów losów")
            print("Twoje wybrane liczby : ", (prawda))
            print("Podczas kiedy ostatnia edycja lotto miała wylosowane te liczby: ", berg)
            c3 = timer * (2.3 / 365)
            print("Jak narazie czekasz na wygraną", int(c3),"lat, regularnie 3 razy w tygodniu wysyłając lotto z tymi samymi liczbami")
            print()

    # losowanie liczb lotto: (poniżej b1 do b6)
    b1 = randint(1,49)
    b2 = randint(1,49)
    while b2 == b1:
        b2 = randint(1, 49)
    b3 = randint(1,49)
    while b3 == b2 or b3 == b1:
        b3 = randint(1,49)
    b4 = randint(1,49)
    while b4 == b3 or b4 == b2 or b4 == b1:
        b4 = randint(1,49)
    b5 = randint(1,49)
    while b5 == b4 or b5 == b3 or b5 == b2 or b5 == b1:
        b5 = randint(1, 49)
    b6 = randint(1,49)
    while b6 == b5 or b6 == b4 or b6 == b3 or b6 == b2 or b6 == b1:
        b6 = randint(1, 49)

    #przyporządkowanie liczb wylosowanych w loterii do listy, by mogły być porównane z liczbami użytkownika:
    fals = [b1, b2, b3, b4, b5, b6]


    berg = [b1, b2, b3, b4, b5, b6]

    #program sprawdza, czy liczby wybrane przez użytkownika zostały zalezione w liście fals, reprezentującej obecne liczby ten edycji lotto
    h1 = (fals.count(v1))
    if h1 == 1:
        fals.remove(v1)
    h2 = (fals.count(v2))
    if h2 == 1:
        fals.remove(v2)
    h3 = (fals.count(v3))
    if h3 == 1:
        fals.remove(v3)
    h4 = (fals.count(v4))
    if h4 == 1:
        fals.remove(v4)
    h5 = (fals.count(v5))
    if h5 == 1:
        fals.remove(v5)
    h6 = (fals.count(v6))
    if h6 == 1:
        fals.remove(v6)

    #program liczy ile razy zostały wylosowane wybrane przez użytkownika liczby, i zapisuje to w postaci zmiennej (gg) jeśli gg wynosi 6 to wygrana
    gg = h1 + h2 + h3 + h4 + h5 + h6

    # jeśli gg nie wynosi 6, to resetowane są liczniki znalezionych liczb, i wracamy do punktu startowego
    if gg != 6:
        h1 = 0
        h2 = 0
        h3 = 0
        h4 = 0
        h5 = 0
        h6 = 0

print()

if plec == 0:
    #jeśli użytkownik to mężczyzna:
    print("Brawo! Wybrałeś lotka! udało Ci się to za:", timer, "razem")
    if samolosowanie == 0:
        print("Twoje wybrane liczby to: ", prawda)
    else:
        print("Program wylosował dla Ciebie poniższe liczby:", prawda)
    print()
    print("Liczby, które były wylosowane w tej edycji lotto: ", berg)
    c2 = timer * 3
    c3 = timer * (2.3 / 365)
    c4 = c2 / 1000000
    print("Zakładając, że bilet kosztuje 3 złote, to na tę wygraną przeznaczyłeś", c2, "Złotych")
    if c2 > 1000000:
        print("Średnio wygrana w lotto jest warta niecałe 6 milionów złotych, podczas kiedy Ty, dla wygranej przeznaczyłeś ponad",
              int(c4), "milionów złotych")
    print("Na wygrane musiałeś czekać tylko", int(c3), "lat")
    print("Sam się zastanów, czy było warto")

else:
    #jeśli użytkownik to kobieta:
    print("Brawo! Wygrałaś lotka! udało Ci się to za:", timer, "razem")
    if samolosowanie == 0:
        print("Twoje wybrane liczby to: ", prawda)
    else:
        print("Program wylosował dla Ciebie poniższe liczby:", prawda)
    print("Liczby, które były wylosowane w tej edycji lotto: ", berg)
    c2 = timer * 3
    c3 = timer * (2.3 / 365)
    c4 = c2 / 1000000
    print("Zakładając, że bilet kosztuje 3 złote, to na tę wygraną przeznaczyłaś", c2, "Złotych")
    if c2 > 1000000:
        print("Średnio wygrana w lotto jest warta niecałe 6 milionów złotych, podczas kiedy Ty, dla wygranej przeznaczyłaś ponad",
                        int(c4), "milionów złotych")
    print("Na wygrane musiałaś czekać tylko", int(c3), "lat")
    print("Sama się zastanów, czy było warto")
