import pygame
from math import sin, cos
WINDOW_SIZE = 800
pygame.init()

window = pygame.display.set_mode((WINDOW_SIZE,WINDOW_SIZE))
clock = pygame.time.Clock()

pygame.display.set_caption("Cube Rotation")

projection_matrix = [[1,0,0],
                     [0,1,0],
                     [0,0,0]]

cube_points = [n for n in range(8)]
cube_points[0] = [[-1],[-1],[1]] 
cube_points[1] = [[1],[-1],[1]] 
cube_points[2] = [[1],[1],[1]] 
cube_points[3] = [[-1],[1],[1]] 
cube_points[4] = [[-1],[-1],[-1]] 
cube_points[5] = [[1],[-1],[-1]] 
cube_points[6] = [[1],[1],[-1]] 
cube_points[7] = [[-1],[1],[-1]] 

def multiply_m(a,b):
    arows, acols = len(a), len(a[0])
    brows, bcols = len(b), len(b[0])

    result = [[j for j in range(bcols)]for i in range(arows)]

    if acols == brows:
        for i in range(arows):
            for j in range(bcols):
                for k in range(brows):
                    result[i][j] += a[i][k] * b[k][j]

    else:
        return "error"

    return result

run = True

def connect_points(i,j, points):
    pygame.draw.line(window, (255, 255, 255), (points[i][0], points[i][1]), (points[j][0], points[j][1]))

scale = 100
anglex = angley = anglez = 0
while run:
    clock.tick(60)
    window.fill((0,0,0))
    rotationx = [[1,0,0],
                 [0, cos(anglex), -sin(anglex)],
                 [0, -sin(anglex), cos(anglex)]]
    
    rotationy = [[cos(angley), 0, sin(angley)],
                 [0,1,0],
                 [-sin(angley), 0, cos(angley)]]
    
    rotationz = [[cos(anglez), -sin(anglez), 0],
                  [sin(anglez), cos(anglez), 0],
                  [0,0,1]]

    anglex += 0.1
    angley += 0.1
    anglez += 0.1

    points = [_ for _ in range(len(cube_points))]
    i = 0

    for point in cube_points:
        rotate_x = multiply_m(rotationx, point)
        rotate_y = multiply_m(rotationy, rotate_x)
        rotate_z = multiply_m(rotationz, rotate_y)

        point_2d = multiply_m(projection_matrix, rotate_z)

        x = point_2d[0][0] * scale + WINDOW_SIZE//2
        y = point_2d[1][0] * scale + WINDOW_SIZE//2

        points[i] = (x,y)
        i += 1

        pygame.draw.circle(window, (255,0,0), (x,y), 5)
    '''  
    connect_points(0,1,points)
    connect_points(0,2,points)
    connect_points(0,3,points)
    connect_points(0,4,points)
    connect_points(0,5,points)
    connect_points(0,6,points)
    connect_points(0,7,points)
    connect_points(1,2,points)
    connect_points(2,3,points)
    connect_points(3,4,points)
    connect_points(4,5,points)
    connect_points(5,6,points)
    connect_points(6,7,points)
    '''
    for i in range(8):
        for j in range(i,8):
            connect_points(i,j,points)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

