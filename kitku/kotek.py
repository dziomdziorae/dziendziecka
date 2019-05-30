import pygame


class Kotek:
    def __init__(self):
        self.__catx = 700
        self.__caty = 400
        self.__kot = pygame.image.load('cat.png')
        self.__ruch_poziomy = -1
        self.__ruch_pionowy = 0
        self.__kitku_dlugosc = 150
        self.__kitku_szerokosc = 100

    def ustaw_zmienne(self, ruch_poziomy, ruch_pionowy):
        self.__ruch_poziomy = ruch_poziomy
        self.__ruch_pionowy = ruch_pionowy

    def wyswietl_kotka(self):
        kitku = pygame.transform.scale(self.__kot,
                                       (self.__kitku_dlugosc,
                                        self.__kitku_szerokosc))
        self.__catx += self.__ruch_poziomy
        self.__caty += self.__ruch_pionowy
        return [kitku, (self.__catx, self.__caty)]

    def wez_polozenie(self):
        self.__catx += self.__ruch_poziomy
        self.__caty += self.__ruch_pionowy

        return [(self.__catx, self.__caty),
                (self.__catx + self.__kitku_dlugosc,
                 self.__caty + self.__kitku_szerokosc)]
