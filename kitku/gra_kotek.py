import pygame
from kitku.kotek import Kotek
from kitku.myszka import Myszka
from kitku.mina import Mina


background = [0, 0, 0]


def jesli_myszka(polozenie_kota, polozenie_myszki):
    kotek_x_poczatek = polozenie_kota[0][0]
    kotek_x_koniec = polozenie_kota[1][0]
    kotek_y_poczatek = polozenie_kota[0][1]
    kotek_y_koniec = polozenie_kota[1][1]
    mysz_x_poczatek = polozenie_myszki[0][0]
    mysz_x_koniec = polozenie_myszki[1][0]
    mysz_y_poczatek = polozenie_myszki[0][1]
    mysz_y_koniec = polozenie_myszki[0][1]
    if (mysz_x_poczatek > kotek_x_poczatek and
        mysz_x_koniec < kotek_x_koniec) and\
            (mysz_y_poczatek > kotek_y_poczatek and
             mysz_y_koniec < kotek_y_koniec):
        return True
    return False


def jesli_mina(polozenie_kota, polozenie_miny):
    kotek_x_poczatek = polozenie_kota[0][0]
    kotek_x_koniec = polozenie_kota[1][0]
    kotek_y_poczatek = polozenie_kota[0][1]
    kotek_y_koniec = polozenie_kota[1][1]
    mina_x_poczatek = polozenie_miny[0][0]
    mina_x_koniec = polozenie_miny[1][0]
    mina_y_poczatek = polozenie_miny[0][1]
    mina_y_koniec = polozenie_miny[0][1]
    if (mina_x_poczatek > kotek_x_poczatek and
        mina_x_koniec < kotek_x_koniec) and\
            (mina_y_poczatek > kotek_y_poczatek and
             mina_y_koniec < kotek_y_koniec):
        return True
    return False


def start():
    score = 0
    level = 200
    lista_min = []
    info = str(pygame.display.Info())
    szerokosc_okna = 1300
    wysokosc_okna = 700
    window = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
    done = False
    kotek = Kotek()
    myszka = Myszka()
    while not done:
        window.fill(background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                window.fill(background)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    kotek.ustaw_zmienne(0, 1)
                if event.key == pygame.K_UP:
                    kotek.ustaw_zmienne(0, -1)
                if event.key == pygame.K_LEFT:
                    kotek.ustaw_zmienne(-1, 0)
                if event.key == pygame.K_RIGHT:
                    kotek.ustaw_zmienne(1, 0)
        if level == score:
            level += 200
            lista_min.append(Mina())

        if jesli_myszka(kotek.wez_polozenie(), myszka.wez_polozenie()):
            score += 40
            myszka = Myszka()
            pygame.time.wait(200)

        wyswietl_myszke = myszka.wyswietl_mysz()
        window.blit(wyswietl_myszke[0], wyswietl_myszke[1])
        wyswietl_kotka = kotek.wyswietl_kotka()
        if wyswietl_kotka[1][0] < 0:
            kotek.ustaw_zmienne(1, 0)
        elif wyswietl_kotka[1][0] > 1150:
            kotek.ustaw_zmienne(-1, 0)
        elif wyswietl_kotka[1][1] == 0:
            kotek.ustaw_zmienne(0, 1)
        elif wyswietl_kotka[1][1] > 550:
            kotek.ustaw_zmienne(0, -1)
        window.blit(wyswietl_kotka[0], wyswietl_kotka[1])
        for _ in lista_min:
            wyswietl_mine = _.wyswietl_mine()
            window.blit(wyswietl_mine[0], wyswietl_mine[1])
            if jesli_mina(kotek.wez_polozenie(), _.wez_polozenie()):
                kotek.ustaw_zmienne(0, 0)
                wyswietl_eksplozje = _.wyswietl_eksplozja()
                window.blit(wyswietl_eksplozje[0], wyswietl_eksplozje[1])
                font = pygame.font.SysFont("comicsansms", 45)
                text = font.render("GAME OVER", True, (0, 128, 0))
                window.blit(text,
                            (600 - text.get_width() // 2,
                             350 - text.get_height() // 2))
        pygame.display.flip()


pygame.init()
pygame.font.init()
start()
pygame.quit()