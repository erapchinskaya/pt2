import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы (размеры окна, цвета)
WIDTH, HEIGHT = 800, 600
FPS = 60

# Цвета (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ловец шариков")
clock = pygame.time.Clock()


class Platform:
    def __init__(self):
        self.width = 150
        self.height = 20
        # Размещаем платформу по центру внизу экрана
        self.rect = pygame.Rect(WIDTH // 2 - self.width // 2,
                                HEIGHT - 40,
                                self.width,
                                self.height)
        self.speed = 10
        self.color = GREEN

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self, keys):
        # Обработка управления
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed


class Ball:
    def __init__(self):
        self.radius = random.randint(10, 25)
        # Появляется в случайном месте вверху за экраном
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(-100, -self.radius)
        self.speed_y = random.randint(3, 7)
        self.color = (random.randint(50, 255),
                      random.randint(50, 255),
                      random.randint(50, 255))

    def draw(self, surface):
        pygame.draw.circle(surface, self.color,
                           (self.x, self.y), self.radius)

    def check_collision(self, platform_rect):
        # Находим ближайшую к шарику точку на прямоугольнике платформы
        closest_x = max(platform_rect.left, min(self.x, platform_rect.right))
        closest_y = max(platform_rect.top, min(self.y, platform_rect.bottom))

        # Вычисляем расстояние от центра шарика до этой точки
        distance = ((self.x - closest_x) ** 2 + (self.y - closest_y) ** 2) ** 0.5
        return distance < self.radius

    def update(self):
        # Двигаем шарик вниз
        self.y += self.speed_y
        # Если шарик улетел за низ экрана, возвращаем True
        return self.y > HEIGHT + self.radius


player = Platform()
balls = []
ball_spawn_timer = 0
score = 0
font = pygame.font.Font(None, 36)
game_over = False

# Главный игровой цикл
running = True
while running:
    # Контроль FPS
    clock.tick(FPS)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                player = Platform()
                balls = []
                ball_spawn_timer = 0
                score = 0
                game_over = False

    keys = pygame.key.get_pressed()
    if not game_over:
        player.update(keys)

        ball_spawn_timer += 1
        if ball_spawn_timer >= 30:
            balls.append(Ball())
            ball_spawn_timer = 0

        for ball in balls[:]:
            # Если шарик упал за экран - игра окончена
            if ball.update():
                game_over = True

            # Проверка столкновения с платформой
            if ball.check_collision(player.rect):
                score += 1
                balls.remove(ball)


    # Отрисовка
    # 1. Сначала очищаем экран
    screen.fill(BLACK)
    # 2. Рисуем игровые объекты
    if not game_over:
        player.draw(screen)
        for ball in balls:
            ball.draw(screen)

    # 3. Рисуем UI (счет и сообщение о Game Over)
    score_text = font.render(f"Очки: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    if game_over:
        game_over_text = font.render("GAME OVER! Нажмите R для рестарта",
                                     True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 180, HEIGHT // 2))
    # 4. Обновляем экран
    pygame.display.flip()

# Выход из игры
pygame.quit()
sys.exit()
