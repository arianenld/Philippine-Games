#Import and initialize
import pygame, random
from past.builtins import execfile

pygame.init()

#Display configuration
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption(("Batang 90's: Luksong Baka"))

global Child, Playmates, Background, background1, main3, font1, background2, score, lives, speed1, xBackground

xBackground = 0
background1 = pygame.image.load("3.1.1 bg - gameplay 2.2.jpg")
background2 = pygame.image.load("lbBG2.png")
background2 = pygame.transform.scale(background2, (900,250))

#Entity
pygame.mixer.music.load('quest.ogg')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

swooshSound = pygame.mixer.Sound("swoosh.ogg")

font1 = pygame.font.SysFont("Century Gothic", 25)
score = 0
lives = 5
speed1 = 0


class Child(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        child = pygame.image.load("boy 1.00.png")
        child = pygame.transform.scale(child,(50, 100))
        self.image = child
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 280

        self.child_y = 150
    def update(self):
        self.rect.y = self.rect.y
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.image = pygame.image.load("boy 1.01.png")
                    self.image = pygame.transform.scale(self.image, (65, 100))
                    self.rect.y -= self.child_y
            else:
                self.image = pygame.image.load("boy 1.00.png")
                self.image = pygame.transform.scale(self.image , (50, 100))

        self.rect.y += 8
        if self.rect.y > 280:
            self.rect.y = 280 #PLATFORM
        if self.rect.y < 130: #MAXIMUM HEIGHT OF THE CHILD CAN JUMP
            self.rect.y = 130

class Playmates(pygame.sprite.Sprite):
    willScore = True
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        boys = ["boy 1.1.png", "boy 1.2.png", "boy 1.3.png"]
        choice = random.choice(boys)
        enemy = pygame.image.load(choice)
        enemy = pygame.transform.flip(enemy, True, False)
        enemy = pygame.transform.scale(enemy, (60, 75))
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.x = 850
        self.rect.y = random.randrange(310, 313)
        self.speedx = random.randrange(10, 13)
        self.distance_x = 5

    def update(self):
        global score, speed1

        if score >= 0  and score <=5:
            speed1 = 3
        elif score >= 6 and score <= 10:
            speed1 = 10
        elif score >= 10:
            speed1 = 20

        self.rect.x -= self.speedx + speed1
        if self.rect.x < -13:
            self.kill()
            if self.willScore:
                score += 1


class Background():
    def __init__(self):

        self.bgimage = pygame.image.load("lbBG2.png")
        self.bgimage = pygame.transform.scale(self.bgimage, (900,250))
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 126
        self.bgX1 = 0

        self.bgY2 = 126
        self.bgX2 = self.rectBGimg.width

        self.movingSpeed = 0

    def update(self):
        global score

        if score >= 0 and score <= 5:
            self.movingSpeed = 5
        elif score >= 6 and score <= 10:
            self.movingSpeed = 10
        elif score >= 10:
            self.movingSpeed = 20

        self.bgX1 -= self.movingSpeed
        self.bgX2 -= self.movingSpeed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

    def render(self):
        screen.blit(self.bgimage, (self.bgX1, self.bgY1))
        screen.blit(self.bgimage, (self.bgX2, self.bgY2))


def main3():
    global lives, score, xBackground

    #ACTION
    #Assign values
    clock = pygame.time.Clock()
    done = False

    myFont = pygame.font.SysFont("Century Gothic", 25)
    myFont2 = pygame.font.SysFont("Century Gothic", 50)

    gameoverSound = pygame.mixer.Sound("gameover.ogg")
    gameoverSound.set_volume(.5)

    objChild = Child()
    objBg = Background()

    allSprites = pygame.sprite.Group()
    groupChild = pygame.sprite.Group()
    groupPlaymates = pygame.sprite.Group()

    groupChild.add(objChild)
    allSprites.add(objChild)

    #Loop
    while not done:
        #Timing
        clock.tick(720)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    objChild.update()
                if event.key == pygame.K_ESCAPE:
                    swooshSound.play()
                    execfile("Home.py")

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

        if random.randrange(1, 100) % 50 == 0:
            objPlaymates = Playmates()
            groupPlaymates.add(objPlaymates)
            allSprites.add(objPlaymates)

        for friend in groupPlaymates:
            if objChild.rect.colliderect(friend.rect):
                friend.willScore = False
                groupPlaymates.remove(friend)
                lives -= 1
        xBackground -= 5

        if xBackground > screen.get_width():
            xBackground = 0

        screen.blit(background1, (0, 0))
        score_ = font1.render("Score: "+str(score), True, (0,0,0))
        lives_ = font1.render("Lives: "+str(lives), True, (0,0,0))
        screen.blit(score_,(20,10))
        screen.blit(lives_, (780, 10))
        objBg.update()
        objBg.render()
        allSprites.clear(screen, background2)
        allSprites.draw(screen)
        allSprites.update()

        if lives <= 0:
            lives = 0

        if lives == 0:
            gameoverSound.play()
            lblGO = myFont2.render("GAME OVER", 1, (0, 0, 0))
            lblSB = myFont.render("I-press ang spacebar upang makapaglarong muli.", 1, (0, 0, 0))
            lblEsc = myFont.render("I-press ang ESC upang bumalik sa Home.", 1, (0, 0, 0))
            screen.blit(background1, (0, 0))
            screen.blit(background2, (0, 126))
            screen.blit(lblGO, (300, 20))
            screen.blit(lblSB, (160, 80))
            screen.blit(lblEsc, (200, 110))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                execfile("LuksongBaka.py")

        #Refresh display
        pygame.display.update()

main3()