#Import and Initialize
import pygame, random
from past.builtins import execfile

pygame.init()

#Display Configurations
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sipa")

global Sipa, sipaHeight, sipaWidth, y_upperBound, y_lowerBound, background, sipaArea, gameoverSound, swooshSound, myFont, myFont2, x_Area, Score, font1, Lives, score, lives, sipaSprite

sipaHeight = 130
sipaWidth = 800
y_upperBound = 320
y_lowerBound = 330

background = pygame.image.load("gameplayBg.jpg").convert()
background = pygame.transform.scale(background, (screen.get_size()))
sipaArea = pygame.image.load("sipabg.png")
sipaArea = pygame.transform.scale(sipaArea, (sipaWidth, sipaHeight))

#Entity
gameoverSound = pygame.mixer.Sound("gameover.ogg")
gameoverSound.set_volume(.5)
swooshSound = pygame.mixer.Sound("swoosh.ogg")

myFont = pygame.font.SysFont("Century Gothic", 25)
myFont2 = pygame.font.SysFont("Century Gothic", 50)

x_Area = 0
Score = False
Lives = False
font1 = pygame.font.SysFont("Century Gothic", 25)
score = 0
lives = 5

pygame.mixer.music.load('cinema.ogg')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

class Sipa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        sipa = pygame.image.load("sipa1.png")
        sipa = pygame.transform.scale(sipa, (100, 150))
        self.image = sipa
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width()/2
        self.rect.y = 180

    def update(self):
        global Score, Lives, y_upperBound
        ten = [30, -30]
        choice = random.choice(ten)
        self.rect.y += 2.5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            swooshSound.play()
            if self.rect.y >= y_upperBound or self.rect.y <= 200: #BABO, LALAM
                Lives = True
            elif self.rect.y <= y_upperBound and self.rect.y >= 200:
                Score = True

            self.rect.y -= 50
            self.rect.x += choice

        if self.rect.x <224: #BOUNDARIES FOR X
            self.rect.x = 220
        if self.rect.x > 564:
            self.rect.x = 560

        if self.rect.y <= -150: #BOUNDARIES FOR Y
            self.rect.y = 0
        if self.rect.y > y_lowerBound:
            self.rect.y = y_lowerBound
            Lives = True

        if score >= 15 and score <= 20:
            self.rect.y += 4
        if score >= 21 and score <= 30:
            self.rect.y += 6
        if score >= 31 and score <= 40:
            self.rect.y += 8
        if score >= 50:
            self.rect.y += 10

sipa = Sipa() #OBJECT
sipaSprite = pygame.sprite.Group(sipa) #SPRITE GROUP

def main():
    global score, lives, Score, Lives, sipaArea, sipaHeight, x_Area, y_upperBound, y_lowerBound

    #ACTION
    #Assign Values
    keepGoing = True
    clock = pygame.time.Clock()

    #Loop
    while keepGoing:
        #Timing
        clock.tick(120)

        # Refresh Display
        screen.blit(background, (0, 0))
        screen.blit(sipaArea, (x_Area, 350))
        score_ = font1.render("Score: " + str(score), True, (0, 0, 0))
        lives_ = font1.render("Lives: " + str(lives), True, (0, 0, 0))
        screen.blit(score_, (10, 10))
        screen.blit(lives_, (10, 30))
        sipaSprite.update()
        sipaSprite.draw(screen)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    swooshSound.play()
                    execfile("Home.py")

        #CONDITIONS
            if Score:
                score+=1
                Lives = False
                Score = False
            if Lives:
                lives-=1
                Score = False
                Lives = False

            decrease = [20, 15]
            choice = random.choice(decrease)
            if score == 15:
                sipaHeight -= choice
                y_lowerBound-= choice
                sipaArea = pygame.transform.scale(sipaArea, (800, sipaHeight))
            elif score == 25:
                sipaHeight -= choice
                y_lowerBound -= choice
                sipaArea = pygame.transform.scale(sipaArea, (800, sipaHeight))
            elif score == 40:
                sipaHeight -= choice
                y_lowerBound -= choice
                sipaArea = pygame.transform.scale(sipaArea, (800, sipaHeight))
            if score == 50:
                sipaWidth = 600
                sipaArea = pygame.transform.scale(sipaArea, (sipaWidth, sipaHeight))
                x_Area = 100

        if lives <= 0:
            lives = 0

        #Gameover
        if lives == 0:
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
                #print("here")
                execfile("Sipav2.py")

        pygame.display.update()
main()