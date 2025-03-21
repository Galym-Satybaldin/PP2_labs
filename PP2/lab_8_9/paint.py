import pygame

# Initialize Pygame
pygame.init()

# Set up display
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint Program")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Drawing settings
drawing = False
start_pos = None
brush_size = 5
current_color = BLACK
mode = 'free'  # Drawing modes: free, square, rtriangle, etriangle, rhombus

# Fill screen with white background
screen.fill(WHITE)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Change drawing modes
            if event.key == pygame.K_1:
                mode = 'free'
            elif event.key == pygame.K_2:
                mode = 'square'
            elif event.key == pygame.K_3:
                mode = 'rtriangle'
            elif event.key == pygame.K_4:
                mode = 'etriangle'
            elif event.key == pygame.K_5:
                mode = 'rhombus'
            elif event.key == pygame.K_c:  # Clear screen
                screen.fill(WHITE)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()
            
        elif event.type == pygame.MOUSEBUTTONUP:
            if start_pos:
                drawing = False
                end_pos = pygame.mouse.get_pos()
                
                # Draw shapes based on mode
                if mode == 'square':
                    rect_width = end_pos[0] - start_pos[0]
                    rect_height = end_pos[1] - start_pos[1]
                    pygame.draw.rect(screen, current_color, 
                                   (start_pos[0], start_pos[1], 
                                    rect_width, rect_height), 2)
                
                elif mode == 'rtriangle':  # Right triangle
                    points = [start_pos, 
                             (end_pos[0], start_pos[1]), 
                             end_pos]
                    pygame.draw.polygon(screen, current_color, points, 2)
                
                elif mode == 'etriangle':  # Equilateral triangle
                    base = end_pos[0] - start_pos[0]
                    height = int(base * (3 ** 0.5) / 2)  # Height of equilateral triangle
                    points = [start_pos,
                             (end_pos[0], start_pos[1]),
                             (start_pos[0] + base//2, start_pos[1] - height)]
                    pygame.draw.polygon(screen, current_color, points, 2)
                
                elif mode == 'rhombus':
                    mid_x = (start_pos[0] + end_pos[0]) // 2
                    mid_y = (start_pos[1] + end_pos[1]) // 2
                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    points = [(mid_x, start_pos[1]),          # Top
                             (end_pos[0], mid_y),            # Right
                             (mid_x, end_pos[1]),           # Bottom
                             (start_pos[0], mid_y)]         # Left
                    pygame.draw.polygon(screen, current_color, points, 2)

        elif event.type == pygame.MOUSEMOTION and drawing and mode == 'free':
            current_pos = pygame.mouse.get_pos()
            if start_pos:
                pygame.draw.line(screen, current_color, start_pos, current_pos, brush_size)
                start_pos = current_pos

    # Display instructions
    font = pygame.font.Font(None, 24)
    instructions = "1:Free 2:Square 3:R.Triangle 4:E.Triangle 5:Rhombus C:Clear"
    text = font.render(instructions, True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()