import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, exp_value):
        super().__init__()
        self.image = pygame.Surface((40, 40),5)  # Um pouco menor que o jogador
        self.image.fill((0, 255, 0))  # Preenche a imagem com cor verde
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 10  # Inimigos podem ter uma velocidade diferente
        self.last_update = pygame.time.get_ticks()  # Armazena a última vez que o inimigo foi atualizado
        self.update_interval = random.choice([1000, 500, 200, 100])  # Intervalo de atualização em milissegundos
        self.hp = 50  # Inicializa os pontos de vida do inimigo com um valor menor
        self.hp = 50  # Exemplo de pontos de vida totais
        self.max_hp = 50
        self.exp_value = exp_value  # Quantidade de experiência que o inimigo fornece


    def draw_health_bar(self, surface):
        health_ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, (255,0,0), (self.rect.x, self.rect.y - 10, self.rect.width, 5))
        pygame.draw.rect(surface, (0,255,0), (self.rect.x, self.rect.y - 10, self.rect.width * health_ratio, 5))


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

    def take_damage(self, amount):
        """Reduz os pontos de vida do inimigo."""
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        """Lida com a morte do inimigo."""
        print("Inimigo morreu!")
        self.kill()  # Remove o inimigo do grupo de sprites