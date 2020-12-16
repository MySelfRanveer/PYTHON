#Gun shot game --> gun fires bullets with different velocities and positions , User has to save himself from bullets.

import pygame;
import sys;
pygame.init();

#Screen size and dimensions
WHITE = (255, 255, 255);
HEIGHT = 750;
WIDTH = 1200;
FPS = 30;
RED = (255, 0, 0);
screenWin = pygame.display.set_mode((WIDTH, HEIGHT));
pygame.display.set_caption("GUN SHOOT");


CLOCK = pygame.time.Clock();
font = pygame.font.SysFont('forte', 20);
NEW_FPS = 30;

class Topscore :
    def __init__(self):
        self.high_score = 0;
    def top_score(self, score) :
        if(self.high_score < score):
            self.high_score = score;
        return self.high_score;

topscore = Topscore();

class Gun :
    gun_velocity = 20;
    def __init__(self):
        self.gun_img = pygame.image.load(r'C:\Users\RANVEER\Desktop\PYTHON\Game using python\Game Project\Gun Shot Game\gunGunShoot.jpg');
        self.gun_img_rect = self.gun_img.get_rect();
        self.gun_img_rect.width -= 10;
        self.gun_img_rect.height -= 10;
        self.gun_img_rect.top = HEIGHT / 2;
        self.gun_img_rect.right = WIDTH;
        self.Up = True;
        self.Down = False;

    def gunShoot(self) :
        screenWin.blit(self.gun_img, (self.gun_img_rect));
        if self.gun_img_rect.top <= 0 :
            self.Up = False;
            self.Down = True;
        elif(self.gun_img_rect.bottom >= HEIGHT) :
            self.Up = True;
            self.Down = False;
        if self.Up :
            self.gun_img_rect.top -= self.gun_velocity ;
            #pass;
        elif self.Down :
            self.gun_img_rect.top += self.gun_velocity ;
            #pass;


class Bullets:
    bullets_velocity = 20;

    def __init__(self):
        self.bullets = pygame.image.load(r'C:\Users\RANVEER\Desktop\PYTHON\Game using python\Game Project\Gun Shot Game\bulletGunShoot.jpg')
        self.bullets_img = pygame.transform.scale(self.bullets, (20, 20))
        self.bullets_img_rect = self.bullets_img.get_rect()
        self.bullets_img_rect.right = gun.gun_img_rect.left
        self.bullets_img_rect.top = gun.gun_img_rect.top + 30
        self.bullets_img_rect.left = self.bullets_img_rect.right;

    def update(self):
        screenWin.blit(self.bullets_img, self.bullets_img_rect)

        if self.bullets_img_rect.left > 0:
            self.bullets_img_rect.left -= self.bullets_velocity

class Man:
    velocity = 15;

    def __init__(self):
        self.man_img = pygame.image.load(r'C:\Users\RANVEER\Desktop\PYTHON\Game using python\Game Project\Gun Shot Game\boyGunShoot.png');
        self.man_img_rect = self.man_img.get_rect()
        self.man_img_rect.left = 20
        self.man_img_rect.top = HEIGHT/2 - 100
        self.Down = True
        self.Up = False

    def update(self):
        screenWin.blit(self.man_img, self.man_img_rect)
        if self.man_img_rect.top <= self.velocity:
            game_over()
            if SCORE > self.man_score:
                self.man_score = SCORE
        if self.man_img_rect.bottom >= HEIGHT - self.velocity:
            game_over()
            if SCORE > self.man_score:
                self.man_score = SCORE
        if self.Up:
            self.man_img_rect.top -= 10
        if self.Down:
            self.man_img_rect.bottom += 10


def game_over():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound(r'C:\Users\RANVEER\Desktop\PYTHON\Game using python\Game Project\Gun Shot Game\death_sound.wav')
    music.play()
    topscore.top_score(SCORE)
    game_over_img = pygame.image.load(r'C:\Users\RANVEER\Desktop\PYTHON\Game using python\Game Project\Gun Shot Game\endGunShoot.png');
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (WIDTH/2, HEIGHT/2)
    screenWin.blit(game_over_img, game_over_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                music.stop()
                game_loop()
        pygame.display.update()


def start_game():
    screenWin.fill(WHITE)
    start_img = pygame.image.load(r'C:\Users\RANVEER\Desktop\PYTHON\Game using python\Game Project\Gun Shot Game\startGunShoot.png');
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (WIDTH/2, HEIGHT/2)
    screenWin.blit(start_img, start_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()

def check_level(SCORE):
    global LEVEL
    NEW_FPS = 10;
    if SCORE in range(0, 10):
        LEVEL = 1
        NEW_FPS = 25;
    elif SCORE in range(10, 20):
        LEVEL = 2
        NEW_FPS = 20;
    elif SCORE in range(20, 30):
        LEVEL = 3
        NEW_FPS = 15;
    elif SCORE in range(30, 40):    
        LEVEL = 4
        NEW_FPS = 10;
    else:
        LEVEL = SCORE // 10;
        NEW_FPS = 5;
    return NEW_FPS;


def game_loop():
    while True:
        global gun;
        gun = Gun()
        bullets = Bullets()
        man = Man()
        add_new_bullet_counter = 0
        global SCORE
        SCORE = 0
        global  HIGH_SCORE
        bullets_list = []
        pygame.mixer.music.load(r'C:\Users\RANVEER\Desktop\PYTHON\Game using python\Game Project\Gun Shot Game\start_sound.wav');
        pygame.mixer.music.play(-1, 0.0)
        while True:
            screenWin.fill(WHITE)
            NEW_FPS = check_level(SCORE);
            gun.gunShoot()
            add_new_bullet_counter += 1

            if add_new_bullet_counter == NEW_FPS:
                add_new_bullet_counter = 0
                new_bullet = Bullets()
                bullets_list.append(new_bullet)
            for f in bullets_list:
                if f.bullets_img_rect.left <= 0:
                    bullets_list.remove(f)
                    SCORE += 1
                f.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        man.Up = True
                        man.Down = False
                    elif event.key == pygame.K_DOWN:
                        man.Down = True
                        man.Up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        man.Up = False
                        man.Down = True
                    elif event.key == pygame.K_DOWN:
                        man.Down = True
                        man.Up = False

            score_font = font.render('Score:'+str(SCORE), True, RED)
            score_font_rect = score_font.get_rect()
            score_font_rect.center = (200, 0 + score_font_rect.height/2)
            screenWin.blit(score_font, score_font_rect)

            level_font = font.render('Level:'+str(LEVEL), True, RED)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (500, 0 + score_font_rect.height/2)
            screenWin.blit(level_font, level_font_rect)

            top_score_font = font.render('Top Score:'+str(topscore.high_score),True,RED)
            top_score_font_rect = top_score_font.get_rect()
            top_score_font_rect.center = (800, 0 + score_font_rect.height/2)
            screenWin.blit(top_score_font, top_score_font_rect)

            man.update();
            for f in bullets_list:
                if f.bullets_img_rect.colliderect(man.man_img_rect):
                    game_over()
                    if SCORE > man.man_score:
                        man.man_score = SCORE
            pygame.display.update()
            CLOCK.tick(FPS)

start_game();
