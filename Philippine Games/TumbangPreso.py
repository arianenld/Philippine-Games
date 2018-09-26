#Import and initialize
import pygame, random
from past.builtins import execfile

pygame.init()

global main2, background, canSound, swooshSound, gameoverSound, scoreCtr, canX

#Display configuration
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tumbang Preso")

background = pygame.image.load("gameplayBg.jpg")
background = pygame.transform.scale(background, (800, 600))

#Entity
canSound = pygame.mixer.Sound("canSound.ogg")
swooshSound = pygame.mixer.Sound("swoosh.ogg")
gameoverSound = pygame.mixer.Sound("gameover.ogg")
gameoverSound.set_volume(.5)

pygame.mixer.music.load('duck.ogg')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

scoreCtr = 0
canX = 0

global randomCan, checkChoice
def randomCan():
    global canX, choice
    bombs = ["left", "right"]
    choice = random.choice(bombs)

    if choice == "right":
        canX = screen.get_width()
    if choice == "left":
        canX = 0


def checkChoice():
    global canX, choice, scoreCtr
    if choice == "right":
        canX -= 10
        if scoreCtr >= 5 and scoreCtr < 10:
            canX -= 11
        elif scoreCtr >= 10:
            canX -= 12
    if choice == "left":
        canX += 10
        if scoreCtr >= 5 and scoreCtr < 10:
            canX += 11
        elif scoreCtr >= 10:
            canX += 12

    if canX <= 0 or canX >= screen.get_width():
        randomCan()


def main2():
    global scoreCtr, canX
    livesCtr = 5

    myFont = pygame.font.SysFont("Century Gothic", 25)
    myFont2 = pygame.font.SysFont("Century Gothic", 50)
    randomFallCan = ["can2.1.png", "can2.2.png"]
    randomCan()

    #ACTION
    #Assign values
    clock = pygame.time.Clock()
    keepGoing = True

    sandalX = -70
    sandal_y = 550
    deg = 30
    click = False

    #Loop
    while keepGoing:
        #Timing
        clock.tick(360)

        scoreLbl = myFont.render("Score: " + str(scoreCtr), 1, (0, 0, 0))
        livesLbl = myFont.render("Lives: " + str(livesCtr), 1, (0, 0, 0))

        can = pygame.image.load("can1.png")
        can = pygame.transform.scale(can, (25, 50))

        sandal = pygame.image.load("slipper2.png")
        sandal = pygame.transform.scale(sandal, (25, 50))
        screen.blit(background, (0, 0))
        screen.blit(scoreLbl, (15, 15))
        screen.blit(livesLbl, (700, 15))
        screen.blit(can, (canX, 200))

        checkChoice()

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                swooshSound.play()
                sandalX, sandalY = pygame.mouse.get_pos()
                sandal_y = 550
                click = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    swooshSound.play()
                    execfile("Home.py")
                    quit()


        sandal_rect = sandal.get_rect()
        sandal_rect.x = sandalX
        sandal_rect.y = sandal_y

        can_rect = can.get_rect()
        can_rect.x = canX
        can_rect.y = 200

        if sandal_rect.colliderect(can_rect):
            canSound.play()
            choiceFallCan = random.choice(randomFallCan)
            can = pygame.image.load(choiceFallCan)
            can = pygame.transform.scale(can, (50, 25))
            sandalX = -70
            sandal_y = 550
            pygame.time.delay(150)
            screen.blit(can, (canX - 30, 230))
            scoreCtr += 1
            randomCan()
            click = False

        elif click and not (sandal_rect.colliderect(can_rect)) and sandal_y < 200:
            livesCtr -= 1
            click = False

        if livesCtr <= 0:
            livesCtr = 0

        if livesCtr == 0:
            gameoverSound.play()
            lblGO = myFont2.render("GAME OVER", 1, (0, 0, 0))
            lblSB = myFont.render("I-press ang spacebar upang makapaglarong muli.", 1, (0, 0, 0))
            lblEsc = myFont.render("I-press ang ESC upang bumalik sa Home.", 1, (0, 0, 0))
            screen.blit(background, (0, 0))
            screen.blit(lblGO, (240, 250))
            screen.blit(lblSB, (110, 310))
            screen.blit(lblEsc, (150, 340))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                scoreCtr = 0
                main2()

        #Refresh display
        sandal_y -= 40
        deg += 45
        sandal = pygame.transform.rotozoom(sandal, deg, 1)
        screen.blit(sandal, (sandalX, sandal_y))
        pygame.display.update()


main2()