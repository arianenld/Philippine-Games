#Import and Initialize
import pygame
from past.builtins import execfile

pygame.init()

playX = 100
playY = 100

gameX = 130
gameY = 130

#Display Configurations
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Batang 90s: Laro Tayo!")

background = pygame.image.load("photos/mainBg.jpg").convert()
background = pygame.transform.scale(background, (800, 600))

menu = pygame.image.load("photos/menuBg.jpg")
menu = pygame.transform.scale(menu, (800, 600))

tbIns = pygame.image.load("photos/insTB.jpg")
tbIns = pygame.transform.scale(tbIns, (800, 600))

sipaIns = pygame.image.load("photos/insSipa.jpg")
sipaIns = pygame.transform.scale(sipaIns, (800, 600))

lbIns = pygame.image.load("photos/insLB.jpg")
lbIns = pygame.transform.scale(lbIns, (800, 600))

playButton = pygame.image.load("icons/play.png")
playButton = pygame.transform.scale(playButton, (playX, playY))

sipaButton = pygame.image.load("icons/sipa.png")
sipaButton = pygame.transform.scale(sipaButton, (gameX, gameY))

tumbangpresoButton = pygame.image.load("icons/tumbang preso.png")
tumbangpresoButton = pygame.transform.scale(tumbangpresoButton, (gameX, gameY))

luksongbakaButton = pygame.image.load("icons/luksong baka.png")
luksongbakaButton = pygame.transform.scale(luksongbakaButton, (gameX, gameY))

#Entity
pygame.mixer.music.load('lynn.ogg')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

swooshSound = pygame.mixer.Sound("swoosh.ogg")

home = pygame.image.load("icons/home.png")
home = pygame.transform.scale(home, (40, 40))
home_rect = home.get_rect()
home_rect.x = 750
home_rect.y = 10

back = pygame.image.load("icons/back.png")
back = pygame.transform.scale(back, (40, 40))
back_rect = back.get_rect()
back_rect.x = 10
back_rect.y = 10

play_rect = playButton.get_rect()
play_rect.x = 610
play_rect.y = 170

tb_rect = tumbangpresoButton.get_rect()
tb_rect.x = 333
tb_rect.y = 90

sipa_rect = sipaButton.get_rect()
sipa_rect.x = 155
sipa_rect.y = 90

lb_rect = luksongbakaButton.get_rect()
lb_rect.x = 510
lb_rect.y = 90

myFont = pygame.font.SysFont("Century Gothic", 30, True)
sipaLabel = myFont.render("sipa", 1, (0, 0, 139))
tumbangLabel = myFont.render("tumbang", 1, (255, 204, 0))
presoLabel = myFont.render("preso", 1, (255, 204, 0))
luksongbakaLabel = myFont.render("luksong", 1, (139, 0, 0))
bakaLabel = myFont.render("baka", 1, (139, 0, 0))

pressIns = myFont.render("I-press ang spacebar upang makapaglaro.", 1, (0, 0, 0))

screen.blit(background, (0, 0))
screen.blit(playButton, (610, 170))

#ACTION
#Assign values
clock = pygame.time.Clock()
keepGoing = True
sipaGame = False
tbGame = False
lbGame = False

#Loop
while keepGoing:
    #Timing
    clock.tick(60)

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            swooshSound.play()
            if play_rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill((0,0,0,0))
                screen.blit(menu, (0, 0))
                screen.blit(home, (750, 10))

                screen.blit(sipaButton, (155, 90))
                screen.blit(sipaLabel, (188, 220))

                screen.blit(tumbangpresoButton, (333, 90))
                screen.blit(tumbangLabel, (333, 220))
                screen.blit(presoLabel, (358, 250))

                screen.blit(luksongbakaButton, (510, 90))
                screen.blit(luksongbakaLabel, (520, 220))
                screen.blit(bakaLabel, (535, 250))

            if back_rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill((0, 0, 0, 0))
                screen.blit(menu, (0, 0))
                screen.blit(home, (750, 10))

                screen.blit(sipaButton, (155, 90))
                screen.blit(sipaLabel, (188, 220))

                screen.blit(tumbangpresoButton, (333, 90))
                screen.blit(tumbangLabel, (333, 220))
                screen.blit(presoLabel, (358, 250))

                screen.blit(luksongbakaButton, (510, 90))
                screen.blit(luksongbakaLabel, (520, 220))
                screen.blit(bakaLabel, (535, 250))

            if home_rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill((0, 0, 0, 0))
                screen.blit(background, (0, 0))
                screen.blit(playButton, (610, 170))

            if tb_rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill((0, 0, 0, 0))
                screen.blit(tbIns, (0, 0))
                screen.blit(back, (10, 10))
                screen.blit(pressIns, (80, 535))
                sipaGame = False
                lbGame = False
                tbGame = True

            if sipa_rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill((0, 0, 0, 0))
                screen.blit(sipaIns, (0, 0))
                screen.blit(back, (10, 10))
                screen.blit(pressIns, (80, 535))
                tbGame = False
                lbGame = False
                sipaGame = True

            if lb_rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill((0, 0, 0, 0))
                screen.blit(lbIns, (0, 0))
                screen.blit(back, (10, 10))
                screen.blit(pressIns, (80, 535))
                sipaGame = False
                tbGame = False
                lbGame = True

        if event.type == pygame.KEYDOWN:
            swooshSound.play()
            if event.key == pygame.K_SPACE and tbGame:
                execfile("TumbangPreso.py")

            if event.key == pygame.K_SPACE and sipaGame:
                execfile("Sipav2.py")

            if event.key == pygame.K_SPACE and lbGame:
                execfile("LuksongBaka.py")

    #Refresh Display
    pygame.display.flip()

