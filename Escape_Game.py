import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell(x, y) for y in range(height)] for x in range(width)]
        self.start = self.cells[0][0]
        self.exit = self.cells[-1][-1]
        self.generate()

    def generate(self):
        stack = [self.start]
        while stack:
            current = stack.pop()
            current.visited = True
            neighbors = [self.get_cell(current.x+1, current.y), self.get_cell(current.x-1, current.y),
                         self.get_cell(current.x, current.y+1), self.get_cell(current.x, current.y-1)]
            neighbors = [n for n in neighbors if n and not n.visited]
            if neighbors:
                stack.append(current)
                neighbor = random.choice(neighbors)
                self.remove_walls(current, neighbor)
                stack.append(neighbor)

    def get_cell(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        return self.cells[x][y]

    def remove_walls(self, a, b):
        if a.x < b.x:
            a.walls[1] = False
            b.walls[3] = False
        elif a.x > b.x:
            a.walls[3] = False
            b.walls[1] = False
        elif a.y < b.y:
            a.walls[2] = False
            b.walls[0] = False
        elif a.y > b.y:
            a.walls[0] = False
            b.walls[2] = False

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = [True, True, True, True]

    def draw(self, surface, cell_size):
        x = self.x * cell_size
        y = self.y * cell_size
        if self.walls[0]:
            pygame.draw.line(surface, (255, 255, 255), (x, y), (x+cell_size, y), 1)
        if self.walls[1]:
            pygame.draw.line(surface, (255, 255, 255), (x+cell_size, y), (x+cell_size, y+cell_size), 1)
        if self.walls[2]:
            pygame.draw.line(surface, (255, 255, 255), (x, y+cell_size), (x+cell_size, y+cell_size), 1)
        if self.walls[3]:
            pygame.draw.line(surface, (255, 255, 255), (x, y), (x, y+cell_size), 1)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction, maze):
        new_x = self.x + direction[0]
        new_y = self.y + direction[1]
        if not maze.get_cell(new_x, new_y).walls[direction[2]]:
            self.x = new_x
            self.y = new_y

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

    def move(self, maze):
        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]
        if maze.get_cell(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

class MazeEscape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = Maze(width, height)
        self.player = Player(0, 0)
        self.enemies = [Enemy(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(5)]
        self.clock = pygame.time.Clock()

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width*20, self.height*20))
        pygame.display.set_caption("Maze Escape")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.move((0, -1, 2), self.maze)
                    elif event.key == pygame.K_DOWN:
                        self.player.move((0, 1, 0), self.maze)
                    elif event.key == pygame.K_LEFT:
                        self.player.move((-1, 0, 1), self.maze)
                    elif event.key == pygame.K_RIGHT:
                        self.player.move((1, 0, 3), self.maze)
            screen.fill((0, 0, 0))
            for row in self.maze.cells:
                for cell in row:
                    cell.draw(screen, 20)
            pygame.draw.rect(screen, (0, 255, 0), (self.player.x*20, self.player.y*20, 20, 20))
            for enemy in self.enemies:
                enemy.move(self.maze)
                pygame.draw.rect(screen, (255, 0, 0), (enemy.x*20, enemy.y*20, 20, 20))
                if enemy.x == self.player.x and enemy.y == self.player.y:
                    print("Game Over")
                    pygame.quit()
                    return
            if self.player.x == self.maze.exit.x and self.player.y == self.maze.exit.y:
                print("You Win!")
                pygame.quit()
                return
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    maze_escape = MazeEscape(25, 25)
    maze_escape.run()
