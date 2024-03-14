import pygame
from .base_state import State

class GameOverState(State):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font(None, 74)
        self.text = self.font.render('Game Over', True, (255, 0, 0))
        self.text_rect = self.text.get_rect(center=(400, 200))  # Centraliza o texto

        self.menu_btn_color = (0, 255, 0)
        self.menu_btn_rect = pygame.Rect(300, 300, 200, 50)
        self.btn_font = pygame.font.Font(None, 36)
        self.btn_text = self.btn_font.render('Menu', True, (0, 0, 0))
        self.btn_text_rect = self.btn_text.get_rect(center=self.menu_btn_rect.center)

    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()
        if self.menu_btn_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.game.change_state('menu', reset=True)

    def draw(self, surface):
        surface.fill((0, 0, 0))
        surface.blit(self.text, self.text_rect)
        pygame.draw.rect(surface, self.menu_btn_color, self.menu_btn_rect)
        surface.blit(self.btn_text, self.btn_text_rect)
