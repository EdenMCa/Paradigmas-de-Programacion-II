import sys
import pygame
from Config import Config
from mototaxi import Mototaxi
from cono import Cono
import game_functionalities
from database import guardar_puntuacion  # Función para guardar en la base de datos

def show_start_screen(screen, moto_config):
    """
    Pantalla de inicio con música y botón 'Start'.
    Al hacer clic en el botón, se detiene la música y se sale de esta pantalla.
    """
    pygame.mixer.init()
    # Cargar y reproducir música de inicio
    pygame.mixer.music.load("Media/musica_inicio.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    # Cargar y escalar la imagen de fondo
    background_image = pygame.image.load("Media/base.png")
    background_image = pygame.transform.scale(background_image, (moto_config.screen_width, moto_config.screen_height))

    # Fuente y configuración del botón
    font_path = "Media/LetraRetro.ttf"
    button_font = pygame.font.Font(font_path, 25)
    text_color = (255, 255, 255)
    button_color = (0, 128, 0)
    button_hover_color = (0, 200, 0)

    # Definir el rectángulo del botón "Start"
    button_rect = pygame.Rect(0, 0, 200, 80)
    button_rect.center = (moto_config.screen_width // 2, moto_config.screen_height // 2)

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.blit(background_image, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, button_hover_color, button_rect)
        else:
            pygame.draw.rect(screen, button_color, button_rect)

        button_text = button_font.render("Start", True, text_color)
        screen.blit(button_text, (button_rect.centerx - button_text.get_width() // 2,
                                  button_rect.centery - button_text.get_height() // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                pygame.mixer.music.stop()  # Detener la música de inicio
                running = False

        pygame.display.flip()
        clock.tick(moto_config.FPS)

def get_player_name(screen, moto_config):
    """
    Pantalla para que el jugador ingrese su nombre.
    Devuelve el nombre ingresado.
    """
    font = pygame.font.Font("Media/LetraRetro.ttf", 20)  # Fuente más pequeña para el nombre
    button_font = pygame.font.Font("Media/LetraRetro.ttf", 15)  # Fuente más pequeña para el botón "Aceptar"
    name = ""
    active = True
    clock = pygame.time.Clock()

    # Colores
    text_color = (0, 0, 0)  # Color negro para el texto
    input_box_color = (50, 50, 50)
    input_box_active_color = (50, 50, 50)
    button_color = (0, 128, 0)  # Botón verde
    button_hover_color = (0, 200, 0)  # Verde más brillante al pasar el ratón

    # Cargar imagen de fondo (opcional)
    background_image = pygame.image.load("Media/base.png")
    background_image = pygame.transform.scale(background_image, (moto_config.screen_width, moto_config.screen_height))

    # Crear rectángulo para el campo de texto
    input_box = pygame.Rect(moto_config.screen_width // 2 - 150, 300, 300, 35)

    while active:
        screen.blit(background_image, (0, 0))  # Fondo de pantalla
        pygame.draw.rect(screen, input_box_active_color if len(name) > 0 else input_box_color, input_box)

        prompt = font.render("Ingresa tu nombre:", True, text_color)
        name_text = font.render(name, True, text_color)

        # Posicionar el texto
        screen.blit(prompt, (moto_config.screen_width // 2 - prompt.get_width() // 2, 270))
        screen.blit(name_text, (input_box.x + 10, input_box.y + 10))

        # Dibujar botón "Aceptar"
        button_rect = pygame.Rect(moto_config.screen_width // 2 - 120, 400, 240, 35)  # Tamaño más equilibrado
        mouse_pos = pygame.mouse.get_pos()

        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, button_hover_color, button_rect)
        else:
            pygame.draw.rect(screen, button_color, button_rect)

        button_text = button_font.render("Aceptar", True, text_color)
        screen.blit(button_text, (button_rect.centerx - button_text.get_width() // 2, button_rect.centery - button_text.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 14:
                        name += event.unicode

            # Verificar si el botón "Aceptar" fue presionado
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    active = False

        clock.tick(moto_config.FPS)

    return name



def show_gameOver_screen(screen, moto_config):
    """
    Muestra la pantalla de Game Over con opciones para volver a jugar o salir.
    """
    pygame.mouse.set_visible(False)
    screen.fill((0, 0, 0))
    font_path = "Media/LetraRetro.ttf"

    game_over_image = pygame.image.load("Media/game_over.png")
    game_over_image = pygame.transform.scale(game_over_image, (600, 400))

    title_font = pygame.font.Font(font_path, 60)
    option_font = pygame.font.Font(font_path, 25)
    play_again_font = pygame.font.Font(font_path, 30)

    game_over_pos = (moto_config.screen_width // 2 - game_over_image.get_width() // 2, -150)
    title_pos = (moto_config.screen_width // 2, 200)

    play_again_text = play_again_font.render("Play Again", True, (255, 255, 255))
    play_again_pos = (moto_config.screen_width // 2 - play_again_text.get_width() // 2, 300)

    option_spacing = 100
    yes_pos = (moto_config.screen_width // 2 - option_spacing, 380)
    no_pos = (moto_config.screen_width // 2 + option_spacing, 380)

    clock = pygame.time.Clock()
    selected_option = "Yes"

    waiting = True
    while waiting:
        screen.fill((0, 0, 0))
        screen.blit(game_over_image, game_over_pos)
        game_over_text = title_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over_text, (title_pos[0] - game_over_text.get_width() // 2, title_pos[1]))
        screen.blit(play_again_text, play_again_pos)

        arrow_offset = -40
        yes_text = option_font.render("Yes", True, (0, 255, 0))
        no_text = option_font.render("No", True, (255, 0, 0))
        yes_arrow = option_font.render(">", True, (0, 255, 0)) if selected_option == "Yes" else None
        no_arrow = option_font.render(">", True, (255, 0, 0)) if selected_option == "No" else None

        if yes_arrow:
            screen.blit(yes_arrow, (yes_pos[0] + arrow_offset, yes_pos[1]))
        screen.blit(yes_text, yes_pos)
        if no_arrow:
            screen.blit(no_arrow, (no_pos[0] + arrow_offset, no_pos[1]))
        screen.blit(no_text, no_pos)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    selected_option = "No" if selected_option == "Yes" else "Yes"
                elif event.key == pygame.K_RETURN:
                    if selected_option == "Yes":
                        print("Opción 'Yes' seleccionada. Reiniciando juego...")
                        waiting = False
                    elif selected_option == "No":
                        print("Opción 'No' seleccionada. Cerrando juego...")
                        pygame.quit()
                        sys.exit()
        clock.tick(moto_config.FPS)

def run_game():
    pygame.init()
    moto_config = Config()
    screen = pygame.display.set_mode((moto_config.screen_width, moto_config.screen_height))
    pygame.display.set_caption(moto_config.game_title)

    show_start_screen(screen, moto_config)
    pygame.mouse.set_visible(True)
    jugador_nombre = get_player_name(screen, moto_config)
    pygame.mouse.set_visible(False)

    while True:
        pygame.mixer.music.load("Media/musica_fondo.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        moto_config.background_speed = moto_config.initial_background_speed
        moto_config.scroll = 0
        moto_config.enemy_speed = moto_config.initial_enemy_speed

        mototaxi = Mototaxi(screen, moto_config)
        enemies = []  # Lista de enemigos (conos)
        score = {"points": 0}
        cono = Cono(screen, moto_config, score, enemies, mototaxi)

        clock = pygame.time.Clock()
        running = True
        while running:
            game_functionalities.game_events(moto_config, screen, mototaxi)
            game_functionalities.screen_refresh(moto_config, screen, mototaxi, score, cono)

            # Se llama a check_game_over con todos los argumentos necesarios
            if game_functionalities.check_game_over(moto_config, screen, mototaxi, enemies, cono):
                pygame.mixer.music.stop()
                # Imprimir datos de depuración
                print(f"Guardando puntuación: {jugador_nombre} - {score['points']}")
                guardar_puntuacion(jugador_nombre, score["points"])
                show_gameOver_screen(screen, moto_config)
                running = False

            clock.tick(moto_config.FPS)

        pygame.mouse.set_visible(False)

if __name__ == "__main__":
    run_game()
