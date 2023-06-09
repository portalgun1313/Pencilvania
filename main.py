#To-Do: Add Items, Add the Ability to Damage Entities, Add 1,-7
#music cause its too big for github: https://drive.google.com/file/d/1b6w6JaQoNO0F1eqwfIXyS1vjeDIy_RRw/view?usp=share_link

import pygame, sys
from pygame.locals import QUIT
from pygame import mixer

pygame.mixer.pre_init(33100, -16, 2, 512)
pygame.init()
mixer.init() #bruv

clock = pygame.time.Clock()
fps = 60

#define variables
pygame.mixer.music.load("area0music.mp3")
pygame.mixer.music.play(1,0.0,5000)
tile_size = 32
game_over = 0
levelTime = 0

DISPLAYSURF = pygame.display.set_mode((768, 768))
pygame.display.set_caption('Pencilvania')

#define font thingamajigs
font_victory = pygame.font.SysFont('JMH Typewriter Font',30)

#define COLORS (not colours)
green = (200,255,127)

def drawText(text,font,text_color,x,y):
  img = font.render(text,True, text_color)
  DISPLAYSURF.blit(img,(x,y))

#load sounds
death_fx = pygame.mixer.Sound("deathsound.mp3")
death_fx.set_volume(3)
#load images
enemy_image = pygame.image.load("enemy1.png")
enemy_image = pygame.transform.scale(enemy_image,(100,100))
enemy_image_rect = enemy_image.get_rect()
area0background = pygame.image.load("area0background.png")
area3background = pygame.image.load("area3background.png")
fourw_tile = pygame.image.load("4w.png")
zeroa_tile = pygame.image.load("0a.png")
zeroq_tile = pygame.image.load("0q.png")
zerot_tile = pygame.image.load("0t.png")
zerob_tile = pygame.image.load("0b.png")
zerod_tile = pygame.image.load("0d.png")
zeroc_tile = pygame.image.load("0c.png")
zeror_tile = pygame.image.load("0r.png")
zeros_tile = pygame.image.load("0s.png")
zerop_tile = pygame.image.load("0p.png")
onea_tile = pygame.image.load("1a.png")
oneb_tile = pygame.image.load("1b.png")
onec_tile = pygame.image.load("1c.png")
oned_tile = pygame.image.load("1d.png")
onee_tile = pygame.image.load("1e.png")
onef_tile = pygame.image.load("1f.png")
oneg_tile = pygame.image.load("1g.png")
oneh_tile = pygame.image.load("1h.png")
onei_tile = pygame.image.load("1i.png")
thred_tile = pygame.image.load("world3_07.png")
threu_tile = pygame.image.load("world3_05.png")
threl_tile = pygame.image.load("world3_06.png")
threr_tile = pygame.image.load("world3_08.png")
threb_tile = pygame.image.load("world3_00.png")
sixc_tile = pygame.image.load("world6_07.png")
enemyMoving = False
e1posx = 0

#Setting Map Coords (starting coords are 1,-5)
xroom = -3
yroom = -6
level_coords = [xroom,yroom]
zonen = 1

