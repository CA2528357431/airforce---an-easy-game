import pygame
import random

bg_width=480
bg_height=700
HZ=60

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed):
        super().__init__()
        self.speed=speed
        self.image=pygame.image.load(image_name)
        self.rect=self.image.get_rect()
    def update(self):
        pass


class background(GameSprite):
    def __init__(self, image_name, speed=1):
        super().__init__(image_name, speed)
        
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y>bg_height:
            self.rect.y-=bg_height*2

class enemy(GameSprite):
    enemy_list=[]
    def __init__(self,image_name="./images/enemy.png",speed=random.randint(2,3)):
        super().__init__(image_name,speed)
        self.speeds=speed
        self.sw=random.randint(1,8)
        self.rect.x=random.randint(0,bg_width-self.rect.width)
        
        enemy.enemy_list.append(self)
    def update(self):
        if self.sw==1:
            self.rect.y+=self.speed
        elif self.sw==2:
            self.rect.y+=self.speed
            self.rect.x+=self.speeds
        elif self.sw==3:
            self.rect.y+=self.speed
            self.rect.x-=self.speeds
        elif self.sw==4:
            self.rect.y+=self.speed*2
            self.rect.x-=self.speeds
        elif self.sw==5:
            self.rect.y+=self.speed
            self.rect.x-=self.speeds*2
        elif self.sw==6:
            self.rect.y+=self.speed*2
            self.rect.x+=self.speeds
        elif self.sw==7:
            self.rect.y+=self.speed
            self.rect.x+=self.speeds*2
        elif self.sw==8:
            self.rect.y+=self.speed*2
        
        if self.rect.x<0 or self.rect.x+self.rect.width>bg_width:
            self.speeds*=(-1)

        if self.rect.y>bg_height:
            self.kill()
    
class boss1(GameSprite):
    
    die_image1=pygame.image.load("./images/boss1_down1.png")
    die_image2=pygame.image.load("./images/boss1_down2.png")
    die_image3=pygame.image.load("./images/boss1_down3.png")
    die_image4=pygame.image.load("./images/boss1_down4.png")
    die_image5=pygame.image.load("./images/boss1_down5.png")
    die_image6=pygame.image.load("./images/boss1_down6.png")

    def __init__(self,image_name="./images/boss1.png",speed=0):
        super().__init__(image_name,speed)
        self.rect.x=random.randint(0,bg_width-self.rect.width)
        self.rect.y=random.randint(0,bg_height-200-self.rect.height)
        self.health=100
        self.timer=0
    def update(self):
        self.rect.x=random.randint(0,bg_width-self.rect.width)
        self.rect.y=random.randint(0,bg_height-200-self.rect.height)
    
    

    

class boss2(boss1):
    die_image1=pygame.image.load("./images/boss2_down1.png")
    die_image2=pygame.image.load("./images/boss2_down2.png")
    die_image3=pygame.image.load("./images/boss2_down3.png")
    die_image4=pygame.image.load("./images/boss2_down4.png")
   
    def __init__(self, image_name='./images/boss2.png', speed=0):
        super().__init__(image_name=image_name, speed=speed)
        self.health=30
        
class hero(GameSprite):
    die_image1 = pygame.image.load("./images/hero_down1.png")
    die_image2 = pygame.image.load("./images/hero_down2.png")
    die_image3 = pygame.image.load("./images/hero_down3.png")
    die_image4 = pygame.image.load("./images/hero_down4.png")

    def __init__(self,image_name="./images/hero.png",speed=0):
        super().__init__(image_name,speed=10)
        self.rect.x=bg_width/2-self.rect.width/2
        self.rect.y=bg_height-200
        self.health=1000
        self.timer=0
    def update(self):
        press=pygame.key.get_pressed()
        if press[pygame.K_RIGHT]==1:
            self.rect.x+=self.speed
        elif press[pygame.K_LEFT]==1:
            self.rect.x-=self.speed
        elif press[pygame.K_UP]==1:
            self.rect.y-=self.speed
        elif press[pygame.K_DOWN]==1:
            self.rect.y+=self.speed

        if self.rect.x<0:
            self.rect.x=0
        elif self.rect.x>bg_width-self.rect.width:
            self.rect.x=bg_width-self.rect.width
        if self.rect.y<0:
            self.rect.y=0
        elif self.rect.y>bg_height-self.rect.height:
            self.rect.y=bg_height-self.rect.height

class bullet(GameSprite):
    def __init__(self,ff,image_name,speed):
        super().__init__(image_name,speed)
        self.rect.x=ff.rect.x+ff.rect.width/2
        self.rect.y=ff.rect.y+ff.rect.height/2
class bullet1(bullet):
    def __init__(self, ff, image_name="./images/bullet1.png", speed=12):
        super().__init__(ff,image_name, speed)
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y<0 or self.rect.x<0 or self.rect.x>bg_width:
            self.kill()
class bullet2(bullet):
    def __init__(self, ff, image_name="./images/bullet2.png", speed=3):
        super().__init__(ff,image_name,speed)
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y>bg_height or self.rect.x<0 or self.rect.x>bg_width:
            self.kill()
class bullet3(bullet):
    def __init__(self, ff, image_name="./images/bullet3.png", speed=3):
        super().__init__(ff,image_name, speed)
    def update(self):
        self.rect.x-=self.speed
        if self.rect.y>bg_height or self.rect.x<0 or self.rect.x>bg_width:
            self.kill()
class bullet4(bullet):
    def __init__(self, ff, image_name="./images/bullet4.png", speed=3):
        super().__init__(ff,image_name, speed)
    def update(self):
        self.rect.x+=self.speed
        if self.rect.y>bg_height or self.rect.x<0 or self.rect.x>bg_width:
            self.kill()
class bullet5(bullet):
    def __init__(self, ff, image_name="./images/bullet5.png", speed=3):
        super().__init__(ff,image_name, speed)
    def update(self):
        self.rect.y+=self.speed
        self.rect.x-=self.speed
        if self.rect.y>bg_height or self.rect.x<0 or self.rect.x>bg_width:
            self.kill()
class bullet6(bullet):
    def __init__(self, ff, image_name="./images/bullet6.png", speed=3):
        super().__init__(ff,image_name, speed)
    def update(self):
        self.rect.y+=self.speed
        self.rect.x+=self.speed
        if self.rect.y>bg_height or self.rect.x<0 or self.rect.x>bg_width:
            self.kill()


