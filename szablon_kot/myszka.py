import pygame
import random


class Myszka:
    def __init__(self):
        self.__myszx = random.randint(10, 1150)
        self.__myszy = random.randint(10, 500)
        self.__mysz = pygame.image.load('mouse.png')
        self.__myszka_dlugosc = 100
        self.__myszka_szerokosc = 50

    def wyswietl_mysz(self):
        myszka = pygame.transform.scale(self.__mysz,
                                        (self.__myszka_dlugosc,
                                         self.__myszka_szerokosc))
        return [myszka, (self.__myszx, self.__myszy)]

    def wez_polozenie(self):
        return [[self.__myszx, self.__myszy],
                [self.__myszx + self.__myszka_dlugosc,
                 self.__myszy + self.__myszka_szerokosc]]