class Player():
  def __init__(self,x,y):
    img = pygame.image.load("player1.png")
    self.image = pygame.transform.scale(img, (36,60))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.dead_image = pygame.image.load("player1.png")
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.vel_x = 0
    self.vel_y = 0
    self.jumped = False
    self.canJump = 0
    self.health = 100
    self.maxHealth = 100
    self.damage = 12.5
    self.canAttack = True
    self.attacking = False
    self.jumpHeight = 12
    self.respawnPoint = [64,704,1,5]
    self.inventory = []
    self.powerUps = ["rubbereraser"]
    self.coinCount = 0
    self.deathCount = 0
    self.winnerWinnerChickenDinner = 0

  def reset(self, x, y):
    img = pygame.image.load("player1.png")
    self.image = pygame.transform.scale(img, (36,60))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.dead_image = pygame.image.load("player1.png")
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.vel_x = 0
    self.vel_y = 0
    self.jumped = False
    self.canJump = 0
    self.hasImmunity = False
    self.attacking = False

  def update(self, game_over, xroom, yroom):
    level_coords = [xroom,yroom]
    if game_over == 0: 
    
      if player.health > player.maxHealth:
        player.health = player.maxHealth
      
      if self.powerUps.count("rubbereraser") != 0:
        self.jumpHeight = 13
        self.maxHealth = 110
      
      #get key presses
      key = pygame.key.get_pressed()
      if key[pygame.K_SPACE] and self.jumped == False and self.canJump == 1:
        self.vel_y = self.jumpHeight * -1
        self.jumped = True
        self.canJump = 0
      if not key[pygame.K_SPACE]:
        self.jumped = False
      if key[pygame.K_a]:
        self.vel_x = -12
      if key[pygame.K_d]:
        self.vel_x = 12
      if key[pygame.K_x] and self.attacking == False and self.canAttack == True:
        self.canAttack = False
        self.attacking = True
      if not key[pygame.K_x]:
        self.canAttack = True
  
        #acceleration stuff too cool for you to understand
      self.vel_x *= 0.5
      if self.vel_x < 0.5:
        self_vel_x = 0
      dx = self.vel_x
      self.vel_y += 1
      if self.vel_y > 30:
        self.vel_y = 30
      dy = self.vel_y
      #check collision
      for tile in world.tile_list:
          #check for collision in x direction
        if tile[1].colliderect(self.rect.x + self.vel_x, self.rect.y, self.width, self.height):
          if dx != 0:
            self.rect.x -= abs(dx)/dx
          dx = 0
          #check for collision in y direction
        if tile[1].colliderect(self.rect.x, self.rect.y + self.vel_y, self.width, self.height):
            #check if below the ground i.e. jumping
          if self.vel_y < 0:
            dy = tile[1].bottom - self.rect.top
            self.vel_y = 0
          elif self.vel_y >= 0:
            dy = tile[1].top - self.rect.bottom
            self.vel_y = 0
            self.jumped = False
            self.canJump = 1
          

        #check for collision with enemies & spikes
        if pygame.sprite.spritecollide(self,checkpoint_group,False):
          self.respawnPoint = [self.rect.x,self.rect.y,xroom,yroom]
          self.health = self.maxHealth
        if pygame.sprite.spritecollide(self, enemy1_group, False):
          if self.hasImmunity == False:
            self.health -= (25+10*zonen)
            print(self.health)
            self.hasImmunity = True
        if pygame.sprite.spritecollide(self, spike_group, False):
          if self.hasImmunity == False:
            self.health -= (75+25*zonen)
            print(self.health)
            self.hasImmunity = True
        if not pygame.sprite.spritecollide(self, spike_group, False) and not pygame.sprite.spritecollide(self, enemy1_group, False):
          self.hasImmunity = False
        if pygame.sprite.spritecollide(self, jumpring_group, False):
          self.canJump = 1
        if not pygame.sprite.spritecollide(self, jumpring_group, False) and not tile[1].colliderect(self.rect.x, self.rect.y + self.vel_y, self.width, self.height) and dy != 0:
          self.canJump = 0
        if pygame.sprite.spritecollide(self, topexit_group, False):
          game_over = 1
          yroom += 1
          print(level_coords)
          player.reset(self.rect.x,640)
        if pygame.sprite.spritecollide(self, bottomexit_group, False):
          game_over = 1
          yroom -= 1
          print(level_coords)
          player.reset(self.rect.x,64)
        if pygame.sprite.spritecollide(self, rightexit_group, False):
          game_over = 1
          xroom += 1
          print(level_coords)
          player.reset(64,self.rect.y)
        if pygame.sprite.spritecollide(self, leftexit_group, False):
          game_over = 1
          xroom -= 1
          print(level_coords)
          player.reset(640 ,self.rect.y)
        if pygame.sprite.spritecollide(self, rubbereraserupgrade_group, True):
          self.powerUps.append("rubbereraser")
          print(self.powerUps)
        if pygame.sprite.spritecollide(self, coin_group, True):
          self.coinCount += 1
          self.winnerWinnerChickenDinner = 1
          print("----------")
          if self.powerUps.count("rubbereraser") != 0 and self.deathCount < 150:
            points = round((100-self.deathCount))+50
          else:
            points = 0
          if self.deathCount == 0 and self.powerUps.count("rubbereraser") != 0:
            print("Perfect run!")
          elif self.deathCount == 0 and self.powerUps.count("rubbereraser") != 0:
            print("Well done! But you forgot an item along the way. Go back and try to find it.")
          else:
            print("Points:",points) 
          print("-----------")
          print("You win! Congratulations!")
          print("----------")
          print("Thank you for playing Pencilvaina!")
          print("----------")
          print("Game, artwork, and concepts all made by Robert Bunker and Carson Jurgaitis")
          print("----------")
      


        if self.health <= 0:
          game_over = 1
          xroom = self.respawnPoint[2]
          yroom = self.respawnPoint[3]
          self.deathCount += 1
          player.reset(self.respawnPoint[0],self.respawnPoint[1])
          death_fx.play()
      

          

      #update player coords
      self.rect.x += dx
      self.rect.y += dy
  #draw player onto screen
    elif game_over == 1:
      game_over = 0
    DISPLAYSURF.blit(self.image, self.rect)
    return [game_over,xroom,yroom]



