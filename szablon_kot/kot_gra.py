import pygame
from kotek import Kotek
from myszka import Myszka


def jesli_myszka(polozenie_kota, polozenie_myszki):
    kotek_x_poczatek = polozenie_kota[0][0]
    kotek_x_koniec = polozenie_kota[1][0]
    kotek_y_poczatek = polozenie_kota[0][1]
    kotek_y_koniec = polozenie_kota[1][1]
    mysz_x_poczatek = polozenie_myszki[0][0]
    mysz_x_koniec = polozenie_myszki[1][0]
    mysz_y_poczatek = polozenie_myszki[0][1]
    mysz_y_koniec = polozenie_myszki[0][1]
    return (mysz_x_poczatek > kotek_x_poczatek and
            mysz_x_koniec < kotek_x_koniec) and\
           (mysz_y_poczatek > kotek_y_poczatek and
            mysz_y_koniec < kotek_y_koniec)


background = [0, 0, 0]


def start():
    szerokosc_okna = 1300
    wysokosc_okna = 700
    okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
    done = False
    kotek = Kotek()
    myszka = Myszka()
    while not done:
        okno.fill(background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_UP:
                    pass
                    kotek.ustaw_zmienne(0, -1)
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass

        wyswietl_kotka = kotek.wyswietl_kotka()
        okno.blit(wyswietl_kotka[0], wyswietl_kotka[1])
        pygame.display.flip()


pygame.init()
pygame.font.init()
start()
pygame.quit()
