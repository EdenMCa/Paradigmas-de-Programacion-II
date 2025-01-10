import sys
import pygame
import math
import random
from carros import EnemyCar


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


def screen_refresh(moto_config, screen, mototaxi, screen_size, enemies, score, occupied_lanes):
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
    if moto_config.background_speed < 30.0:
        moto_config.background_speed += 0.03  # Ajusta este valor para cambiar la progresión

    # Actualizar la posición de la moto
    mototaxi.update()

    # Mostrar la mototaxi en pantalla
    mototaxi.dibujar()

    # Dibujar y actualizar enemigos
    update_enemies(screen, moto_config, enemies, mototaxi, score, occupied_lanes)

    # Mostrar la puntuación
    draw_score(screen, score)

    # Actualizar la pantalla
    pygame.display.update()


def update_enemies(screen, moto_config, enemies, mototaxi, score, occupied_lanes):
    for enemy in enemies[:]:
        # Actualizar posición y animación del enemigo
        enemy.update()

        # Dibujar el enemigo
        enemy.draw()

        # Verificar colisión
        if mototaxi.collision_rect.colliderect(enemy.collision_rect):
            print("¡Colisión! Fin del juego.")
            return True  # Devolver True al detectar colisión

        # Eliminar enemigos que salen de la pantalla
        if enemy.rect.right < 0:
            enemies.remove(enemy)
            score["points"] += 1

            # Liberar el carril del enemigo
            for lane, y_position in {
                "left": moto_config.screen_height // 2 - 120,
                "right": moto_config.screen_height // 2 + 20
            }.items():
                if enemy.rect.y == y_position:
                    occupied_lanes[lane] = False

    # Generar nuevos enemigos aleatoriamente
    if random.randint(1, 100) <= moto_config.enemy_spawn_chance:
        spawn_enemy(moto_config, screen, enemies, occupied_lanes)

    return False  # Si no hay colisión, el juego continúa


def spawn_enemy(moto_config, screen, enemies, occupied_lanes):
    designs = ["carro1", "carro2"]  # Nombres de las carpetas de diseños
    design = random.choice(designs)  # Elegir un diseño aleatorio

    # Definir las posiciones de los carriles (eje y)
    lanes = {
        "left": moto_config.screen_height // 2 - 120,  # Carril izquierdo
        "right": moto_config.screen_height // 2 + 20  # Carril derecho
    }

    # Elegir un carril no ocupado
    available_lanes = [lane for lane in lanes if not occupied_lanes[lane]]

    # Si no hay carriles disponibles, no generar enemigo
    if not available_lanes:
        return

    chosen_lane = random.choice(available_lanes)
    scale = (300, 300)  # Valores para el tamaño
    enemy = EnemyCar(screen, moto_config, design, scale)  # Crear un carro enemigo
    enemy.rect.y = lanes[chosen_lane]  # Asignar la posición en el carril elegido

    # Marcar el carril como ocupado
    occupied_lanes[chosen_lane] = True

    enemies.append(enemy)


def draw_score(screen, score):
    font_path = "Media/LetraRetro.ttf"  # Ruta al archivo de la fuente
    font = pygame.font.Font(font_path, 15)  # Fuente por defecto
    score_text = font.render(f"Puntuación: {score['points']}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))


def check_game_over(moto_config, screen, mototaxi, enemies):
    # Lógica para verificar si el juego ha terminado
    if mototaxi.image_rect.top <= 0:  # Si la moto llega a la parte superior
        return True  # El juego ha terminado

    # También puedes añadir otras condiciones aquí, por ejemplo, si la moto choca con un enemigo
    for enemy in enemies:
        if mototaxi.collision_rect.colliderect(enemy.collision_rect):
            return True  # El juego ha terminado debido a una colisión

    # Si llegamos aquí, el juego continúa
    return False


def show_game_over_screen(screen, moto_config):
    font_path = "Media/LetraRetro.ttf"  # Ruta al archivo de la fuente
    font = pygame.font.Font(font_path, 40)
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(game_over_text,
                (moto_config.screen_width // 2 - game_over_text.get_width() // 2, moto_config.screen_height // 4))

    # Opción para continuar o salir
    button_font = pygame.font.Font(font_path, 25)
    button_color = (0, 128, 0)
    button_hover_color = (0, 200, 0)
    button_rect = pygame.Rect(0, 0, 200, 80)
    button_rect.center = (moto_config.screen_width // 2, moto_config.screen_height // 2 + 100)

    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, button_hover_color, button_rect)
    else:
        pygame.draw.rect(screen, button_color, button_rect)

    button_text = button_font.render("Play Again", True, (255, 255, 255))
    screen.blit(button_text, (
    button_rect.centerx - button_text.get_width() // 2, button_rect.centery - button_text.get_height() // 2))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                print("Botón Play Again presionado. Reiniciando juego...")
                waiting = False  # Reiniciar el juego

