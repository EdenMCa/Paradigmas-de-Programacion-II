import pygame

class Config:
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 500
        self.game_title = "MTX Racing"
        self.background_image = pygame.image.load("Media/fondo_bucle.png")
        self.mototaxi_speed = 17.0  # Velocidad de la moto
        self.scroll = 0
        self.background_speed = 1.0  # Velocidad actual del fondo
        self.initial_background_speed = 1.0  # Valor inicial del fondo para reinicios
        self.escalar_cono = 0.3  # Factor para escalar el cono
        self.FPS = 60  # Fotogramas por segundo
        self.RELOJ = pygame.time.Clock()
        self.enemy_speed = 10.0  # Velocidad actual del enemigo (cono)
        self.initial_enemy_speed = 10.0  # Valor inicial de la velocidad del enemigo
