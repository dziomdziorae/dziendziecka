#!/usr/bin/env python3

import argparse
import os
import sys
import typing

lokalizacja_skryptu = os.path.dirname(os.path.realpath(__file__))

konfiguracja = {
    'plik_z_danymi': f"{lokalizacja_skryptu}/baza_danych.txt",
    'separator': ';',
}


class Zakup:
    def __init__(self):
        self.nazwa_produktu = ""

    def to_array(self):
        return [
            self.nazwa_produktu
        ]
# Koniec klasy Zakup


def wczytaj_dane() -> typing.List[Zakup]:
    lokalizacja_bazy = konfiguracja["plik_z_danymi"]

    dane: typing.List[Zakup] = []

    try:
        plik = open(lokalizacja_bazy, "r")
    except FileNotFoundError as err:
        return dane

    linie = plik.readlines()
    for linia in linie:
        linia = linia.rstrip()
        pola = linia.split(konfiguracja['separator'])
        if len(pola) < 1: continue
        zakup = Zakup()
        zakup.nazwa_produktu = pola[0]
        dane.append(zakup)

    return dane


def zapisz_dane(dane: typing.List[Zakup]) -> None:
    lokalizacja_bazy = konfiguracja["plik_z_danymi"]

    plik = open(lokalizacja_bazy, "w")
    for zakup in dane:
        linia = str.join(konfiguracja['separator'], zakup.to_array()) + '\n'
        plik.write(linia)
    pass


# Polecenia:
def wypisz(opcje):

    print("Twoja lista zakupów:")

    if opcje.tabelka:
        format_tekstu = "| %5s | %-40s |"
        print("\n\n")
        print(format_tekstu % ("L.P.", "Nazwa"))
    else:
        format_tekstu = "Zakup nr %s:\nNazwa: %s\n\n"

    dane = wczytaj_dane()

    for lp in range(1, len(dane) + 1):
        zakup = dane[lp - 1]
        print(format_tekstu % (str(lp), zakup.nazwa_produktu))

    if opcje.tabelka:
        print("\nUWAGA: Niestety, na razie nie umiem zrobić tabelki :(\n\n")

    pass


def dodaj(opcje):
    dane = wczytaj_dane()

    if not opcje.nazwa:
        print("BŁĄD: Nie podano nazwy zakupu!")
        return

    nowy_zakup = Zakup()
    nowy_zakup.nazwa_produktu = opcje.nazwa

    dane.append(nowy_zakup)

    zapisz_dane(dane)
    pass


def usun(opcje):
    dane = wczytaj_dane()

    if not opcje.numer:
        print("BŁĄD: Nie podano numeru zakupu do usunięcia.")
        return

    if opcje.numer < 1 or opcje.numer > len(dane):
        print("BŁĄD: Nie ma tkaiego zakupu o numerze %d" % opcje.numer)
        return

    id_usuniecia = opcje.numer - 1
    zakup_do_usuniecia = dane[id_usuniecia]
    dane.remove(zakup_do_usuniecia)

    print("Usunięto zakup nr %d." % opcje.numer)

    zapisz_dane(dane)

    pass


polecenia = {
    'wypisz':   wypisz,
    'dodaj':    dodaj,
    'usun':     usun,
}


# Główna logika programu:
def start():
    parser = argparse.ArgumentParser(
        description="Program do obsługi listy zakupów",
    )
    podpolecenia = parser.add_subparsers(
        dest='polecenie',
        help="Opis opcji:")

    polecenie_wypisz = podpolecenia.add_parser(
        "wypisz",
        help="wypisuje wszystko z listy zakupów")
    polecenie_wypisz.add_argument(
        "--tabelka",
        action='store_true',
        help="Sformatuje listę w formie tabelki")

    polecenie_dodaj = podpolecenia.add_parser(
        "dodaj",
        help="dodaje nową rzecz do listy zakupów")
    polecenie_dodaj.add_argument("nazwa")

    polecenie_usun = podpolecenia.add_parser(
        "usun",
        help="usuwa rzecz z listy zakupów")
    polecenie_usun.add_argument(
        "numer",
        type=int)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    opcje = parser.parse_args()

    if opcje.polecenie in polecenia:
        polecenia[opcje.polecenie](opcje)
    else:
        raise ValueError(f"Nie ma takiej opcji: {opcje['polecenie']}")
    pass


if __name__ == "__main__":
    start()
