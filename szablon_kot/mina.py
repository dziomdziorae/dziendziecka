import pygame
import random


class Mina:
    def __init__(self):
        self.__minax = random.randint(0, 1150)
        self.__minay = random.randint(0, 500)
        self.__eksplozja = pygame.image.load('eksplozja.png')
        self.__mina = pygame.image.load('mina.png')
        self.__mina_dlugosc = 100
        self.__mina_szerokosc = 50

    def wyswietl_mine(self):
        mina = pygame.transform.scale(self.__mina,
                                      (self.__mina_dlugosc,
                                       self.__mina_szerokosc))
        return [mina, (self.__minax, self.__minay)]

    def wez_polozenie(self):
        return [[self.__minax, self.__minay],
                [self.__minax + self.__mina_dlugosc,
                self.__minay + self.__mina_szerokosc]]

    def wyswietl_eksplozja(self):
        mina = pygame.transform.scale(self.__eksplozja,
                                      (self.__mina_dlugosc*3,
                                       self.__mina_szerokosc*3))
        return [mina, (self.__minax, self.__minay)]

