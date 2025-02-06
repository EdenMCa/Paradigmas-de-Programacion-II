import pygame
import random

class Cono:
    def __init__(self, screen, moto_config, score, enemies, mototaxi):
        self.screen = screen
        self.moto_config = moto_config
        self.score = score
        self.enemies = enemies
        self.mototaxi = mototaxi
        self.bandera = True  # Bandera para indicar el estado (True = juego en curso)
        self.spawn_delay = 60  # Número de frames entre cada aparición (aprox. 1 segundo a 60 FPS)
        self.spawn_timer = 0   # Contador de frames para el spawn

    def spawn_enemy(self):
        enemy_image = pygame.image.load("Media/cono.png")  # Asegúrate de que la ruta sea correcta
        enemy_image = pygame.transform.scale(
            enemy_image,
            (
                int(enemy_image.get_width() * self.moto_config.escalar_cono),
                int(enemy_image.get_height() * self.moto_config.escalar_cono)
            )
        )
        enemy_rect = enemy_image.get_rect()
        enemy_rect.x = self.moto_config.screen_width  # Aparece en el borde derecho
        enemy_rect.y = random.randint(
            self.moto_config.screen_height // 2,
            self.moto_config.screen_height - enemy_rect.height
        )
        self.enemies.append({"image": enemy_image, "rect": enemy_rect})

    def can_spawn_new_enemy(self):
        # Permitir hasta 3 enemigos simultáneos (ajusta este valor si lo consideras necesario)
        return len(self.enemies) < 3

    def update(self):
        # Actualizar posición de cada enemigo y comprobar colisiones
        for enemy in self.enemies[:]:
            # Mover enemigo de derecha a izquierda
            enemy["rect"].x -= self.moto_config.enemy_speed
            # Incrementa gradualmente la velocidad del enemigo
            self.moto_config.enemy_speed += 0.05

            # Ajustar el rectángulo de colisión (para mayor precisión)
            collision_rect = pygame.Rect(
                enemy["rect"].x + 10,
                enemy["rect"].y + 10,
                enemy["rect"].width - 20,
                enemy["rect"].height - 20
            )

            # Dibujar enemigo
            self.screen.blit(enemy["image"], enemy["rect"])

            # Verificar colisión con la mototaxi
            if self.mototaxi.collision_rect.colliderect(collision_rect):
                self.bandera = False
                print("¡Colisión! Fin del juego.")

            # Eliminar enemigos que salen de la pantalla y actualizar puntuación
            if enemy["rect"].right < 0:
                self.enemies.remove(enemy)
                self.score["points"] += 1

        # Controlar el tiempo entre apariciones de nuevos conos
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            if self.can_spawn_new_enemy():
                self.spawn_enemy()
            self.spawn_timer = 0
