#!/usr/bin/env python3

import argparse
import os
import sys
import typing

lokalizacja_skryptu = os.path.dirname(os.path.realpath(__file__))

konfiguracja = {
}


class Zakup:
    def __init__(self):
        pass

    def to_array(self):
        pass
# Koniec klasy Zakup


def wczytaj_dane(konfiguracja: typing.Dict[str, str]) -> typing.List[Zakup]:
    pass


def zapisz_dane(dane: typing.List[Zakup]) -> None:
    pass


# Polecenia:
def wypisz(opcje):
    pass


def dodaj(opcje):
    pass


def usun(opcje):
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
