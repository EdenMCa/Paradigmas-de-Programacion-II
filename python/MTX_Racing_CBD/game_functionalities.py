import sys
import pygame
import math

def game_events(moto_config, screen, mototaxi):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Verificar si el evento (presionar tecla) se ha ejecutado
        elif event.type == pygame.KEYDOWN:
            game_events_keydown(event, moto_config, screen, mototaxi)

        # Verificar si el evento (soltar tecla) se ha ejecutado
        elif event.type == pygame.KEYUP:
            game_events_keyup(event, mototaxi)

def game_events_keydown(event, moto_config, screen, mototaxi):
    if event.key == pygame.K_UP:
        mototaxi.is_moving_up = True
    elif event.key == pygame.K_DOWN:
        mototaxi.is_moving_down = True

def game_events_keyup(event, mototaxi):
    if event.key == pygame.K_UP:
        mototaxi.is_moving_up = False
    elif event.key == pygame.K_DOWN:
        mototaxi.is_moving_down = False

def screen_refresh(moto_config, screen, mototaxi, score, cono):
    # Lógica del scroll infinito del fondo
    bg_width = moto_config.background_image.get_width()
    tiles = math.ceil(moto_config.screen_width / bg_width) + 1

    # Dibujar el fondo desplazándose
    for i in range(0, tiles):
        screen.blit(moto_config.background_image, (i * bg_width + moto_config.scroll, 0))

    # Actualizar el scroll
    moto_config.scroll -= moto_config.background_speed  # Velocidad ajustada para el fondo

    # Reiniciar el scroll cuando se completa un ciclo
    if abs(moto_config.scroll) > bg_width:
        moto_config.scroll = 0

    # Incrementar la velocidad del fondo progresivamente hasta un tope
    if moto_config.background_speed < 25.0:
        moto_config.background_speed += 0.03  # Ajusta este valor para cambiar la progresión

    # Actualizar la posición de la moto
    mototaxi.update()

    # Mostrar la mototaxi en pantalla
    mototaxi.dibujar()

    # Actualizar cono
    cono.update()
    # Mostrar la puntuación
    draw_score(screen, score)

    # Actualizar la pantalla
    pygame.display.update()

def draw_score(screen, score):
    font_path = "Media/LetraRetro.ttf"  # Ruta al archivo de la fuente
    font = pygame.font.Font(font_path, 15)  # Fuente por defecto
    score_text = font.render(f"Puntuación: {score['points']}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

def check_game_over(moto_config, screen, mototaxi, enemies, cono):
    # También puedes añadir otras condiciones aquí, por ejemplo, si la moto choca con un enemigo
    if cono.bandera is False:
        return True  # El juego ha terminado debido a una colisión
    else:
        # Si llegamos aquí, el juego continúa
        return False