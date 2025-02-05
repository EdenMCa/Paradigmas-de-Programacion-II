import pygame

# Clase para manipular al personaje moto.
class Mototaxi:
    def __init__(self, screen, moto_config):
        self.screen = screen
        self.images = [pygame.image.load(f"Media//mototaxi/moto{i}.png") for i in range (6)]

        self.current_image = 0  # Índice de la imagen actual
        self.animation_speed = 0.3  # Velocidad de la animación (ajustable)
        self.animation_timer = 0

        # Obtener el rectángulo de la primera imagen
        self.image = self.images[self.current_image]
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicializar la posición
        self.image_rect.centerx = self.screen_rect.left + 150 # Eje x
        self.image_rect.bottom = self.screen_rect.bottom + 20 # Eje y

        # Bandera
        self.is_moving_up = False
        self.is_moving_down = False

        # Velocidad
        self.moto_config = moto_config # Se crea el objeto
        self.mototaxi_speed = self.moto_config.mototaxi_speed # Se crea la variable para la velocidad.
        self.image_rect_centerx = float(self.image_rect.centerx) # Hacemos un cast a flotante.
        self.image_rect_centery = float(self.image_rect.centery) # Cast a flotante

    # Mét0do que dibuja la moto en su ubicación y su rectángulo de colisión
    def dibujar(self):
        self.screen.blit(self.image, self.image_rect)
        #pygame.draw.rect(self.screen, (0, 255, 0), self.collision_rect, 2)  # Verde con borde de 2 píxeles

    # Métod0 que actualiza la posición del personaje.
    def update(self):
        if self.is_moving_up and (self.image_rect.top > self.screen_rect.top + 70):
            self.image_rect_centery -= self.mototaxi_speed # Velocidad hacia arriba.
        elif self.is_moving_down and (self.image_rect.bottom < self.screen_rect.bottom + 30):
            self.image_rect_centery += self.mototaxi_speed # Velocidad hacia abajo.

        self.image_rect.centerx = self.image_rect_centerx # Asignamos el flotante al entero.
        self.image_rect.centery = self.image_rect_centery # Asignamos el flotante al entero.

        self.collision_rect = pygame.Rect(
            self.image_rect.x + 65,  # Reducir margen izquierdo
            self.image_rect.y + 185,  # Reducir margen superior
            self.image_rect.width - 160,  # Reducir ancho
            self.image_rect.height - 250  # Reducir altura
        )

        # Actualizar animación
        self.animate()

    def animate(self):
        # Incrementar el temporizador de animación
        self.animation_timer += self.animation_speed
        if self.animation_timer >= 1:  # Cambiar de imagen cada 1 unidad de tiempo
            self.animation_timer = 0
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]  # Cambiar a la siguiente imagen
