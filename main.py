import pygame
pygame.init()
black = (0, 0, 0)
X = 500
Y = 500
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Image')
c1R = int(input("Enter radius for circle 1:"))
c2R = int(input("Enter radius for circle 2:"))
dis = int(input("Enter distance between the two circles:"))
cocentric = False
tangent = False
two = False
zero = False
if dis == c1R + c2R:
    tangent = True
    image = pygame.image.load("tangent.jpg")
    print("The two circles are tangent.")
elif dis == 0:
    cocentric = True
    image = pygame.image.load('cocentric.png')
    print("The two circles are cocentric.")
elif dis < c1R+c2R:
    two = True
    image = pygame.image.load('two.jpg')
    print("The two circles have two points of intersection.")
elif dis > c1R + c2R:
    zero = True
    image = pygame.image.load('zero.jpg')
    print("The two circles have zero points of intersection.")

while True:

    display_surface.fill(black)

    display_surface.blit(image, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

        pygame.display.update()