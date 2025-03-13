import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)

# Tamaño de la pantalla
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20  # Tamaño de cada bloque

# Configuración de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Juego de la Viborita')

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Fuente para mostrar el puntaje
font_style = pygame.font.SysFont("bahnschrift", 25)

# Puntaje
score = 0

# Función para mostrar el puntaje
def mostrar_puntaje(puntaje):
    value = font_style.render("Puntaje: " + str(puntaje), True, BLACK)
    screen.blit(value, [0, 0])

# Función para dibujar la serpiente
def nuestra_serpiente(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])

# Función principal del juego
def juego():
    global score
    game_over = False
    game_close = False

    # Posición inicial de la serpiente
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
    x1_change = 0
    y1_change = 0

    # Lista de bloques de la serpiente
    snake_List = []
    Length_of_snake = 1

    # Posición de la comida
    foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            mostrar_puntaje(Length_of_snake - 1)
            mensaje = font_style.render("¡Perdiste! Presiona Q para salir o C para jugar de nuevo.", True, RED)
            screen.blit(mensaje, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)
        pygame.draw.rect(screen, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        nuestra_serpiente(BLOCK_SIZE, snake_List)
        mostrar_puntaje(Length_of_snake - 1)

        pygame.display.update()

        # Comprobar si la serpiente ha comido la comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            Length_of_snake += 1

        clock.tick(15)  # Velocidad de la serpiente

    pygame.quit()
    quit()

# Llamar a la función principal
juego()
