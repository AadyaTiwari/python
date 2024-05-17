import pygame 

#initializing pygame 
pygame.init()

#creating screen
screen = pygame.display.set_mode((800,600))

#Adding Title and Icon to the game
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

#Player 
playerImg = pygame.image.load('alien.png')
playerX= 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX,playerY))

#game loop
run = True

while run:
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255,0,0), (200,100,150,150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player()
    pygame.display.update()
