import math

def rotate(point, degrees):
    x = point[0]
    y = point[1]
    xR = x * math.cos(math.radians(degrees)) - y * math.sin(math.radians(degrees))
    yR = x * math.sin(math.radians(degrees)) + y * math.cos(math.radians(degrees))
    return [xR, yR]

def scaling(point, s):
    return [point[0] * s, point[1] * s]

def cartesianTranslation(center, point):
    return [center[0] + point[0], center[1] - point[1]]

def translation(pos, point):
    return [pos[0] + point[0], pos[1] + point[1]]