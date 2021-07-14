import pygame
import random
from source import *

HZ = 60

pygame.init()

create_enemy1 = pygame.USEREVENT
create_enemy2 = pygame.USEREVENT + 1
fire1 = pygame.USEREVENT + 2
fire2 = pygame.USEREVENT + 3
fire3 = pygame.USEREVENT + 4
fire = pygame.USEREVENT + 5

sound1 = pygame.mixer.Sound("./sound/bullet.wav")
sound2 = pygame.mixer.Sound("./sound/enemy.wav")
sound3 = pygame.mixer.Sound("./sound/boss1.wav")
sound4 = pygame.mixer.Sound("./sound/boss2.wav")
sound5 = pygame.mixer.Sound("./sound/game.ogg")
sound6 = pygame.mixer.Sound("./sound/success.wav")


class play:
    def __init__(self):
        self.i = 0
        self.bg = pygame.image.load("./images/background.png")
        self.bg_rect = self.bg.get_rect()
        self.screen = pygame.display.set_mode(self.bg_rect.size)
        self.clock = pygame.time.Clock()

        pygame.time.set_timer(create_enemy1, 500)
        pygame.time.set_timer(create_enemy2, 8000)
        pygame.time.set_timer(fire1, 700)
        pygame.time.set_timer(fire2, 180)
        pygame.time.set_timer(fire3, 1000)
        pygame.time.set_timer(fire, 50)

    def start(self):
        self.create_sprites()
        while True:
            self.i += 1
            self.clock.tick(HZ)
            self.event_handle()
            self.fire_check()
            self.update()

            pygame.display.update()
            if (self.boss_1 not in self.boss1_group) and (self.boss_2 not in self.boss2_group) and (
                    self.boss_3 not in self.boss2_group):
                x = pygame.image.load("./images/gameover.png")
                x_rect = x.get_rect()
                self.screen.blit(x, (self.bg_rect.width / 2 - x_rect.width / 2, self.bg_rect.height / 2))
                self.i -= 1
                sound6.play()
                pygame.display.update()

    def create_sprites(self):
        bg1 = background("./images/background.png")
        bg2 = background("./images/backgroundbc.png")
        bg2.rect.y -= self.bg_rect.height
        self.bg_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()

        self.boss_1 = boss1()
        self.boss1_group = pygame.sprite.Group(self.boss_1)

        self.boss_2 = boss2()
        self.boss_3 = boss2()
        self.boss2_group = pygame.sprite.Group(self.boss_2, self.boss_3)

        self.hero = hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        self.bullet_hero = pygame.sprite.Group()

        self.bullet_enemy = pygame.sprite.Group()

        self.enemy_body_list = pygame.sprite.Group()

        self.boss1_body_list = pygame.sprite.Group()

        self.boss2_body_list = pygame.sprite.Group()

    def event_handle(self):
        event = pygame.event.get()
        for x in event:
            if x.type == pygame.QUIT:
                play.over()
            elif x.type == create_enemy1:
                a = enemy()
                self.enemy_group.add(a)
            elif x.type == create_enemy2:
                a1 = enemy()
                self.enemy_group.add(a1)
                a2 = enemy()
                self.enemy_group.add(a2)
                a3 = enemy()
                self.enemy_group.add(a3)
                a4 = enemy()
                self.enemy_group.add(a4)
                a5 = enemy()
                self.enemy_group.add(a5)
                a6 = enemy()
                self.enemy_group.add(a6)
            elif x.type == fire1:
                b1 = bullet2(self.boss_1)
                b2 = bullet3(self.boss_1)
                b3 = bullet4(self.boss_1)
                b4 = bullet5(self.boss_1)
                b5 = bullet6(self.boss_1)
                self.bullet_enemy.add(b1, b2, b3, b4, b5)
            elif x.type == fire2:
                b1 = bullet2(self.boss_2)
                b2 = bullet2(self.boss_3)
                self.bullet_enemy.add(b1, b2)
            elif x.type == fire3:
                for y in enemy.enemy_list:
                    sw = random.randint(1, 2)
                    if sw == 1:
                        b = bullet3(y)
                    elif sw == 2:
                        b = bullet4(y)
                    self.bullet_enemy.add(b)
            elif x.type == fire:
                press = pygame.key.get_pressed()
                # 通过设置时间设置射速
                if press[pygame.K_SPACE] == 1:
                    b = bullet1(self.hero)
                    self.bullet_hero.add(b)
                    sound1.play()

    def update(self):
        # 通过物理帧数是否满足条件来达成速度小于 1单位/帧
        if self.i % 2 == 0:
            self.bg_group.update()
            self.bg_group.draw(self.screen)
        else:
            self.bg_group.draw(self.screen)

        if self.i % (HZ * 1.8) == 0:
            self.boss1_group.update()
            self.boss1_group.draw(self.screen)
        else:
            self.boss1_group.draw(self.screen)

        if self.i % (HZ * 1.1) == 0:
            self.boss2_group.update()
            self.boss2_group.draw(self.screen)
        else:
            self.boss2_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.bullet_enemy.update()
        self.bullet_enemy.draw(self.screen)

        self.bullet_hero.update()
        self.bullet_hero.draw(self.screen)

    def fire_check(self):
        if self.boss_1.timer > HZ / 2 * 6:
            pygame.sprite.groupcollide(self.enemy_group, self.bullet_hero, True, True)
            pygame.sprite.groupcollide(self.bullet_enemy, self.bullet_hero, True, True)
        if self.boss_1.health <= 0:
            pygame.sprite.groupcollide(self.boss1_group, self.bullet_hero, False, True)
            self.boss_1.timer += 1
            if self.boss_1.timer <= HZ / 2 * 1:
                self.boss_1.image = boss1.die_image1
                sound4.play()
            elif self.boss_1.timer <= HZ / 2 * 2:
                self.boss_1.image = boss1.die_image2
            elif self.boss_1.timer <= HZ / 2 * 3:
                self.boss_1.image = boss1.die_image3
            elif self.boss_1.timer <= HZ / 2 * 4:
                self.boss_1.image = boss1.die_image4
            elif self.boss_1.timer <= HZ / 2 * 5:
                self.boss_1.image = boss1.die_image5
            elif self.boss_1.timer <= HZ / 2 * 6:
                self.boss_1.image = boss1.die_image6
            else:
                self.boss_1.kill()

        else:
            if len(pygame.sprite.groupcollide(self.boss1_group, self.bullet_hero, False, True)) != 0:
                self.boss_1.health -= 1

        if self.boss_3.health <= 0:
            if self.boss_3.timer > HZ / 2 * 4:
                pygame.sprite.spritecollide(self.boss_3, self.bullet_hero, True)
            self.boss_3.timer += 1
            if self.boss_3.timer <= HZ / 2 * 1:
                self.boss_3.image = boss2.die_image1
                sound3.play()
            elif self.boss_3.timer <= HZ / 2 * 2:
                self.boss_3.image = boss2.die_image2
            elif self.boss_3.timer <= HZ / 2 * 3:
                self.boss_3.image = boss2.die_image3
            elif self.boss_3.timer <= HZ / 2 * 4:
                self.boss_3.image = boss2.die_image4
            else:
                self.boss_3.kill()

        else:
            if len(pygame.sprite.spritecollide(self.boss_3, self.bullet_hero, True)) != 0:
                self.boss_3.health -= 1

        if self.boss_2.health <= 0:
            if self.boss_2.timer > HZ / 2 * 4:
                pygame.sprite.spritecollide(self.boss_3, self.bullet_hero, True)
            self.boss_2.timer += 1
            if self.boss_2.timer <= HZ / 2 * 1:
                self.boss_2.image = boss2.die_image1
                sound3.play()
            elif self.boss_2.timer <= HZ / 2 * 2:
                self.boss_2.image = boss2.die_image2
            elif self.boss_2.timer <= HZ / 2 * 3:
                self.boss_2.image = boss2.die_image3
            elif self.boss_2.timer <= HZ / 2 * 4:
                self.boss_2.image = boss2.die_image4
            else:
                self.boss_2.kill()


        else:
            if len(pygame.sprite.spritecollide(self.boss_2, self.bullet_hero, True)) != 0:
                self.boss_2.health -= 1

        if self.hero.health <= 0:

            self.hero.timer += 1
            if self.hero.timer <= HZ / 2 * 1:
                self.hero.image = hero.die_image1
                sound2.play()
            elif self.hero.timer <= HZ / 2 * 2:
                self.hero.image = hero.die_image2
            elif self.hero.timer <= HZ / 2 * 3:
                self.hero.image = hero.die_image3
            elif self.hero.timer <= HZ / 2 * 4:
                self.hero.image = hero.die_image4
            else:
                self.hero.kill()

        else:
            if len(pygame.sprite.spritecollide(self.hero, self.enemy_group, True)) != 0:
                self.hero.health -= 1
            if len(pygame.sprite.spritecollide(self.hero, self.bullet_enemy, True)) != 0:
                self.hero.health -= 1

    @classmethod
    def over(cls):
        pygame.quit()


if __name__ == "__main__":
    game = play()
    game.start()
