import pygame
#import time

def draw_block():
    surface.fill((36,36,36))
    grid_size = 25  
    grid_color = (60, 60, 60) 
    draw_grid(surface, grid_size, grid_color)
    surface.blit(block, (block_x,block_y))
    pygame.display.flip()

def draw_grid(surface, grid_size, color):
    """Draws a grid on the given surface."""
    width, height = surface.get_size()
    for x in range(0, width, grid_size):  # Vertical lines
        pygame.draw.line(surface, color, (x, 0), (x, height))
    for y in range(0, height, grid_size):  # Horizontal lines
        pygame.draw.line(surface, color, (0, y), (width, y))

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((500,500))
    pygame.display.set_caption("SNAKE GAME")
    surface.fill((36,36,36))
    grid_size = 25  
    grid_color = (60, 60, 60) 
    draw_grid(surface, grid_size, grid_color)


    block = pygame.image.load("photo.jpg").convert()
    block = pygame.transform.scale(block, (25, 25))
    block_x = 100
    block_y = 100

    surface.blit(block,(block_x,block_y))

    pygame.display.flip()

    running =  True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_UP:
                    block_y = block_y - 25
                    draw_block()
                if event.key == pygame.K_DOWN:
                    block_y = block_y + 25
                    draw_block()
                if event.key == pygame.K_RIGHT:
                    block_x = block_x + 25
                    draw_block()
                if event.key == pygame.K_LEFT:
                    block_x = block_x - 25
                    draw_block()
            elif event.type == pygame.QUIT:
                running = False
