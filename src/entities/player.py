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
        self.hp = 100  # Inicializa os pontos de vida do jogador
        self.max_hp = 100

    # Outros métodos...

    def draw_health_bar(self, surface):
        # Proporção da vida atual em relação à vida total
        health_ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, (255,0,0), (self.rect.x, self.rect.y - 10, self.rect.width, 5))  # Barra de fundo (vermelha)
        pygame.draw.rect(surface, (0,255,0), (self.rect.x, self.rect.y - 10, self.rect.width * health_ratio, 5))  # Barra de vida atual (verde)

        
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

    def take_damage(self, amount):
        """Reduz os pontos de vida do jogador."""
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        """Lida com a morte do jogador."""
        print("Jogador morreu!")
        # Aqui você pode adicionar lógica para fim de jogo, reiniciar, etc.