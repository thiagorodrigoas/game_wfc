import pygame
from .base_state import State

class MenuState(State):
    def __init__(self, game):
        super().__init__(game)
        self.start_btn_color = (0, 255, 0)  # Cor verde para o botão
        self.start_btn_rect = pygame.Rect(300, 250, 200, 50)  # Define a posição e o tamanho do botão
        self.font = pygame.font.Font(None, 36)  # Define a fonte do texto do botão
        self.text = self.font.render('Iniciar Jogo', True, (0, 0, 0))  # Cria o texto do botão
        self.text_rect = self.text.get_rect(center=self.start_btn_rect.center)  # Centraliza o texto no botão

    def update(self, dt):
        # Verifica se o mouse foi clicado e se está sobre o botão
        mouse_pos = pygame.mouse.get_pos()
        if self.start_btn_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.game.change_state('game')  # Muda para o estado do jogo

    def draw(self, surface):
        # Desenha o botão
        pygame.draw.rect(surface, self.start_btn_color, self.start_btn_rect)
        surface.blit(self.text, self.text_rect)
