jednostki = str(input(
    "Wybierz rodzaj jednostki, w ktorej podasz dane: metryczne [metry(m) i kilogramy(kg)]"
    "\nlub imperialne [cale(in) i funty(lb)]; aby wybrac jednostki metryczne wpisz 1, aby"
    " \nwybrac jednostki imperialne wpisz 2 : "))

if jednostki == ("1"):
    print("Wybrano jednostki metryczne")
else:
    print("Wybrano jednostki imperialne")

wpisy = int(input("Ile wpisow chce dokonac urzytkownik? Podaj liczbe: "))
a = 1

while a <= wpisy:

    imie = str(input("Podaj imie osoby: "))
    nazwisko = str(input("Podaj nazwisko osoby: "))

    print("Podane imie i nazwisko to:")
    print(imie, nazwisko)

    plec = print(input("Podaj płeć biologiczna [kobieta/mezczyzna]: "))
    if jednostki == ("1"):
        masa = float(input("Podaj masę w kilogramach: "))
    else:
        masa = float(input("Podaj masę w funtach: "))

    if jednostki == "1":
        wzrost = float(input("Podaj wzrost w metrach [np 1.78]: "))
    else:
        wzrost = float(input("Podaj wzrost w calach: "))

    if jednostki == "1":
        bmi = float(masa / (wzrost ** 2))
    else:
        bmi = float(masa / wzrost ** 2) * 703

    # parametry dobrane wg tabeli z instrukcji
    print()
    print(f"BMI: {bmi}\n")
    if bmi < 16:
        print("Wygłodzenie. Zagrożenie zdrowia.")
    elif bmi <= 16.99 and bmi >= 16:
        print("Wychudzenie.")
    elif bmi <= 18.49 and bmi >= 17.0:
        print("Niedowaga.")
    elif bmi <= 25 and bmi >= 18.5:
        print("Prawidłowa masa ciała.")
    elif bmi <= 30 and bmi >= 25:
        print("Nadwaga.")
    elif (bmi <= 35 and bmi > 30):
        print("Otyłość I stopnia.")
    elif bmi <= 39.99 and bmi > 35:
        print("Otyłość II stopnia.")
    else:
        print("Otyłość III stopnia.")

    wpisy = (wpisy) - 1

wpisy = str(input("Dokonales juz wszystkie wpisy. Czy chcesz dokonac wiecej wpisów? [Wpisz: tak lub nie]: "))
print(wpisy)

if wpisy != ("tak"):
    print("Dokonano wpisow, koniec.")
else:

    wpisy = int(input("Ile wpisow chce dokonac urzytkownik? Podaj liczbe: "))
    a = 1

    while a <= wpisy:

        imie = str(input("Podaj imie osoby: "))
        nazwisko = str(input("Podaj nazwisko osoby: "))

        print("Podane imie i nazwisko to:")
        print(imie, nazwisko)

        plec = print(input("Podaj płeć biologiczna [kobieta/mezczyzna]: "))
        if jednostki == ("1"):
            masa = float(input("Podaj masę w kilogramach: "))
        else:
            masa = float(input("Podaj masę w funtach: "))

        if jednostki == ("1"):
            wzrost = float(input("Podaj wzrost w metrach [np 1.78]: "))
        else:
            wzrost = float(input("Podaj wzrost w calach: "))

        if jednostki == ("1"):
            bmi = float(masa / (wzrost ** 2))
        else:
            bmi = float(masa / wzrost ** 2) * 703

        # parametry dobrane wg tabeli z instrukcji
        print()
        print(f"BMI: {bmi}\n")
        if bmi < 16:
            print("Wygłodzenie. Zagrożenie zdrowia.")
        elif bmi <= 16.99 and bmi >= 16:
            print("Wychudzenie.")
        elif bmi <= 18.49 and bmi >= 17.0:
            print("Niedowaga.")
        elif bmi <= 25 and bmi >= 18.5:
            print("Prawidłowa masa ciała.")
        elif bmi <= 29.99 and bmi >= 25:
            print("Nadwaga.")
        elif (bmi <= 34.99 and bmi > 30):
            print("Otyłość I stopnia.")
        elif bmi <= 39.99 and bmi >= 35:
            print("Otyłość II stopnia.")
        else:
            print("Otyłość III stopnia.")
#test
        wpisy = (wpisy) - 1
    wpisy = str(input("Dokonano juz wszystkich wpisow. Koniec. "))
    print(wpisy)
