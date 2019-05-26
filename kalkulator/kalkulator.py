import pygame
import kalkulator_logika


szerokosc_okna = 400
wysokosc_okna = 350
okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
background = [0, 0, 0]


def tabela_cyfr():
    cyfry_klawisze = {'1': [[100, 100], [150, 120]],
                      '2': [[165, 100], [215, 120]],
                      '3': [[230, 100], [280, 120]],
                      '4': [[100, 135], [150, 155]],
                      '5': [[165, 135], [215, 155]],
                      '6': [[230, 135], [280, 155]],
                      '7': [[100, 170], [150, 190]],
                      '8': [[165, 170], [215, 190]],
                      '9': [[230, 170], [280, 190]],
                      '0': [[165, 205], [215, 225]]
                      }
    return cyfry_klawisze


def tabela_dzialan():
    dzialania_przyciski = {'\\': [[300, 75], [340, 95]],
                           '+': [[300, 100], [340, 120]],
                           '-': [[300, 125], [340, 145]],
                           '*': [[300, 150], [340, 170]],
                           '=': [[300, 175], [340, 195]],
                           'c': [[300, 200], [340, 220]],

                           }
    return dzialania_przyciski


def sprawdz_przycisk_cyfra(posx, posy):
    if posx < 100 or posx > 280 or posy < 100 or posy > 225:
        print("wywalam tutaj %s %s " %(posx, posy))
        return False
    przyciski_tabela = tabela_cyfr()
    for _ in range(10):
        posx_x_end = przyciski_tabela[str(_)][1][0]
        pos_y_end = przyciski_tabela[str(_)][1][1]
        pos_x_begin = przyciski_tabela[str(_)][0][0]
        pos_y_begin = przyciski_tabela[str(_)][0][1]
        if ((posx <= posx_x_end)and posx >= pos_x_begin) \
                and ((posy <= pos_y_end) and posy >= pos_y_begin):
            return str(_)


def sprawdz_przycisk_dzialanie(posx, posy):
    if posx <= 300 or posx >= 340 or posy <= 75 or posy >= 220:
        print("wywalam tutaj")

        return False
    przyciski_tabela = tabela_dzialan()
    for _ in przyciski_tabela:
        posx_x_end = przyciski_tabela[str(_)][1][0]
        pos_y_end = przyciski_tabela[str(_)][1][1]
        pos_x_begin = przyciski_tabela[str(_)][0][0]
        pos_y_begin = przyciski_tabela[str(_)][0][1]
        if ((posx < posx_x_end)and posx > pos_x_begin) \
                and ((posy < pos_y_end) and posy > pos_y_begin):
            return str(_)

def start():
    ostatnia_suma = 0
    operacje = []
    liczba = []
    przyciski = tabela_cyfr()
    dzialania = tabela_dzialan()
    done = False
    monitor_dl = 170
    monitor_sz = 30
    klawisz_cyfra_dl = 50
    klawisz_cyfra_sz = 20
    klawisz_dzialanie_dl = 40
    klawisz_dzialanie_sz = 20
    while not done:
        okno.fill(background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                value = sprawdz_przycisk_cyfra(pos[0], pos[1])
                if value and len(liczba) < 15:
                    print(value)
                    if liczba == ostatnia_suma and liczba:
                        liczba = []
                    liczba.append(value)
                    print(liczba)
                dzialanie = sprawdz_przycisk_dzialanie(pos[0], pos[1])
                if dzialanie == "=":
                    if liczba:
                        operacje.append("".join(liczba))
                        liczba = list(kalkulator_logika.oblicz(operacje))
                        operacje = []
                        ostatnia_suma = liczba
                elif dzialanie == 'c':
                    liczba = []
                elif dzialanie:
                    if operacje:
                        if not operacje[-1].isnumeric():
                            if liczba:
                                operacje.append("".join(liczba))
                                operacje.append(dzialanie)
                                liczba = []
                    elif liczba and (not operacje):
                        operacje.append("".join(liczba))
                        operacje.append(dzialanie)
                        liczba = []


        font = pygame.font.SysFont("comicsansms", 18)

        pygame.draw.rect(okno, (255, 255, 255),
                         pygame.Rect(105, 60, monitor_dl, monitor_sz))
        text_value = font.render(''.join(liczba), True, (0, 0, 0))
        okno.blit(text_value, (105 + monitor_dl - text_value.get_width(), 60))
        for _ in dzialania:
            pos_klawisz_x = dzialania[_][0][0]
            pos_klawisz_y = dzialania[_][0][1]
            pygame.draw.rect(okno, (0, 128, 255),
                             pygame.Rect(pos_klawisz_x,
                                         pos_klawisz_y,
                                         klawisz_dzialanie_dl, klawisz_dzialanie_sz))
            text = font.render(str(_), True, (255, 255, 255))
            okno.blit(text, (pos_klawisz_x + 17, pos_klawisz_y - 3))
        for _ in range(10):
            pos_klawisz_x = przyciski[str(_)][0][0]
            pos_klawisz_y = przyciski[str(_)][0][1]
            pygame.draw.rect(okno, (0, 128, 255),
                             pygame.Rect(pos_klawisz_x, pos_klawisz_y,
                             klawisz_cyfra_dl, klawisz_cyfra_sz))
            text = font.render(str(_), True, (255, 255, 255))
            okno.blit(text, (pos_klawisz_x+26, pos_klawisz_y - 3))

        pygame.display.flip()
