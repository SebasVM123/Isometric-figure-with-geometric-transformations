from MODEL import functions
import pygame

class IsometricFigure:
    def __init__(self, surface):
        self.surface = surface
        self.points = [[0,0], [0,-40], [52,-70], [140, -20], [140, 20], [104,40], [104,0], [52,70], [34,60], [86,30],
                       [86,-10], [52,-30], [34,20]]
        self.transPoints = self.points
        self.scale = 1
        self.rotation = 0
        self.color = [191, 182, 214]

    def draw(self):
        surface = self.surface
        center = [250, 300]
        points = self.transPoints

        cPoints = []
        for p in points:
            cPoints.append(functions.cartesianTranslation(center, p))

        pygame.draw.line(surface, self.color, cPoints[0], cPoints[1], width=2)
        pygame.draw.line(surface, self.color, cPoints[0], cPoints[11], width=2)
        pygame.draw.line(surface, self.color, cPoints[0], cPoints[12], width=2)
        pygame.draw.line(surface, self.color, cPoints[1], cPoints[2], width=2)
        pygame.draw.line(surface, self.color, cPoints[2], cPoints[3], width=2)
        pygame.draw.line(surface, self.color, cPoints[2], cPoints[11], width=2)
        pygame.draw.line(surface, self.color, cPoints[3], cPoints[4], width=2)
        pygame.draw.line(surface, self.color, cPoints[4], cPoints[5], width=2)
        pygame.draw.line(surface, self.color, cPoints[4], cPoints[6], width=2)
        pygame.draw.line(surface, self.color, cPoints[5], cPoints[6], width=2)
        pygame.draw.line(surface, self.color, cPoints[5], cPoints[7], width=2)
        pygame.draw.line(surface, self.color, cPoints[5], cPoints[9], width=2)
        pygame.draw.line(surface, self.color, cPoints[7], cPoints[8], width=2)
        pygame.draw.line(surface, self.color, cPoints[8], cPoints[9], width=2)
        pygame.draw.line(surface, self.color, cPoints[8], cPoints[12], width=2)
        pygame.draw.line(surface, self.color, cPoints[9], cPoints[10], width=2)
        pygame.draw.line(surface, self.color, cPoints[10], cPoints[11], width=2)
        pygame.draw.line(surface, self.color, cPoints[10], cPoints[12], width=2)

    def scaling(self, n):
        sPoints = []
        for p in self.points:
            sPoints.append(functions.scaling(p, self.scale + n))

        self.scale = round(self.scale + n, 1)
        self.transPoints = sPoints

    def rotate(self, t):
        rPoints = []
        for p in self.transPoints:
            rPoints.append(functions.rotate(p, t))

        self.rotation += t
        self.transPoints = rPoints
        self.points = self.transPoints

    def move(self, d):
        dPoints = []
        for p in self.transPoints:
            dPoints.append(functions.translation(d, p))

        self.transPoints = dPoints
        self.points = self.transPoints