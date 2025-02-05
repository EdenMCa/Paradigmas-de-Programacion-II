import pygame
import sys
import random

class Bocho:
    def __init__(self, screen, moto_config, score, enemies, mototaxi):
        self.screen = screen
        self.moto_config = moto_config
        self.score = score
        self.enemies = enemies
        self.mototaxi = mototaxi

    def update(self):
        for enemy in self.enemies[:]:
            enemy["rect"].x -= self.moto_config.enemy_speed  # Movimiento horizontal de derecha a izquierda

            # Ajustar el rectángulo de colisión
            collision_rect = pygame.Rect(
                enemy["rect"].x + 65,  # Reducir margen izquierdo
                enemy["rect"].y + 185,  # Reducir margen superior
                enemy["rect"].width - 160,  # Reducir ancho
                enemy["rect"].height - 250  # Reducir altura
            )

            # Dibujar enemigo
            self.screen.blit(enemy["image"], enemy["rect"])

            # Dibujar rectángulo de colisión para depuración
            pygame.draw.rect(self.screen, (255, 0, 0), collision_rect, 2)

            # Verificar colisión
            if self.mototaxi.collision_rect.colliderect(collision_rect):
                print("¡Colisión! Fin del juego. Eliminado por bocho.")
                pygame.quit()
                sys.exit()

            # Eliminar enemigos que salen de la pantalla
            if enemy["rect"].right < 0:  # Si el enemigo sale completamente por la izquierda
                self.enemies.remove(enemy)
                self.score["points"] += 1

        # Generar nuevos enemigos aleatoriamente si no hay conflictos
        if random.randint(1,
                          100) <= 1:  # Ajusta la probabilidad de aparición (se tiene que modificar conforme pase el juego)
            if self.can_spawn_new_enemy():
                self.spawn_enemy()

    def can_spawn_new_enemy(self):
        # Verifica si existe un enemigo en el área del nuevo obstáculo
        for enemy in self.enemies:
            # Si hay un enemigo en una posición vertical que se solape con el nuevo, no lo creamos
            if abs(enemy["rect"].y - self.moto_config.screen_height // 2) < enemy["rect"].height:
                return False  # Hay un enemigo en el mismo rango, no generamos uno nuevo
        return True

    def spawn_enemy(self):
        enemy_image = pygame.image.load("Media/carro1/frame0.png")  # Imagen de cono

        # Escala la imagen
        enemy_image = pygame.transform.scale(enemy_image, (
            enemy_image.get_width() * self.moto_config.escalar_bocho,
            enemy_image.get_height() * self.moto_config.escalar_bocho))

        enemy_rect = enemy_image.get_rect()
        enemy_rect.x = self.moto_config.screen_width  # Comienza desde el borde derecho
        enemy_rect.y = random.randint(self.moto_config.screen_height // 2,
                                      self.moto_config.screen_height - enemy_rect.height)
        self.enemies.append({"image": enemy_image, "rect": enemy_rect})