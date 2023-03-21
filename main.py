import pygame, sys
from pygame.locals import QUIT

pygame.init()

clock = pygame.time.Clock()
fps = 60

#define variables
tile_size = 32
game_over = 0
xroom = 0
yroom = 2
zonen = 0

DISPLAYSURF = pygame.display.set_mode((768, 768))
pygame.display.set_caption('Pencilvania')

#load images
enemy_image = pygame.image.load("enemy1.png")
enemy_image = pygame.transform.scale(enemy_image,(100,100))
enemy_image_rect = enemy_image.get_rect()
area0background = pygame.image.load("area0background.png")
area0background = pygame.transform.scale(area0background,(768,768))
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
sixc_tile = pygame.image.load("world6_07.png")
enemyMoving = False
e1posx = 0

#Setting Map Coords
xroom = 0
yroom = 1
level_coords = [xroom,yroom]
zonen = 0

class Player():
  def __init__(self,x,y):
    img = pygame.image.load("player1.png")
    self.image = pygame.transform.scale(img, (36,60))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.dead_image = pygame.image.load("sus.png")
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.vel_x = 0
    self.vel_y = 0
    self.jumped = False
    self.canJump = 0

  def reset(self, x, y):
    img = pygame.image.load("player1.png")
    self.image = pygame.transform.scale(img, (36,60))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.dead_image = pygame.image.load("sus.png")
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.vel_x = 0
    self.vel_y = 0
    self.jumped = False
    self.canJump = 0

  def update(self, game_over, xroom, yroom):
    
    if game_over == 0: 
    
      
      
      #get key presses
      key = pygame.key.get_pressed()
      if key[pygame.K_SPACE] and self.jumped == False and self.canJump == 1:
        self.vel_y = -12
        self.jumped = True
        self.canJump = 0
      if not key[pygame.K_SPACE]:
        self.jumped = False
      if key[pygame.K_a]:
        self.vel_x = -12
      if key[pygame.K_d]:
        self.vel_x = 12
  
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
            self.canJump = 1
          

        #check for collision with enemies & spikes
        if pygame.sprite.spritecollide(self, enemy1_group, False):
          game_over = -1
        if pygame.sprite.spritecollide(self, spike_group, False):
          game_over = -1
        if pygame.sprite.spritecollide(self, jumpring_group, False):
          self.canJump = 1
        if pygame.sprite.spritecollide(self, topexit_group, True):
          game_over = 1
          yroom += 1
          player.reset(64,640)
          print(yroom)
      


      

          

      #update player coords
      self.rect.x += dx
      self.rect.y += dy
  #draw player onto screen
    elif game_over == -1:
      player.reset(64,640)
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
            if tile == "6c":
              img = pygame.transform.scale(sixc_tile, (tile_size,tile_size))
              img_rect = img.get_rect()
              img_rect.x = col_count * tile_size
              img_rect.y = row_count * tile_size
              tile = (img, img_rect)
            if tile == "s1":
              spike = Spike(col_count * tile_size, row_count * tile_size + 11)
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
          col_count += 1
        row_count += 1


  def draw(self):
    for tile in self.tile_list:
      DISPLAYSURF.blit(tile[0],tile[1])


class Enemy(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("slime1.png")
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.move_direction = 4
    self.move_counter = 0
    self.width = 32
    self.height = 16
    
  def update(self):
    self.rect.x += self.move_direction
    self.move_counter += 1
    if abs(self.move_counter) > 30:
      self.move_direction *= -1
      self.move_counter *= -1
    for tile in world.tile_list:
          #check for collision in x direction
        if tile[1].colliderect(self.rect.x + self.move_direction, self.rect.y, self.width, self.height):
          self.move_direction *= -1
          self.move_counter *= -1



class Spike(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load("spike1.png")
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

if game_over == 1:
  enemy1_group = pygame.sprite.Group.clear()
  spike_group = pygame.sprite.Group.clear()
  jumpring_group = pygame.sprite.Group.clear()
  topexit_group = pygame.sprite.Group.clear()

def getLevel(zonen,level_coords):
    if level_coords == [0,1]:
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
          ["0d",0,0,0,"0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"],
          ["0t","0a","0a","0a","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p","0p"]
          ]
    elif level_coords == [0,2]:
          world_data = [
          ["0s","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0c","0r"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j",0,0,0,0,0,0,0,0,0,0,0,0,0,"0b"],
          ["0d",0,0,0,0,0,0,0,0,"j","0a","0a","0a","0a",0,0,0,0,0,0,0,0,0,"0b"],
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
    return world_data


world_data = getLevel(zonen,level_coords)
player = Player(64, 704)

enemy1_group = pygame.sprite.Group()
spike_group = pygame.sprite.Group()
jumpring_group = pygame.sprite.Group()
topexit_group = pygame.sprite.Group()

def draw_grid():
  for line in range(0,25):
    pygame.draw.line(DISPLAYSURF,(255,255,255), (0, line * tile_size),(768, line * tile_size))
    pygame.draw.line(DISPLAYSURF,(255,255,255), (line * tile_size, 0),(line * tile_size, 768))








world = World(world_data)


while True:

  clock.tick(fps)

  DISPLAYSURF.blit(area0background,(0,0))
  draw_grid()

  if game_over == 0:
    enemy1_group.update()
  enemy1_group.draw(DISPLAYSURF)
  spike_group.draw(DISPLAYSURF)
  jumpring_group.draw(DISPLAYSURF)
  topexit_group.draw(DISPLAYSURF)

  player_data = player.update(game_over,xroom,yroom)
  game_over = player_data[0]
  xroom = player_data[1]
  yroom = player_data[2]
  level_coords = [xroom,yroom]
  if game_over == 1:
    game_over = 0
    enemy1_group = pygame.sprite.Group()
    spike_group = pygame.sprite.Group()
    jumpring_group = pygame.sprite.Group()
    topexit_group = pygame.sprite.Group()
    world_data = getLevel(zonen,level_coords)
    world = World(world_data)
  
  world.draw()

  
  
  for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
  pygame.display.update()
