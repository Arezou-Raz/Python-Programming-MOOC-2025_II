import pygame
from random import randint

# Game constants
WIDTH, HEIGHT = 640, 480
ROBOT_SPEED = 4
MONSTER_SPEED = 2
WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

class RobotCollector:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Robot Collector - Avoid the Monsters!")
        self.font = pygame.font.SysFont("Arial", 24)
        self.clock = pygame.time.Clock()

        self.load_assets()
        self.reset_game()
        self.main_loop()

    def load_assets(self):
        """Load sprites provided by the course template."""
        self.robot = pygame.image.load("robot.png")
        self.coin = pygame.image.load("coin.png")
        self.monster = pygame.image.load("monster.png")

    def reset_game(self):
        """Set or reset the game state."""
        # Player starting position
        self.robot_x = WIDTH // 2
        self.robot_y = HEIGHT // 2

        # Coin starting position
        self.new_coin_pos()

        # List of monsters: each is [x, y, dx, dy]
        # Starting with 3 monsters for a good challenge
        self.monsters = []
        for i in range(3):
            self.monsters.append([
                randint(0, WIDTH - self.monster.get_width()),
                randint(0, HEIGHT - self.monster.get_height()),
                MONSTER_SPEED if randint(0,1) == 0 else -MONSTER_SPEED,
                MONSTER_SPEED if randint(0,1) == 0 else -MONSTER_SPEED
            ])

        self.score = 0
        self.game_over = False

        # Dictionary to track which keys are held down
        self.keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False,
                     pygame.K_UP: False, pygame.K_DOWN: False}

    def new_coin_pos(self):
        """Move the coin to a random location."""
        self.coin_x = randint(0, WIDTH - self.coin.get_width())
        self.coin_y = randint(0, HEIGHT - self.coin.get_height())

    def handle_logic(self):
        """Update positions and check for collisions."""
        if self.game_over:
            return

        # 1. Move Robot
        if self.keys[pygame.K_LEFT] and self.robot_x > 0:
            self.robot_x -= ROBOT_SPEED
        if self.keys[pygame.K_RIGHT] and self.robot_x < WIDTH - self.robot.get_width():
            self.robot_x += ROBOT_SPEED
        if self.keys[pygame.K_UP] and self.robot_y > 0:
            self.robot_y -= ROBOT_SPEED
        if self.keys[pygame.K_DOWN] and self.robot_y < HEIGHT - self.robot.get_height():
            self.robot_y += ROBOT_SPEED

        # 2. Move Monsters (Bouncing logic)
        for m in self.monsters:
            m[0] += m[2] # x + dx
            m[1] += m[3] # y + dy

            # Bounce off walls
            if m[0] <= 0 or m[0] >= WIDTH - self.monster.get_width():
                m[2] *= -1
            if m[1] <= 0 or m[1] >= HEIGHT - self.monster.get_height():
                m[3] *= -1

        # 3. Check Collisions
        robot_rect = pygame.Rect(self.robot_x, self.robot_y, self.robot.get_width(), self.robot.get_height())
        coin_rect = pygame.Rect(self.coin_x, self.coin_y, self.coin.get_width(), self.coin.get_height())
