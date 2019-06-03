def oblicz(operacje):
    if operacje:
        wynik = int(operacje[0])
    else:
        wynik = "0"
    for _ in range(1, len(operacje), 2):
        if operacje[_] == "+":
            wynik = wynik + int(operacje[_+1])
        elif operacje[_] == '-':
            wynik = wynik - int(operacje[_+1])
        elif operacje[_] == '*':
            wynik = wynik * int(operacje[_ + 1])
        elif operacje[_] == '/':
            if int(operacje[_+1]):
                wynik = wynik / int(operacje[_ + 1])
            else:
                wynik = "error"
                break

    return str(wynik)
