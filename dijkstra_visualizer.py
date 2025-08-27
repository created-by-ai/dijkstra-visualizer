import pygame
import heapq
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
FONT = pygame.font.SysFont("Arial", 20)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dijkstra's Algorithm Visualization")
clock = pygame.time.Clock()

# Grid: 2D list to store nodes
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
# 0 = empty, 1 = wall, 2 = start, 3 = end
start_node = None
end_node = None

# Distance and previous tracking
distances = {}
previous = {}
visited = set()

# Create a graph from grid (for adjacency)
def get_neighbors(row, col):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE and grid[r][c] != 1:
            neighbors.append((r, c))
    return neighbors

# Dijkstra's Algorithm (step-by-step)
def dijkstra_step():
    global start_node, end_node, distances, previous, visited, grid

    if not start_node or not end_node:
        return False

    if not distances:
        # Initialize
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                distances[(i, j)] = float('inf')
        distances[start_node] = 0
        previous[start_node] = None

    # Priority queue: (distance, row, col)
    pq = [(0, start_node[0], start_node[1])]
    processed = set()

    while pq:
        d, row, col = heapq.heappop(pq)
        if (row, col) in processed:
            continue
        processed.add((row, col))

        # Mark as visited (blue)
        if (row, col) != start_node:
            grid[row][col] = 4  # Blue (processed)

        # Check if reached end
        if (row, col) == end_node:
            # Reconstruct path
            path = []
            current = (row, col)
            while current:
                path.append(current)
                current = previous[current]
            path.reverse()
            for r, c in path:
                if (r, c) != start_node and (r, c) != end_node:
                    grid[r][c] = 5  # Green (path)
            return True  # Done

        # Explore neighbors
        for nr, nc in get_neighbors(row, col):
            if (nr, nc) in processed:
                continue
            new_dist = d + 1  # Assuming unit weight (for simplicity)
            if new_dist < distances[(nr, nc)]:
                distances[(nr, nc)] = new_dist
                previous[(nr, nc)] = (row, col)
                heapq.heappush(pq, (new_dist, nr, nc))
                if (nr, nc) != end_node:
                    grid[nr][nc] = 4  # Blue (in queue)

        # Draw current state
        draw_grid()
        pygame.display.flip()
        pygame.time.delay(100)  # Delay for animation effect

    return False  # No path found

# Draw grid and nodes
def draw_grid():
    screen.fill(WHITE)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[i][j] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            elif grid[i][j] == 2:
                pygame.draw.rect(screen, RED, rect)
            elif grid[i][j] == 3:
                pygame.draw.rect(screen, ORANGE, rect)
            elif grid[i][j] == 4:
                pygame.draw.rect(screen, BLUE, rect)
            elif grid[i][j] == 5:
                pygame.draw.rect(screen, GREEN, rect)
            else:
                pygame.draw.rect(screen, GRAY, rect, 1)  # Empty

    # Add labels
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 2:
                text = FONT.render("S", True, WHITE)
                screen.blit(text, (j * CELL_SIZE + 5, i * CELL_SIZE + 5))
            elif grid[i][j] == 3:
                text = FONT.render("E", True, WHITE)
                screen.blit(text, (j * CELL_SIZE + 5, i * CELL_SIZE + 5))

    pygame.display.flip()

# Main loop
def main():
    global start_node, end_node
    running = True
    in_dijkstra = False

    while running:
        screen.fill(WHITE)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row, col = y // CELL_SIZE, x // CELL_SIZE

                if event.button == 1:  # Left click
                    if not start_node:
                        start_node = (row, col)
                        grid[row][col] = 2
                    elif not end_node and (row, col) != start_node:
                        end_node = (row, col)
                        grid[row][col] = 3
                    elif (row, col) != start_node and (row, col) != end_node:
                        grid[row][col] = 1  # Wall

                elif event.button == 3:  # Right click
                    if (row, col) == start_node:
                        start_node = None
                        grid[row][col] = 0
                    elif (row, col) == end_node:
                        end_node = None
                        grid[row][col] = 0
                    elif grid[row][col] == 1:
                        grid[row][col] = 0  # Remove wall

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start_node and end_node and not in_dijkstra:
                    in_dijkstra = True
                    # Run Dijkstra step-by-step
                    while not dijkstra_step():
                        pygame.time.delay(100)
                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                running = False
                                break
                        if not running:
                            break
                    in_dijkstra = False

        # Show instructions
        instruction = FONT.render("Left Click: Place Start (S), End (E), or Wall", True, BLACK)
        instruction2 = FONT.render("Right Click: Remove nodes or walls", True, BLACK)
        instruction3 = FONT.render("Press SPACE to start Dijkstra", True, BLACK)
        screen.blit(instruction, (10, HEIGHT - 100))
        screen.blit(instruction2, (10, HEIGHT - 70))
        screen.blit(instruction3, (10, HEIGHT - 40))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()