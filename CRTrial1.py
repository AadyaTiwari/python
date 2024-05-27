import math
import pygame
import sys

class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"3D({self.x:>2}, {self.y:>2}, {self.z:>2})"
    
    def scale(self, factor):
        return Point3D(self.x * factor, self.y * factor, self.z * factor)
    
    def translate(self, x, y, z):
        return Point3D(self.x + x, self.y + y, self.z + z)
    
    def rotateZ(self, angle):
        x1 = self.x * math.cos(angle) - self.y * math.sin(angle)
        y1 = self.y * math.cos(angle) + self.x * math.sin(angle)
        return Point3D(x1, y1, self.z)
    
    def rotateX(self, angle):
        y1 = self.y * math.cos(angle) - self.z * math.sin(angle)
        z1 = self.z * math.cos(angle) + self.y * math.sin(angle)
        return Point3D(self.x, y1, z1)
    
    def rotateY(self, angle):
        x1 = self.x * math.cos(angle) - self.z * math.sin(angle)
        z1 = self.z * math.cos(angle) + self.x * math.sin(angle)
        return Point3D(x1, self.y, z1)

angle = 0.01
factor = 100
min_angle = 0.001  # Minimum rotation speed to prevent stopping

# Rotation direction for each axis
rotate_x_direction = 1
rotate_y_direction = 1
rotate_z_direction = 1

# List to store multiple cubes, each represented by its own set of vertices
cubes = []

# Initial cube
initial_vertices = [Point3D(-1, 1, -1),
                    Point3D(1, 1, -1),
                    Point3D(1, 1, 1),
                    Point3D(-1, 1, 1),
                    Point3D(-1, -1, -1),
                    Point3D(1, -1, -1),
                    Point3D(1, -1, 1),
                    Point3D(-1, -1, 1)]
cubes.append(initial_vertices)

lines = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (3, 7), (1, 5), (2, 6)]

def draw_cube(vertices):
    for l in lines:
        p1 = vertices[l[0]].scale(factor).translate(400, 400, 400)
        p2 = vertices[l[1]].scale(factor).translate(400, 400, 400)
        pygame.draw.line(screen, white, (p1.x, p1.y), (p2.x, p2.y), 5)
    pygame.display.flip()

def rotate_cube(vertices):
    new_vertices = []
    for v in vertices:
        new_vertices.append(
            v.rotateX(rotate_x_direction * angle)
            .rotateY(rotate_y_direction * 2 * angle)
            .rotateZ(rotate_z_direction * angle / 2)
        )
    return new_vertices

def draw_button(text, x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.Font(None, 28)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

def check_button_click(x, y, width, height, mouse_pos):
    return x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('3D Rotating Cube with Speed and Direction Control')

# Define colors
white = (255, 255, 255)
button_color = (100, 100, 100)

# Button state
button_pressed = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            button_pressed = True
            if check_button_click(20, 20, 120, 40, mouse_pos):
                angle += 0.01
            elif check_button_click(150, 20, 120, 40, mouse_pos):
                angle = max(angle - 0.01, min_angle)  # Prevent angle from going below min_angle
            elif check_button_click(280, 20, 200, 40, mouse_pos):
                rotate_x_direction *= -1  # Toggle X rotation direction
            elif check_button_click(490, 20, 200, 40, mouse_pos):
                rotate_y_direction *= -1  # Toggle Y rotation direction
            elif check_button_click(700, 20, 200, 40, mouse_pos):
                rotate_z_direction *= -1  # Toggle Z rotation direction
            elif check_button_click(20, 80, 120, 40, mouse_pos):
                # Add a new cube at a different position
                translation_offset = len(cubes) * 200
                new_vertices = [v.translate(translation_offset, translation_offset, 0) for v in initial_vertices]
                cubes.append(new_vertices)
            elif check_button_click(150, 80, 120, 40, mouse_pos) and len(cubes) > 1:
                cubes.pop()  # Remove the last cube
        elif event.type == pygame.MOUSEBUTTONUP:
            button_pressed = False

    # Fill the screen with black
    screen.fill((0, 0, 0))
    
    # Draw buttons
    draw_button("Speed Up", 20, 20, 120, 40, button_color)
    draw_button("Slow Down", 150, 20, 120, 40, button_color)
    draw_button("Toggle X Direction", 280, 20, 200, 40, button_color)
    draw_button("Toggle Y Direction", 490, 20, 200, 40, button_color)
    draw_button("Toggle Z Direction", 700, 20, 200, 40, button_color)
    draw_button("Add Cube", 20, 80, 120, 40, button_color)
    draw_button("Remove Cube", 150, 80, 120, 40, button_color)
    
    # Rotate and draw each cube
    for i in range(len(cubes)):
        cubes[i] = rotate_cube(cubes[i])
        draw_cube(cubes[i])

# Quit Pygame
pygame.quit()
sys.exit()
