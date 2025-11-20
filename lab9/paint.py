import pygame
import math

# Colors
white = (255, 255, 255)
eraser = (0, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))  
    pygame.display.set_caption("Drawing Shapes Lab 8 Extension")
    clock = pygame.time.Clock()
    
    radius = 15  #radius for freehand drawing
    mode = white  #Current color
    last_pos = None  #Last mouse position for drawing lines
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  
                    return
                
                #change color mode
                if event.key == pygame.K_r:
                    mode = red
                elif event.key == pygame.K_g:
                    mode = green
                elif event.key == pygame.K_b:
                    mode = blue
                elif event.key == pygame.K_y:
                    mode = yellow
                elif event.key == pygame.K_BACKSPACE:  # Eraser
                    mode = eraser
                
                #Draw shapes at mouse position
                elif event.key == pygame.K_w:  # Rectangle / square
                    drawSquare(screen, pygame.mouse.get_pos(), 100, mode)
                elif event.key == pygame.K_c:  # Circle
                    drawCircle(screen, pygame.mouse.get_pos(), 50, mode)
                elif event.key == pygame.K_t:  # Right triangle
                    drawRightTriangle(screen, pygame.mouse.get_pos(), 100, mode)
                elif event.key == pygame.K_e:  # Equilateral triangle
                    drawEquilateralTriangle(screen, pygame.mouse.get_pos(), 100, mode)
                elif event.key == pygame.K_h:  # Rhombus
                    drawRhombus(screen, pygame.mouse.get_pos(), 120, 60, mode)
            
            #drawing with mouse
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                last_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION and event.buttons[0]:
                if last_pos is not None:
                    start_pos = last_pos
                    end_pos = pygame.mouse.get_pos()
                    drawLineBetween(screen, start_pos, end_pos, radius, mode)
                    last_pos = end_pos
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, start, end, width, color_mode):
    color = color_mode
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = i / iterations
        x = int(start[0] + (end[0] - start[0]) * progress)
        y = int(start[1] + (end[1] - start[1]) * progress)
        pygame.draw.circle(screen, color, (x, y), width)

#Draw square
def drawSquare(screen, pos, size, color):
    x, y = pos
    pygame.draw.rect(screen, color, (x, y, size, size), 3)

#Draw circle
def drawCircle(screen, pos, radius, color):
    x, y = pos
    pygame.draw.circle(screen, color, (x, y), radius, 3)

#Draw right triangle (right angle at bottom-left)
def drawRightTriangle(screen, pos, size, color):
    x, y = pos
    points = [(x, y), (x, y + size), (x + size, y + size)]
    pygame.draw.polygon(screen, color, points, 3)

#Draw equilateral triangle
def drawEquilateralTriangle(screen, pos, size, color):
    x, y = pos
    height = math.sqrt(3)/2 * size
    points = [(x, y), (x - size/2, y + height), (x + size/2, y + height)]
    pygame.draw.polygon(screen, color, points, 3)

#Draw rhombus
def drawRhombus(screen, pos, width, height, color):
    x, y = pos
    points = [(x, y - height//2), (x + width//2, y), (x, y + height//2), (x - width//2, y)]
    pygame.draw.polygon(screen, color, points, 3)

main()