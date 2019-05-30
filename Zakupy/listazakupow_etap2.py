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
    print("Nie jestem jeszcze zaimplementowany :(")
    pass


def dodaj(opcje):
    print("Nie jestem jeszcze zaimplementowany :(")
    pass


def usun(opcje):
    print("Nie jestem jeszcze zaimplementowany :(")
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
