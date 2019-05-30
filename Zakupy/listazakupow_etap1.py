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
    pass


if __name__ == "__main__":
    start()
