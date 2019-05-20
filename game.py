import pygame

window_length = 1200
window_height = 700
window = pygame.display.set_mode((window_length, window_height))
background = [0, 0, 0]


def start():
    catx = 700
    caty = 400
    move = -5
    done = False
    jump = 0
    image = pygame.image.load("cat.png")

    while not done:
        window.fill(background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                window.fill(background)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump = 10
        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render("We can write something here", True, (0, 128, 0))
        window.blit(text,
                    (600 - text.get_width() // 2,
                     450 - text.get_height() // 2))
        pygame.draw.rect(window, (0, 128, 255),
                         pygame.Rect(10, 24, 15, 50))
        pygame.draw.circle(window, (200, 22, 134), (199, 200), 12)
        image = pygame.transform.scale(image, (250, 200))
        catx = catx + move
        caty = caty - jump
        if catx < 25:
            image = pygame.transform.flip(image, True, False)
            move = 5
        if catx > window_length - 220:
            image = pygame.transform.flip(image, True, False)
            move = -5
        if caty < 250:
            jump = -10
        if caty == 400:
            jump = 0
        window.blit(image, (catx, caty))

   #     pix = pygame.PixelArray(window)
  #      pix[40][20] = (255,255, 255)
 #       pix[80][20] = (255, 255, 255)
#        pix[100][20 ] = (255,255 , 255)
        pygame.display.flip()
#        pygame.time.wait(50)
pygame.init()
pygame.font.init()
start()
pygame.quit()