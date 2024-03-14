import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40),5)  # Um pouco menor que o jogador
        self.image.fill((0, 255, 0))  # Preenche a imagem com cor verde
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 10  # Inimigos podem ter uma velocidade diferente
        self.last_update = pygame.time.get_ticks()  # Armazena a última vez que o inimigo foi atualizado
        self.update_interval = random.choice([1000, 500, 200, 100])  # Intervalo de atualização em milissegundos

    def update(self):
        if pygame.time.get_ticks() - self.last_update > self.update_interval:
            self.last_update = pygame.time.get_ticks()
            self.rect.x += random.choice([-1, 1]) * self.speed  # Movimento horizontal aleatório
            self.rect.y += random.choice([-1, 1]) * self.speed  # Movimento vertical aleatório


        # Garante que o inimigo não saia da tela
        #TODO: Criar feat que altera as dimensões dinamicamente 
        screen_width, screen_height = 800, 600  # Substitua por suas dimensões de tela reais
        self.rect.x = max(0, min(screen_width - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(screen_height - self.rect.height, self.rect.y))