import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
FPS = 5

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 150, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

# Классы
class Segment:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE,
                          GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, WHITE, rect)


class Apple:
    def __init__(self):
        self.radius = GRID_SIZE // 2
        self.randomize_position()

    def draw(self, surface):
        pygame.draw.circle(surface, RED,
                           (self.x, self.y), self.radius)

    def randomize_position(self):
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        # Выравнивание по сетке
        self.x = (self.x // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2
        self.y = (self.y // GRID_SIZE) * GRID_SIZE + GRID_SIZE // 2

class Snake:
    def __init__(self):
        self.segments = [Segment(5, 5)]  # Начинаем с одного сегмента
        self.dx = 1  # Направление движения по X
        self.dy = 0  # Направление движения по Y
        self.grow_to = 0  # Счетчик сегментов, на которые нужно вырасти

    def draw(self, surface):
        for segment in self.segments:
            segment.draw(surface)

    def grow(self):
        self.grow_to += 1

    def move(self):
        # Получаем текущую позицию головы
        head = self.segments[0]
        new_x = head.x + self.dx
        new_y = head.y + self.dy

        # Создаем новую голову
        new_head = Segment(new_x, new_y)

        # Вставляем новую голову в начало списка
        self.segments.insert(0, new_head)

        # Если не нужно расти, удаляем последний сегмент
        if self.grow_to > 0:
            self.grow_to -= 1
        else:
            self.segments.pop()

    def check_collision(self):
        head = self.segments[0]

        # Проверка столкновения с границами экрана
        if head.x < 0 or head.x >= WIDTH // GRID_SIZE or \
                head.y < 0 or head.y >= HEIGHT // GRID_SIZE:
            return True

        # Проверка столкновения с самой собой
        for segment in self.segments[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True

        return False

    def check_apple_collision(self, apple):
        head = self.segments[0]
        # Проверка расстояния от головы до центра яблока
        distance = ((head.x * GRID_SIZE + GRID_SIZE // 2 - apple.x) ** 2 +
                    (head.y * GRID_SIZE + GRID_SIZE // 2 - apple.y) ** 2) ** 0.5
        return distance < (GRID_SIZE // 2 + apple.radius)


def reset_game():
    """Сброс игры к начальному состоянию"""
    global snake, apple, score, ingame
    snake = Snake()
    apple = Apple()
    score = 0
    ingame = True


# Спрайты
seg = Segment(10,10)
apple = Apple()
snake = Snake()
font = pygame.font.SysFont('Arial', 25)
score = 0

# Игровой цикл
ingame = True
while True:
    clock.tick(FPS)
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Выход из игры
            pygame.time.delay(500)
            pygame.quit()
            sys.exit()

        # Управление змейкой
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Рестарт по клавише R
                reset_game()
            if ingame:
                if event.key == pygame.K_UP and snake.dy != 1:
                    snake.dx, snake.dy = 0, -1
                elif event.key == pygame.K_DOWN and snake.dy != -1:
                    snake.dx, snake.dy = 0, 1
                elif event.key == pygame.K_LEFT and snake.dx != 1:
                    snake.dx, snake.dy = -1, 0
                elif event.key == pygame.K_RIGHT and snake.dx != -1:
                    snake.dx, snake.dy = 1, 0

    if ingame:
        snake.move()
        # Проверка коллизий
        if snake.check_collision():
            ingame = False

        # Проверка, съела ли змея яблоко
        if snake.check_apple_collision(apple):
            snake.grow()
            apple.randomize_position()
            score += 1

        # Рендеринг
        screen.fill(GREEN)
        snake.draw(screen)
        apple.draw(screen)
        # Отрисовка счета
        score_text = font.render(f'Счет: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))
    else:
        # Экран окончания игры
        screen.fill(GREEN)
        game_over_text = font.render('Игра окончена! Нажми R для рестарта',
                                     True, WHITE)
        screen.blit(game_over_text, (WIDTH//2-180, HEIGHT//2))

    # Обновление экрана
    pygame.display.update()

pygame.quit()
sys.exit()