class World():
  def __init__(self, data):
      self.tile_list = []

      row_count = 0
      for row in data:
        col_count = 0
        for tile in row:
          if tile != 0:
            if tile == 1:
              img = pygame.transform.scale(fourw_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "0a":
              img = pygame.transform.scale(zeroa_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "0q":
              img = pygame.transform.scale(zeroq_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "0t":
              img = pygame.transform.scale(zerot_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "0b":
              img = pygame.transform.scale(zerob_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "0d":
              img = pygame.transform.scale(zerod_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "0c":
              img = pygame.transform.scale(zeroc_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "0r":
              img = pygame.transform.scale(zeror_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "0s":
              img = pygame.transform.scale(zeros_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "0p":
              img = pygame.transform.scale(zerop_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "1a":
              img = pygame.transform.scale(onea_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "1b":
              img = pygame.transform.scale(oneb_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "1c":
              img = pygame.transform.scale(onec_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "1d":
              img = pygame.transform.scale(oned_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "1e":
              img = pygame.transform.scale(onee_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "1f":
              img = pygame.transform.scale(onef_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "1g":
              img = pygame.transform.scale(oneg_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "1h":
              img = pygame.transform.scale(oneh_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "1i":
              img = pygame.transform.scale(onei_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "3b":
              img = pygame.transform.scale(threb_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "3u":
              img = pygame.transform.scale(threu_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "3l":
              img = pygame.transform.scale(threl_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "3d":
              img = pygame.transform.scale(thred_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "3r":
              img = pygame.transform.scale(threr_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
              self.tile_list.append(tile)
            if tile == "6c":
              img = pygame.transform.scale(sixc_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
            if tile == "s1":
              spike = Spike(col_count * tile_size, row_count * tile_size + 11,1)
              spike_group.add(spike)
            if tile == "s2":
              spike = Spike(col_count * tile_size, row_count * tile_size + 11,2)
              spike_group.add(spike)
            if tile == "s3":
              spike = Spike(col_count * tile_size, row_count * tile_size + 11,3)
              spike_group.add(spike)
            if tile == "e1":
              enemy1 = Enemy(col_count * tile_size, row_count * tile_size + 15)
              enemy1_group.add(enemy1)
            if tile == "j":
              jumpring = JumpRing(col_count * tile_size, row_count * tile_size)
              jumpring_group.add(jumpring)
            if tile == "tx":
              topexit = TopExit(col_count * tile_size, row_count * tile_size)
              topexit_group.add(topexit)
            if tile == "bx":
              bottomexit = BottomExit(col_count * tile_size, row_count * tile_size)
              bottomexit_group.add(bottomexit)
            if tile == "rx":
              rightexit = RightExit(col_count * tile_size, row_count * tile_size)
              rightexit_group.add(rightexit)
            if tile == "lx":
              leftexit = LeftExit(col_count * tile_size, row_count * tile_size)
              leftexit_group.add(leftexit)
            if tile == "cz":
              checkpoint = Checkpoint(col_count * tile_size, row_count * tile_size)
              checkpoint_group.add(checkpoint)
            if tile == "rubbereraserupgrade":
              rubbereraserupgrade = RubberEraserUpgradeItem(col_count * tile_size, row_count * tile_size)
              rubbereraserupgrade_group.add(rubbereraserupgrade)
            if tile == "c":
              if player.coinCount < 1:
                coin = Coin(col_count * tile_size, row_count * tile_size)
                coin_group.add(coin)
          col_count += 1
        row_count += 1


  def draw(self):
    for tile in self.tile_list:
      DISPLAYSURF.blit(tile[0],tile[1])


class Enemy(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    self.health = 50
    self.image = pygame.image.load("slime1.png")
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.width = 32
    self.height = 16
    self.move_direction = 4
    
  def update(self):
    self.rect.x += self.move_direction
    for tile in world.tile_list:
          #check for collision in x direction
        if tile[1].colliderect(self.rect.x + self.move_direction, self.rect.y, self.width, self.height):
          self.move_direction *= -1
    if player.attacking == True and player.rect.colliderect(self.rect.x - self.width, self.rect.y - self.height, self.width*2, self.height*2):
      self.health -= player.damage
      player.attacking = False
      print(self.health)
    if self.health <= 0:
      self.rect.y += 2000



class Spike(pygame.sprite.Sprite):
  def __init__(self,x,y,variant):
    pygame.sprite.Sprite.__init__(self)
    if variant == 1:
      img = pygame.image.load("spike1.png")
    elif variant == 2:
      img = pygame.image.load("spike2.png")
    elif variant == 3:
      img = pygame.image.load("spike3.png")
    self.image = pygame.transform.scale(img, (tile_size,tile_size // 1.5))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.move_direction = 4
    self.move_counter = 0

class JumpRing(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load("jumpring.png")
    self.image = pygame.transform.scale(img, (tile_size,tile_size))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class TopExit(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load("verticalexit.png")
    self.image = pygame.transform.scale(img, (2*tile_size,tile_size))
    self.rect = self.image.get_rect()
    self.rect.x = x 
    self.rect.y = y
class BottomExit(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load("verticalexit.png")
    self.image = pygame.transform.scale(img, (2*tile_size,tile_size))
    self.rect = self.image.get_rect()
    self.rect.x = x 
    self.rect.y = y
class RightExit(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load("horizontalexit.png")
    self.image = pygame.transform.scale(img, (tile_size,tile_size*2))
    self.rect = self.image.get_rect()
    self.rect.x = x 
    self.rect.y = y
class LeftExit(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load("horizontalexit.png")
    self.image = pygame.transform.scale(img, (tile_size,tile_size*2))
    self.rect = self.image.get_rect()
    self.rect.x = x 
    self.rect.y = y

class Checkpoint(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load("checkpoint.png")
    self.image = pygame.transform.scale(img, (tile_size,tile_size))
    self.rect = self.image.get_rect()
    self.rect.x = x 
    self.rect.y = y

class RubberEraserUpgradeItem(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load("rubbereraserupgrade.png")
    self.image = pygame.transform.scale(img, (tile_size*2,tile_size*2))
    self.rect = self.image.get_rect()
    self.rect.x = x 
    self.rect.y = y
class Coin(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load("world3coin.png")
    self.image = pygame.transform.scale(img, (tile_size,tile_size))
    self.rect = self.image.get_rect()
    self.rect.x = x 
    self.rect.y = y

  
def getLevel(zonen,level_coords):
    if level_coords == [5,-3]:
      zonen = 0
      world_data = [
          ["0s","tx",0,"0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","s1","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"s1","0b"],
          ["0d",0,0,0,0,"j","j","j",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"s1","0b"],
          ["0d",0,0,0,0,"s1","s1","s1",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,"0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a",0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"0a","0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,"0a","0a","0a","0a","0a",0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,"0a","0a",0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,"0a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d","0a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d","0a","0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d","0a","0a","0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d","0a","0a","0a","0a",0,0,0,0,0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,"0a",0,0,0,"0a","0a",0,0,"e1",0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"0a",0,0,0,0,"0a","0a","0a","0a","0a","0a","0a","0a","0a","0p"],
          ["0d",0,0,0,0,0,"0a","0a","0a","s1","s1","s1","s1","s1","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"],
          ["0d",0,0,0,0,"0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"],
          ["0d",0,"cz",0,"0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [5,-2]:
          zonen = 0
          world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["0d",0,0,0,0,0,0,0,0,"j","0a","0a","0a","0a",0,0,0,0,0,0,0,0,0,0],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,"0p",0,0,0,0,0,0,"0p","0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,"0p",0,0,0,0,0,0,"0p","0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,"0p",0,0,0,0,0,0,"0p","0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,"0p",0,0,0,0,0,0,"0p","0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,"0p",0,0,0,0,0,0,"0p","0b"],
          ["0d",0,0,0,"j","j","j","j","j","j","s1",0,0,0,0,0,0,"0p",0,0,0,0,0,"0b"],
          ["0d",0,0,0,"j","j","s1","s1","s1","s1","0p",0,0,0,0,0,0,"0p",0,0,0,0,0,"0b"],
          ["0d",0,0,0,"j","j","s1","s1","s1","s1","0p",0,0,0,0,0,0,"0p",0,0,0,0,0,"0b"],
          ["0d",0,0,0,"j","j","s1","s1","s1","s1","0p",0,0,0,"j",0,"0p",0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,"j","j","j","j","j","j","j","j","j","j","j",0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j","j","j","j","j","j","0a",0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j","j","j","j","j","j",0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j","0a","0a","0a","0a","0a",0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,"j","0p",0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,"j","0p",0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,"j","0p","e1","e1","e1",0,0,0,0,0,0,0,0,0,"0p"],
          ["0t","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","bx",0,"0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a"]
          ]
    elif level_coords == [6,-2]:
          zonen = 0
          world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d","0a","0a","0a","0a",0,0,0,0,0,0,"0a",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0p",0,0,0,0,0,0,"0p",0,"j",0,"s1",0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0p",0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0p","0a","0a","0a","0a","0a","0a","0p","s1",0,"j",0,"s1",0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a","s1",0,0,"s1 ","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","s1",0,0,"s1","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","s1","cz",0,"s1","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","s1",0,0,"s1","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","s1",0,0,"s1","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","s1",0,0,"s1","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","s1",0,0,0,"rx"],
          ["0d",0,0,0,0,0,"e1",0,0,0,0,0,0,0,0,0,0,0,"0p","s1",0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [7,-2]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,"0a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,"0a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"s1","s1",0,0,"0p","s1",0,0,0,0,"j",0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0a","0a",0,0,0,0,0,"0a","0a",0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"j",0,0,"s1","s1",0,0,"j",0,0,0,0,0,0,"s1",0,0,0,0,"0p"],
          ["lx",0,0,0,"s1",0,0,0,0,0,0,"s1",0,0,0,0,0,"0a","0a",0,0,0,0,"0p"],
          [0,0,"cz",0,"0a",0,0,0,0,0,0,"0a",0,0,0,0,0,0,"e1",0,0,0,0,"0p"],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [903,11]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [0,1]:
        zonen = 0
        world_data = [
          ["0s","tx",0,"0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","s1","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"s1","0b"],
          ["0d",0,0,0,0,"j","j","j",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"s1","0b"],
          ["0d",0,0,0,0,"s1","s1","s1",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,"0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a",0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"0a","0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,"0a","0a","0a","0a","0a",0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,"0a","0a",0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,"0a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d","0a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d","0a","0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d","0a","0a","0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d","0a","0a","0a","0a",0,0,0,0,0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,"0a",0,0,0,"0a","0a",0,0,"e1",0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"0a",0,0,0,0,"0a","0a","0a","0a","0a","0a","0a","0a","0a","0p"],
          ["0d",0,0,0,0,0,"0a","0a","0a","s1","s1","s1","s1","s1","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"],
          ["0d",0,0,0,0,"0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"],
          ["0d",0,"c",0,"0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [0,2]:
          zonen = 0
          world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["0d",0,0,0,0,0,0,0,0,"j","0a","0a","0a","0a",0,0,0,0,0,0,0,0,0,0],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,"0p",0,0,0,0,0,0,"0p","0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,"0p",0,0,0,0,0,0,"0p","0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,"0p",0,0,0,0,0,0,"0p","0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,"0p",0,0,0,0,0,0,"0p","0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,"0p",0,0,0,0,0,0,"0p","0b"],
          ["0d",0,0,0,"j","j","j","j","j","j","s1",0,0,0,0,0,0,"0p",0,0,0,0,0,"0b"],
          ["0d",0,0,0,"j","j","s1","s1","s1","s1","0p",0,0,0,0,0,0,"0p",0,0,0,0,0,"0b"],
          ["0d",0,0,0,"j","j","s1","s1","s1","s1","0p",0,0,0,0,0,0,"0p",0,0,0,0,0,"0b"],
          ["0d",0,0,0,"j","j","s1","s1","s1","s1","0p",0,0,0,"j",0,"0p",0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,"j","j","j","j","j","j","j","j","j","j","j",0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j","j","j","j","j","j","0a",0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j","j","j","j","j","j",0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j","0a","0a","0a","0a","0a",0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,"j","0p",0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,"j","0p",0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,"j","0p","e1","e1","e1",0,0,0,0,0,0,0,0,0,"0p"],
          ["0t","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a","0a"]
          ]
    elif level_coords == [1,2]:
          zonen = 0
          world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d","0a","0a","0a","0a",0,0,0,0,0,0,"0a",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0p",0,0,0,0,0,0,"0p",0,"j",0,"s1",0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0p",0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0p","0a","0a","0a","0a","0a","0a","0p","s1",0,"j",0,"s1",0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a","s1",0,0,"s1 ","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","s1",0,0,"s1","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","s1","cz",0,"s1","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","s1",0,0,"s1","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","s1",0,0,"s1","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","s1",0,0,"s1","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","s1",0,0,0,"rx"],
          ["0d",0,0,0,0,0,"e1",0,0,0,0,0,0,0,0,0,0,0,"0p","s1",0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [2,2]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,"0a",0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,"0a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,"0a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"s1","s1",0,0,"0p","s1",0,0,0,0,"j",0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0a","0a",0,0,0,0,0,"0a","0a",0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"j",0,0,"s1","s1",0,0,"j",0,0,0,0,0,0,"s1",0,0,0,0,"0p"],
          ["0d",0,0,0,"s1",0,0,0,0,0,0,"s1",0,0,0,0,0,"0a","0a",0,0,0,0,"0p"],
          ["0d",0,0,0,"0a",0,0,0,0,0,0,"0a",0,0,0,0,0,0,"e1",0,0,0,0,"0p"],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [3,2]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [1,-5]:
          zonen = 0
          world_data = [
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,"cz",0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [2,-5]:
        zonen = 0
        world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,"0a","0a","0a","0a","0a",0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,"s1","s1","s1","s1","s1","s1",0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [3,-5]:
        zonen = 0
        world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          [0,0,0,0,0,0,0,"s1",0,0,0,0,"s1",0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","bx",0,"0p","0p"]
          ]
    elif level_coords == [3,-6]:
        zonen = 0
        world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","tx",0,"0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","0p","0p","0p",'0p',"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,"0p","0p",0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0p","0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["0d",0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [4,-6]:
        zonen = 0
        world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [5,-6]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,"0a","0a",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,"s1",0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,'0a',0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [6,-6]:
          zonen = 0
          world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,"0a","0a",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,"rubbereraserupgrade",0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,"s1",0,0,0,0,0,0,0,0,0,"0a",0,0,"0p"],
          [0,0,0,0,0,0,0,0,0,0,'0a',0,0,0,0,0,0,0,0,"0a",'0p',"0a",0,"0p"],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [0,-5]:
        zonen = 0
        world_data = [
          ["0s","tx",0,"0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d","0p","0p",0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d","0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","bx",0,"0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [0,-6]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","tx",0,"0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,"0p","0p","0p","0p",0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d","0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,"0p",0,"s1",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0p","0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,'0p',0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,"0p",0,"s1",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,"0p","0p",'0p',"0p",0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [1,-6]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","bx",0,"0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [2,-5]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,"0a","0a","0a","0a","0a",0,0,0,0,0,0,0,0,"0p"],
          [0,0,0,0,0,0,0,0,"0a","0a","0a","0a","0a","0a","0a",0,0,0,0,0,0,0,0,"0p"],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [-1,-6]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [-2,-6]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [0,-4]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"s1",0,"s1",0,0,0,0],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,"0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,"0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"],
          ["0d",0,0,0,0,0,0,"0p",'0p',"0p",'0p',"0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p",'0p'],
          ["0t","bx",0,"0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [1,-4]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,"cz",0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,"0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p",0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0d","0p","0p","0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p","0p","0p","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0p'],
          ["0t","bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"0p"]
          ]
    elif level_coords == [-1,-5]:
      zonen = 0
      world_data = [
          ["0s","tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [-1,-4]:
      zonen = 0
      world_data = [
          ["0s","tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"tx",0,"0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0t","bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"0p"]
          ]
    elif level_coords == [-1,-3]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          [0,0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",'0p',"0p","0p","0p","0p","0p","0p","0p","0p","0p","j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0t","bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"bx",0,"0p"]
          ]
    elif level_coords == [2,-4]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [3,-4]:
      zonen = 0
      world_data = [
          ["0s","tx",0,"0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d","0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p",0,"0p"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [3,-3]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","bx",0,"0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [4,-3]:
      zonen = 0
      world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0p"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [8,-2]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","tx",0,"3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b","3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b","3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,"3l"],
          ["lx",0,0,0,0,0,0,0,0,0,"3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3l"],
          [0,0,0,0,0,0,0,0,0,"3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3l"],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [8,-1]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","tx",0,"3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,"3b",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","bx",0,"3u"]
          ]
    elif level_coords == [8,0]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","bx",0,"3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [7,0]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","tx",0,"3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,'3b',0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,'3b','3b',"3b",0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,"3b","3b","3b",0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,"3b","3b",0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,"3b","3b",0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,"j","3b",0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,"3b","3b",0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,"3b","3b","3b","3b",0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,"3l"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b","3b","3b",0,0,0,0,0],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [6,0]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [5,0]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["3u","3u","3u","3u","bx",0,"3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [9,-1]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [9,0]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [10,0]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","tx",0,"3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b","3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b","3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,"3l"],
          ["lx",0,0,0,0,0,0,0,0,0,"3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3l"],
          [0,0,0,0,0,0,0,0,0,"3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3b","3l"],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [10,1]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","bx",0,"3u"]
          ]
    elif level_coords == [9,1]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [7,1]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","bx",0,"3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [6,1]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [8,1]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","tx",0,"3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'3b',"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3b",0,0,"3b",0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,"3b","3b",0,0,0,0,0,0,0,0,0,"3l"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          [0,0,0,0,0,"cz",0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [8,2]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["lx",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3u","3u","3u","3u","3u","3u","3u","3u","bx",0,"3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [7,2]:
      zonen = 3
      world_data = [
          ["3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d","3d"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,"c",0,0,0,0,0,0,0,0,0,0,0,0,0,"3l"],
          ["3r",0,0,0,0,0,0,0,0,"3b",0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["3r",0,0,0,0,0,0,0,"3b","3b","3b",0,0,0,0,0,0,0,0,0,0,0,0,0],
          ["3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u","3u"]
          ]
    elif level_coords == [-3,-6]:
      zonen = 1
      world_data = [
          ["1e","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","tx",0,"1e"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"j","1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1g","1a","1a","1a","1a","1a","1a","1a","1e"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,"1a","1c","1c","1c","1c","1c","1c","1c","1c","1e"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,"1g","1f",0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,"1h","1i",0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,"1a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d","1a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"rx"],
          ["1d",0,0,0,0,0,"1a",0,0,0,0,"cz",0,0,'s3',0,0,0,0,0,0,0,0,0],
          ["1e","1a","1a","1a","1a","1a","1e","1a","1a","1a","1a","1a","1a","1a","1a","1a","1a","1a","1a","1a","1a","1a","1a","1e"]
        ]
    elif level_coords == [-3,-5]:
        zonen = 1
        world_data = [
          ["1e","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","1c","tx",0,"1e"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"j","1b"],
          ["1d",0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1g","1a","1a","1a","1a","1a","1a","1a","1e"],
          ["1d",0,0,0,0,"1a",0,0,0,"s3","s3",0,0,0,0,"1h","1c","1c","1c","1c","1c","1c","1c","1e"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1e","1f",0,0,0,0,0,0,0,"1g","1f",0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1e","1i",0,0,0,0,0,0,0,"1h","1i",0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d","s3","s3","s3",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,"s3",0,0,"1a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,"s3",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,"s3",0,"j","j",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d",0,0,"s3",0,0,"s3",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1d","e1","e1","1a","s3","s3","1a",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"1b"],
          ["1e","1a","1a","1e","1a","1a","1e","1a","1a","1a","1a","1a","1a","1a","1a","1a","1a","1a","1a","1a","1a","bx",0,"1e"]
        ]
    
    return [zonen, world_data]


world_data = getLevel(zonen,level_coords)[1]
player = Player(384, 704)

enemy1_group = pygame.sprite.Group()
spike_group = pygame.sprite.Group()
jumpring_group = pygame.sprite.Group()
topexit_group = pygame.sprite.Group()
bottomexit_group = pygame.sprite.Group()
rightexit_group = pygame.sprite.Group()
leftexit_group = pygame.sprite.Group()
checkpoint_group = pygame.sprite.Group()
rubbereraserupgrade_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

def draw_grid():
  for line in range(0,25):
    pygame.draw.line(DISPLAYSURF,(255,255,255), (0, line * tile_size),(768, line * tile_size))
    pygame.draw.line(DISPLAYSURF,(255,255,255), (line * tile_size, 0),(line * tile_size, 768))

def healthUI(health):
  if health < 0:
    health = 0
  healthbar = pygame.image.load("healthbar.png")
  healthbar = pygame.transform.scale(healthbar,(health*3, 16))
  DISPLAYSURF.blit(healthbar,(3,3))
def maxHealthUI(maxhealth):
  maxhealthframe = pygame.image.load("healthbar.png")
  maxhealthframe = pygame.transform.scale(maxhealthframe,(maxhealth*3+6, 22))
  maxhealthframe_rect = maxhealthframe.get_rect()
  pygame.draw.rect(DISPLAYSURF,(0,0,0), maxhealthframe_rect, maxhealth)
def drawBackground(zonen):
  if zonen == 0:
    background = pygame.image.load("area0background.png")
  elif zonen == 1:
    background = pygame.image.load("area1background.png")
  elif zonen == 3:
    background = pygame.image.load("area3background.png")
  background = pygame.transform.scale(background, (768,768))
  DISPLAYSURF.blit(background,(0,0))






world = World(world_data)


while True:
  clock.tick(fps)

  levelTime += 1

  draw_grid()
  drawBackground(zonen)
  if game_over == 0:
    enemy1_group.update()
  enemy1_group.draw(DISPLAYSURF)
  spike_group.draw(DISPLAYSURF)
  jumpring_group.draw(DISPLAYSURF)
  topexit_group.draw(DISPLAYSURF)
  rightexit_group.draw(DISPLAYSURF)
  leftexit_group.draw(DISPLAYSURF)
  bottomexit_group.draw(DISPLAYSURF)
  checkpoint_group.draw(DISPLAYSURF)
  rubbereraserupgrade_group.draw(DISPLAYSURF)
  coin_group.draw(DISPLAYSURF)

  player_data = player.update(game_over,xroom,yroom)
  game_over = player_data[0]
  xroom = player_data[1]
  yroom = player_data[2]
  level_coords = [xroom,yroom]
  if game_over == 1:
    enemy1_group = pygame.sprite.Group()
    spike_group = pygame.sprite.Group()
    jumpring_group = pygame.sprite.Group()
    topexit_group = pygame.sprite.Group()
    rightexit_group = pygame.sprite.Group()
    leftexit_group = pygame.sprite.Group()
    bottomexit_group = pygame.sprite.Group()
    checkpoint_group = pygame.sprite.Group()
    rubbereraserupgrade_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()
    zonen = getLevel(zonen,level_coords)[0]
    world_data = getLevel(zonen,level_coords)[1]
    world = World(world_data)
    game_over = 0
  
  world.draw()
  maxHealthUI(player.maxHealth)
  healthUI(player.health)
  if player.winnerWinnerChickenDinner == 1:
    if player.powerUps.count("rubbereraser") != 0 and player.deathCount < 150:
      points = round((100-player.deathCount))+50
    elif player.deathCount < 150 and player.powerUps.count("rubbereraser") == 0:
      points = round((100-player.deathCount))
    else:
      points = 0
    if player.deathCount == 0 and player.powerUps.count("rubbereraser") != 0:
      drawText("Perfect run!",font_victory,green,200,200)
    elif player.deathCount == 0 and player.powerUps.count("rubbereraser") == 0:
      drawText("Well done! But you forgot an item along the way.",font_victory,green,50,200)
      drawText("Try again and find it.",font_victory,green,50,250)
    drawText("Points:",font_victory,green,50,150) 
    drawText(str(points),font_victory,green,125,150) 
    drawText("Thank you for playing Pencilvaina!",font_victory,green,50,300)
    drawText("Game, artwork, and concepts all made by",font_victory,green,50,350)
    drawText("Robert Bunker and Carson Jurgaitis",font_victory,green,50,400)
  for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
  pygame.display.update()
