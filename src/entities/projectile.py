import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((0, 0, 255))  # Cor azul
        self.rect = self.image.get_rect(center=start_pos)

        # Calculando a direção do movimento
        x_diff = target_pos[0] - start_pos[0]
        y_diff = target_pos[1] - start_pos[1]
        self.direction = pygame.math.Vector2(x_diff, y_diff).normalize()

        self.speed = 5

    def update(self):
        # Move o projétil na direção calculada
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
