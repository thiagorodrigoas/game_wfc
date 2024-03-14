import pygame

def map_sprites(sprite_sheet_path, sprite_size, columns, rows):
    
    sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
    # Inicializa uma lista para manter os sprites mapeados
    
    sprites = []
    for row in range(rows):
        for col in range(columns):
            # Calcula a posição x, y do sprite na folha
            x = col * sprite_size[0]
            y = row * sprite_size[1]
            # Cria um novo Surface para cada sprite
            sprite = pygame.Surface(sprite_size, pygame.SRCALPHA)
            # Desenha a área de interesse do sprite sheet no novo Surface
            sprite.blit(sprite_sheet, (0, 0), (x, y, sprite_size[0], sprite_size[1]))
            sprites.append(sprite)
    
    return sprites


# def generate_list_sprites(sprite_sheet_path, ):
#     ...

#     # Caminho para o sprite sheet carregado
#     sprite_sheet_path = '/mnt/data/TX Player.png'  # Atualize para o caminho correto do sprite sheet

#     # Carrega a imagem do sprite sheet
#     sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()

#     # Definir o tamanho dos sprites e a quantidade de colunas e linhas
#     sprite_size = (32, 32)
#     columns, rows = 5, 2  # Número de colunas e linhas no sprite sheet

#     # Mapear os sprites usando a função
#     return map_sprites(sprite_sheet, sprite_size, columns, rows)
