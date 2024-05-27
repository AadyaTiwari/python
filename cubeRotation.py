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
    
    def scale(self,factor):
        return Point3D(self.x * factor,self.y * factor,self.z * factor)
    
    def translate(self,x,y,z):
        return Point3D(self.x+x,self.y+y,self.z+z)
    
    def rotateZ(self,angle):
        x1 = self.x*math.cos(angle) - self.y*math.sin(angle)
        y1 = self.y*math.cos(angle) + self.x*math.sin(angle)
        return Point3D(x1,y1,self.z)
    
    def rotateX(self,angle):
        y1 = self.y*math.cos(angle) - self.z*math.sin(angle)
        z1 = self.z*math.cos(angle) + self.y*math.sin(angle)
        return Point3D(self.x,y1,z1)
    
    def rotateY(self,angle):
        x1 = self.x*math.cos(angle) - self.z*math.sin(angle)
        z1 = self.z*math.cos(angle) + self.x*math.sin(angle)
        return Point3D(x1,self.y,z1)
    
    
    # def rotate(ax1,ax2,angle):
        
        
angle = 0.01

factor = 100

vertices = [Point3D(-1,1,-1),
            Point3D(1,1,-1),
            Point3D(1,1,1),
            Point3D(-1,1,1),
            Point3D(-1,-1,-1),
            Point3D(1,-1,-1),
            Point3D(1,-1,1),
            Point3D(-1,-1,1)
           ]

print(vertices)

lines = [(0,1),
         (1,2),
         (2,3),
         (3,0),
         (4,5),
         (5,6),
         (6,7),
         (7,4),
         (0,4),
         (3,7),
         (1,5),
         (2,6)
         ]

def draw_cube():
    for l in lines:
        p1 = vertices[l[0]].scale(factor).translate(300,300,300)
        p2 = vertices[l[1]].scale(factor).translate(300,300,300)
        
        # Draw a white line from the top-left to the bottom-right of the window
        pygame.draw.line(screen, white, (p1.x, p1.y), (p2.x, p2.y), 5)  # 5 is the thickness of the line
    
    # Update the display
    pygame.display.flip()

def rotate():
    global vertices
    new_vertices = []
    for v in vertices:
        new_vertices.append(v.rotateX(angle).rotateY(2*angle).rotateZ(angle/2))
    vertices = new_vertices
        
    

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))  # Window size: 800x600
pygame.display.set_caption('Draw a Line with Pygame')  # Window title

# Define colors
white = (255, 255, 255)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))
    rotate()
    draw_cube()

# Quit Pygame
pygame.quit()
sys.exit()