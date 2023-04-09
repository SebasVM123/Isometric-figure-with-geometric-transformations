import pygame
from MODEL import isometric_figure


if __name__ == '__main__':
    background = [255, 252, 199]
    width = height = 600

    pygame.init()
    screen = pygame.display.set_mode([width, height])
    screen.fill(background)
    pygame.display.set_caption('Figura Isométrica')

    figure = isometric_figure.IsometricFigure(screen)
    figure.draw()

    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    if figure.scale < 2:
                        figure.scaling(0.1)
                if event.key == pygame.K_x:
                    if figure.scale > 0.3:
                        figure.scaling(-0.1)
                if event.key == pygame.K_q:
                    figure.rotate(5)
                if event.key == pygame.K_e:
                    figure.rotate(-5)
                if event.key == pygame.K_w:
                    figure.move([0, 5])
                if event.key == pygame.K_s:
                    figure.move([0, -5])
                if event.key == pygame.K_a:
                    figure.move([-5, 0])
                if event.key == pygame.K_d:
                    figure.move([5, 0])

        screen.fill(background)
        figure.draw()
        pygame.display.flip()
