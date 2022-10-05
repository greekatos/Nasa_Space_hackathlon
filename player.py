import math
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load("images/player_1.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(600, 360))
        
        self.move_speed = 5 # Up, down, right, left speed (controlled by arrow keys) 1
        self.forward_speed = 2 # Forward speed (controlled by awsd keys) 3
        self.rotation_speed = 45 #rotation speed
        self.rotation = 0

    def move_Up(self):
        self.rect.y -= self.move_speed    # go to y
        
    def move_Down(self):
        self.rect.y += self.move_speed
        
    def move_Right(self):
        self.rect.x += self.move_speed
        
    def move_Left(self):
        self.rect.x -= self.move_speed 

    def move_forward(self):
        self.rect.x += self.move_speed * math.sin(self.rotation)
        self.rect.y += self.move_speed * math.cos(self.rotation)
    
    def rotate_right(self):
        self.rotation += self.rotation_speed 
        #player_img = pygame.transform.rotate(player_img,-1)
        self.image = pygame.transform.rotate(self.image, self.rotation_speed)
    def rotate_left(self):
        self.rotation -= self.rotation_speed
        self.image = pygame.transform.rotate(self.image, -self.rotation_speed)
