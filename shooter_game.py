from pygame import *
class Pdate(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x <= 800:
            self.rect.x += 5
        if keys[K_a] and self.rect.x >= 0:
            self.rect.x -= 5
    def shoot(self):
        b1 = Bullet('bullet.png', self.rect.x+20, self.rect.y+5, 10, 20)
        fire.add(b1)
        shot.play()

class Bullet(Base):
    def update(self):
class Enemy(Base):
    def update(self):
        global health
        self.rect.y += 2
        if self.rect.y >= 600:
            self.rect.y = -50
            self.rect.x = randint(0, 750)
            health -= 1
        if sprite.spritecollide(self, fire, True):
            self.rect.y = -50
            self.rect.x = randint(0, 750)
            global score
            score += 1
        if sprite.collide_rect(self, hero):
            health -= 1
            self.rect.y = -25
            self.rect.x = randint(0, 1000)

class Boss(Base):
    def start_hp(self):
        self.hp = 10
    def update(self):
        self.rect.y += 1
        if self.rect.y >= 600 or sprite.collide_rect(self, hero):
            global health
            health = 0
        if sprite.spritecollide(self, fire, True):
            self.hp -= 1

hero = Player('roocket.png', 500, 500, 50, 100)
enem = Enemy('ufo.png',randint(0, 800), -50, 50, 50)
enem2 = Enemy('ufo.png',randint(0, 800), -50, 50, 50)
enem3 = Enemy('ufo.png',randint(0, 800), -50, 50, 50)
enem4 = Enemy('ufo.png',randint(0, 800), -50, 50, 50)

fire = sprite.Group()
enemies = sprite.Group()
enemies.add(enem, enem2, enem3, enem4)

bg = image.load('bgs.jpg')
bg = transform.scale(bg, (800, 700))
big_boss = Boss('ufo.png', 300, -200, 75, 75)  
big_boss.start_hp()
hero.shoot()

health = 5
score = 0

font.init()
shrift = font.Font(None, 35)
mixer.init()
shot = mixer.Sound('fire.ogg')

while health  > 0:
    for e in event.get():
        if e.type == QUIT:
            quit()
            exit()
        if e.type == MOUSEBUTTONDOWN:
            hero.shoot()

    
gamescreen.blit(bg, (0, 0)) 
    hero.update()
    hero.reset()

    fire.update()
    fire.draw(gamescreen)

    health_txt = shrift.render('Здоровье : ' +str(health), 1, (255, 0, 0))
    gamescreen.blit(health_txt, (0, 0))

    score_txt = shrift.render('Счёт : ' +str(score), 1, (255, 0, 0))
    gamescreen.blit(score_txt, (0, 40))


if score >= 10:
    big_boss.update()
    big_boss.reset()
    if big_boss.hp <= 0:
        gamescreen.blit(bg, (0, 0))
        end = shrift.render('ПОБЕДА', 1, (0, 255, 0))
        gamescreen.blit(end, (200, 200))
        gamescreen.blit(score_txt, (200, 250))
        display.update()
        time.delay(3000)
        quit()
        exit()
    else:
        enemies.update()
        enemies.draw(gamescreen)

    display.update()
    clock.tick(60)
gamescreen.blit(bg, (0, 0))
end = shrift.render('Поражение', 1, (0, 255, 0))
gamescreen.blit(end, (200, 200))
gamescreen.blit(score_txt, (200, 250))
display.update()
time.delay(3000)

