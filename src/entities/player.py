import pygame
from utils.sprites import map_sprites

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        sprites = map_sprites(sprite_sheet_path='assets/images/sprites/player/TX Player.png', 
                                   sprite_size=(32, 64),
                                   columns=4,
                                   rows=2)  # Lista para armazenar cada quadro da animação
        
        self.dict_sprites = {'left':sprites[2],
                             'right':pygame.transform.flip(sprites[2], True, False),
                             'up': sprites[1],
                             'down':sprites[0],
                             'shadow':sprites[3]}
        
        self.current_sprite = self.dict_sprites['down']
        self.image = self.current_sprite  # Imagem atual do sprite
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5


    def update(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.image = self.dict_sprites['left']
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.image = self.dict_sprites['right']
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.image = self.dict_sprites['up']
        if keys[pygame.K_s]:
            self.rect.y += self.speed
            self.image = self.dict_sprites['down']
    
    
    def draw(self, surface):
        # Desenha a sombra primeiro
        #surface.blit(self.dict_sprites['shadow'], self.rect)
        # Depois desenha o sprite do jogador
        surface.blit(self.image, self.rect)