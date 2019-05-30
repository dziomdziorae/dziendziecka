import pygame

class Prostokat:
    def __init__(self, pozx, pozy, indeks):
        self.__prostokat_x = pozx
        self.__prostokat_y = pozy
        self.__prostokat_szerokosc = 160
        self.__prostokat_wysokosc = 120
        self.__prostokat = pygame.Rect(self.__prostokat_x,
                                       self.__prostokat_y,
                                       self.__prostokat_szerokosc,
                                       self.__prostokat_wysokosc)
        self.__indeks = indeks

    def wyswietl_prostokat(self):
        return self.__prostokat

    def get_indeks(self):
        return self.__indeks

    def ustaw_indeks(self, indeks):
        self.__indeks = indeks

    def sprawdz_czy_zmienic_kolor(self, pozycja_myszki):

        return (pozycja_myszki[0] < self.__prostokat_x + self.__prostokat_szerokosc) and\
            (pozycja_myszki[0] > self.__prostokat_x) and\
            (pozycja_myszki[1] < self.__prostokat_y + self.__prostokat_wysokosc) and (
                        pozycja_myszki[1] > self.__prostokat_y)