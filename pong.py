import pygame


screen = pygame.display.set_mode((1200, 500))


def game(level):
    done = False
    x = 10
    y = 10
    top = 20
    posx = 600
    posy = 250
    a = 1 * level
    b = 1 * level
    length = 80
    scorea = 0
    scoreb = 0
    temp = 0
    sleep = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                screen.fill((0, 0, 0))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            done = True
        if scorea == 5:
            screen.fill((0, 0, 0))
            text = font.render("The winner is the player no 1",
            True, (0, 128, 0))

            score = "Score:  " + str(scorea)+ ':' + str(scoreb)
            score_text = font.render(score, True, (0, 128, 0))
            screen.blit(text,
                        (600 - text.get_width() // 2,
                         250 - text.get_height() // 2))
            screen.blit(score_text,
                        (600 - text.get_width() // 2,
                         10 - text.get_height() // 2))
            sleep += 1
            if sleep == 6000:
                done = True
        elif scoreb == 5:
            screen.fill((0, 0, 0))
            text = font.render("The winner is the player no 2",
             True, (0, 128, 0))
            screen.blit(text,
                        (600 - text.get_width() // 2,
                         10 - text.get_height() // 2))
            sleep += 1
            if sleep == 6000:
                done = True
        else:
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont("comicsansms", 15)
            score = "Score:  " + str(scorea) + ':' + str(scoreb)
            text = font.render(score, True, (0, 128, 0))
            screen.blit(text,
                        (600 - text.get_width() // 2,
                         10 - text.get_height() // 2))

            if posx >= 1180:
                if posy < y + length and posy > y:
                    a = -1 * level
                    b = -0.3 * level
                    temp = 0
                else:
                    a = 0
                    b = 0
                    if temp == 0:
                        scorea += 1
                        temp = 1
            if posx <= 10:
                if posy < x + length and posy > x:
                    a = 1 * level
                    b = 0.7 * level
                    temp = 0
                else:
                    a = 0
                    b = 0
                    if temp == 0:
                        scoreb += 1
                        temp = 1
            if posy < top:
                b = 0.5
            if posy > 490:
                b = -0.5
            pygame.draw.rect(screen, (0, 128, 255),
            pygame.Rect(10, x, 15, length))
            pygame.draw.rect(screen, (0, 128, 124),
            pygame.Rect(int(posx), int(posy), 10, 10))
            pygame.draw.rect(screen, (0, 128, 255),
            pygame.Rect(1180, y, 15, length))
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w] and x > top:
                x -= 1
            if pressed[pygame.K_a] and x < 500 - length:
                x += 1
            if pressed[pygame.K_DOWN] and y < 500-length:
                y += 1
            if pressed[pygame.K_UP] and y > top:
                y -= 1
            if pressed[pygame.K_ESCAPE]:
                done = True
            posx += a
            posy += b
        pygame.display.flip()

pygame.init()
pygame.font.init()
game(3)
pygame.quit()