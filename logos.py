
import pygame
class Question():
    def __init__(self,question:str,correct_answer:str,other_answers:list[str]):
        self.question = question
        self.correct_answer = correct_answer
        self.other_answers = other_answers
        pass

class Star_1_logo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/star_1_logo.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Star_2_logo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/star_2_logo.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Star_3_logo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/star_3_logo.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Star_4_logo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/star_4_logo.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Star_5_logo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/star_5_logo.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Star_6_logo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/star_6_logo.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))        

class Quiz_logo(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/quiz_star_2.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class About_us_logo(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/about_us_logo_7.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Video_logo(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/video_logo_3.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class About_us_info(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/about_us.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Video_info(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/video_info.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Presentation_1(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/presentation_1.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Presentation_2(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/presentation_2.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Presentation_3(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/presentation_3.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Presentation_4(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/presentation_4.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Presentation_5(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/presentation_5.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))

class Presentation_6(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/presentation_6.png").convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(0)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect(center = (x,y))


