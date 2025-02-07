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
    La música de inicio se reproduce hasta que el jugador inicia el juego.
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
            # Se elimina la detención de la música aquí para que siga sonando
            elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                running = False

        pygame.display.flip()
        clock.tick(moto_config.FPS)

def get_player_name(screen, moto_config):
    """
    Pantalla para que el jugador ingrese su nombre.
    """
    font = pygame.font.Font("Media/Games-Italic.ttf", 30)  # Fuente retro más adecuada
    nametext = pygame.font.Font("Media/Name Smile.otf", 20)
    button_font = pygame.font.Font("Media/Games-Italic.ttf", 25)  # Fuente más retro para el botón "Aceptar"
    name = ""
    active = True
    clock = pygame.time.Clock()

    # Colores adecuados para un tema retro
    text_color = (0, 0, 0)
    name_color = (0, 0, 0)
    input_box_color = (255, 255, 255)
    input_box_active_color = (105, 105, 105)  # Amarillo brillante al estar activo, para un efecto retro
    button_color = (0, 0, 0)  # Verde para el botón
    button_hover_color = (0, 255, 0)  # Verde brillante cuando el ratón pasa sobre el botón
    button_text_color = (255, 255, 255)  # Color del texto del botón

    background_image = pygame.image.load("Media/base.png")
    background_image = pygame.transform.scale(background_image, (moto_config.screen_width, moto_config.screen_height))

    # Crear rectángulo para el campo de texto
    input_box = pygame.Rect(moto_config.screen_width // 2 - 110, 310, 220, 35)

    while active:
        screen.blit(background_image, (0, 0))  # Fondo de pantalla
        pygame.draw.rect(screen, input_box_active_color if len(name) > 0 else input_box_color, input_box)

        prompt = font.render("Ingresa tu nombre:", True, text_color)
        name_text = nametext.render(name, True, name_color)

        text_width = name_text.get_width()
        text_x = input_box.x + (input_box.width - text_width) // 2  # Centra el texto dentro del cuadro
        screen.blit(prompt, (moto_config.screen_width // 2 - prompt.get_width() // 2, 270))
        screen.blit(name_text, (text_x, input_box.y + 10))  # El texto ahora se centra dinámicamente

        # Dibujar botón "Aceptar"
        button_rect = pygame.Rect(moto_config.screen_width // 2 - 50, 375, 100, 40)  # Tamaño más equilibrado
        mouse_pos = pygame.mouse.get_pos()

        # Cambiar color del botón y texto cuando el ratón pasa sobre el botón
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, button_hover_color, button_rect)
            button_text_color = (0, 0, 0)  # Cambiar el color del texto a negro cuando el ratón pasa sobre el botón
        else:
            pygame.draw.rect(screen, button_color, button_rect)
            button_text_color = (255, 255, 255)  # Color original del texto

        button_text = button_font.render("Jugar", True, button_text_color)
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
                    if len(name) < 8:
                        name += event.unicode

            # Verificar si el botón "Aceptar" fue presionado
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    active = False

        clock.tick(moto_config.FPS)

    pygame.mixer.music.stop()  # Detener la música de inicio cuando se ingresa el nombre
    return name


def show_gameOver_screen(screen, moto_config):
    """
    Muestra la pantalla de Game Over con opciones para volver a jugar o salir.
    Se reproduce una música exclusiva para esta pantalla.
    """
    # Cargar y reproducir la música de Game Over
    pygame.mixer.music.load("Media/RIP-15.wav")
    pygame.mixer.music.set_volume(1.5)
    pygame.mixer.music.play(0)

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

    play_again_text = play_again_font.render("Play Again?", True, (255, 255, 255))
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

    pygame.mixer.music.stop()  # Detener la música de Game Over al salir de la pantalla

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
