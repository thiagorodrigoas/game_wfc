import pygame
from .base_state import State
from entities.player import Player
from entities.enemy import Enemy
from entities.projectile import Projectile
import random

ENEMY_SPAWN_EVENT = pygame.USEREVENT + 5

class GameState(State):
    def __init__(self, game):
        super().__init__(game)
        self.bg_color = (200, 200, 200)  # Cor cinza para o fundo
        self.player = Player(100, 100)  # Inicializa o personagem
        self.enemies = pygame.sprite.Group()  # Grupo de inimigos
        self.projectiles = pygame.sprite.Group()  # Grupo de projeteis
        self.add_enemies()
        self.enter()



    def enter(self):
        # Definir evento personalizado para a aparição de inimigos
        pygame.time.set_timer(ENEMY_SPAWN_EVENT, 2000)  # Timer para criar inimigos a cada 2000 milissegundos (2 segundos)

    
    def add_enemies(self):
        # Inicialize os inimigos aqui
        for _ in range(5):  # Cria 5 inimigos
            x = random.randint(0, 760)
            y = random.randint(0, 560)
            self.enemies.add(Enemy(x, y))  # Adiciona os inimigos ao grupo

    def update(self, dt):
        keys = pygame.key.get_pressed()  # Captura as teclas pressionadas
        self.player.update(keys)  # Atualiza a posição do jogador
        

        for event in pygame.event.get():
            if event.type == ENEMY_SPAWN_EVENT:
                self.add_enemies()

        self.enemies.update()  # Atualiza o inimigo
        
        # Verifica se há colisão entre o jogador e qualquer inimigo
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.exit()
            self.game.change_state('game_over')  # Altera para o estado de Game Over


        # Captura o evento de clique do mouse para disparar
        if pygame.mouse.get_pressed()[0]:  # Se o botão esquerdo do mouse foi pressionado
            mouse_pos = pygame.mouse.get_pos()
            new_projectile = Projectile(self.player.rect.center, mouse_pos, damage=2)
            self.projectiles.add(new_projectile)

        # Atualiza os projéteis
        self.projectiles.update()

        # Detecção de colisão entre projéteis e inimigos
        #pygame.sprite.groupcollide(self.projectiles, self.enemies, True, True)

        # Verificação de colisão entre projéteis e inimigos
        collisions = pygame.sprite.groupcollide(self.projectiles, self.enemies, True, False)
        for projectile, enemies_hit in collisions.items():
            for enemy in enemies_hit:
                enemy.take_damage(projectile.damage)  # Aplica o dano do projétil ao inimigo
                # Verifique se o inimigo morreu como resultado do dano dentro do método take_damage

        

    def draw(self, surface):
        surface.fill(self.bg_color)  # Preenche o fundo com a cor cinza
        self.player.draw(surface)# Desenha o personagem 
        self.player.draw_health_bar(surface)  # Desenha a barra de vida do jogador
        
        self.enemies.draw(surface)  # Desenha todos os inimigos
        self.projectiles.draw(surface)  # Desenha os projéteis na tela

        for enemy in self.enemies:
            enemy.draw_health_bar(surface)  # Desenha a barra de vida de cada inimigo

    def exit(self):
        # Desativa o timer ao sair do GameState
        pygame.time.set_timer(ENEMY_SPAWN_EVENT, 0)