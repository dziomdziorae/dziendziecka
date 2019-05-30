from szablon_kolory.prostokat import Prostokat
import pygame


def zmien_kolor(zmiana, indeks, lista_kolorow):
    if zmiana == 1:
        if indeks == len(lista_kolorow) - 1:
            return 0
        else:
            return indeks + 1
    else:
        if not indeks:
            return len(lista_kolorow) - 1
        else:
            return indeks - 1


lista_kolorow_tla = [[127, 255, 212], [230, 28, 102],
                     [65, 105, 225], [249, 224, 75],
                     [0, 127, 255], [159, 251,  136],
                     [226, 225, 163], [255, 255, 190],
                     [159, 159, 223], [188, 226, 127]]

lista_kolorow_prostokat = [[51, 0, 204], [172, 225, 174],
                           [255, 215, 0], [255, 56, 0],
                           [255, 192, 0], [213, 173,  66],
                           [218, 124, 32], [255, 109, 102],
                           [233, 127, 81], [233, 107, 57]]

lista_prostokatow = [Prostokat(100, 70, 0),
                     Prostokat(800, 30, 0),
                     Prostokat(750, 450, 0),
                     Prostokat(100, 400, 0),
                     Prostokat(500, 300, 0)]

pygame.init()
szerokosc_okna = 1200
wysokosc_okna = 700
okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
indeks_tla = 0
done = True
background = [0, 0, 0]

while done:
    okno.fill(lista_kolorow_tla[indeks_tla])
    for _ in lista_prostokatow:
        pygame.draw.rect(okno, lista_kolorow_prostokat[_.get_indeks()], _.wyswietl_prostokat())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                okno.fill(background)
                pygame.time.wait(800)
                done = False
            if event.key == pygame.K_LEFT:
                change_tlo = True
                for _ in lista_prostokatow:
                    if _.sprawdz_czy_zmienic_kolor(pygame.mouse.get_pos()):
                        _.ustaw_indeks(zmien_kolor(-1, _.get_indeks(), lista_kolorow_prostokat))
                        change_tlo = False
                        break
                if change_tlo:
                    indeks_tla = zmien_kolor(-1, indeks_tla, lista_kolorow_tla)
            if event.key == pygame.K_RIGHT:
                change_tlo = True
                for _ in lista_prostokatow:
                    if _.sprawdz_czy_zmienic_kolor(pygame.mouse.get_pos()):
                        _.ustaw_indeks(zmien_kolor(-1, _.get_indeks(), lista_kolorow_prostokat))
                        change_tlo = False
                        break
                if change_tlo:
                    indeks_tla = zmien_kolor(1, indeks_tla, lista_kolorow_tla)
    pygame.display.flip()
pygame.quit()
