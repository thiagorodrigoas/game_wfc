import pygame
import sys
from game.state_manager import StateManager
from game.states.menu_state import MenuState
from game.states.game_state import GameState
from game.states.game_over_state import GameOverState
# Inicialização do Pygame
pygame.init()

# Configurações da janela do jogo
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Roguelike de Fantasia Medieval')


# Inicialização do gerenciador de estados
state_manager = StateManager()
state_manager.add_state('menu', MenuState)
state_manager.add_state('game', GameState)
state_manager.add_state('game_over', GameOverState)

state_manager.change_state('menu')

# Relógio do jogo para controle de FPS
clock = pygame.time.Clock()

# Loop principal do jogo
running = True
while running:
    dt = clock.tick(60) / 1000.0  # Delta time em segundos
    
    # Atualizações
    state_manager.update(dt)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Renderização
    screen.fill((0, 0, 0))  # Limpa a tela com cor preta
    state_manager.draw(screen)
    pygame.display.flip()

# Finalização do Pygame antes de sair
pygame.quit()
sys.exit()
