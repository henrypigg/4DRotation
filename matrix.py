import pygame
import math

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.values = [[0 for i in range(n)] for j in range(m)]

    def __repr__(self):
        returnString = ""
        for row in self.values:
            for value in row:
                returnString += str(value) + " "
            returnString += "\n"

        return returnString    

def matMult(m, v):
    if m.n != v.size:
        print("ERROR: Matrix columns do not equal vector size.")
        return
    elif m.m == 2:
        newVector = R2Vector(0, 0)
    elif m.m == 3:
        newVector = R3Vector(0, 0, 0)
    elif m.m == 4:
        newVector = R4Vector(0, 0, 0, 0)

    for i in range(m.m):
        for j in range(m.n):
            newVector.vector[i] += (v.vector[j] * m.values[i][j])

    return newVector


class R2Vector:
    def __init__(self, x, y):
        self.size = 2
        self.vector = [x, y]

    def __repr__(self):
        return str(self.vector)


class R3Vector:
    def __init__(self, x, y, z):
        self.size = 3
        self.vector = [x, y, z]
    
    def __repr__(self):
        return str(self.vector)

    def projection(self):
        projectionMatrix = Matrix(3, 2)
        projectionMatrix.values = [[1, 0, 0],[0, 1, 0]]

        return matMult(projectionMatrix, self)

class R4Vector:
    def __init__(self, x, y, z, w):
        self.size = 4
        self.vector = [x, y, z, w]

    def __repr__(self):
        return str(self.vector)

    def projection(self):
        distance = 150

        if self.vector[3] != distance:
            v = 1 / (distance - self.vector[3])
        else:
            v = 1

        projectionMatrix = Matrix(4, 3)
        projectionMatrix.values = [[v, 0, 0, 0],
                                   [0, v, 0, 0],
                                   [0, 0, v, 0]]
        newVector = matMult(projectionMatrix, self)

        return newVector.projection()

class HyperCube:
    def __init__(self, size):
        self.vertices = []
        self.vertices.append(R4Vector((0.5) * size,  (0.5) * size,  (0.5) * size,  (0.5) * size))
        self.vertices.append(R4Vector((-0.5) * size, (0.5) * size,  (0.5) * size,  (0.5) * size))
        self.vertices.append(R4Vector((-0.5) * size, (-0.5) * size, (0.5) * size,  (0.5) * size))
        self.vertices.append(R4Vector((0.5) * size,  (-0.5) * size, (0.5) * size,  (0.5) * size))
        self.vertices.append(R4Vector((0.5) * size,  (0.5) * size,  (-0.5) * size, (0.5) * size))
        self.vertices.append(R4Vector((-0.5) * size, (0.5) * size,  (-0.5) * size, (0.5) * size))
        self.vertices.append(R4Vector((-0.5) * size, (-0.5) * size, (-0.5) * size, (0.5) * size))
        self.vertices.append(R4Vector((0.5) * size,  (-0.5) * size, (-0.5) * size, (0.5) * size))
        self.vertices.append(R4Vector((0.5) * size,  (0.5) * size,  (0.5) * size,  (-0.5) * size))
        self.vertices.append(R4Vector((-0.5) * size, (0.5) * size,  (0.5) * size,  (-0.5) * size))
        self.vertices.append(R4Vector((-0.5) * size, (-0.5) * size, (0.5) * size,  (-0.5) * size))
        self.vertices.append(R4Vector((0.5) * size,  (-0.5) * size, (0.5) * size,  (-0.5) * size))
        self.vertices.append(R4Vector((0.5) * size,  (0.5) * size,  (-0.5) * size, (-0.5) * size))
        self.vertices.append(R4Vector((-0.5) * size, (0.5) * size,  (-0.5) * size, (-0.5) * size))
        self.vertices.append(R4Vector((-0.5) * size, (-0.5) * size, (-0.5) * size, (-0.5) * size))
        self.vertices.append(R4Vector((0.5) * size,  (-0.5) * size, (-0.5) * size, (-0.5) * size))

    def display(self, world):
        counter = 0
        for vertex in self.vertices:
            #print(vertex)
            newVector = vertex.projection()
            #print(newVector)
            #pygame.draw.circle(world.screen, (255, 255, 255), (newVector.vector[0] + 500, newVector.vector[1] + 300), 5)
        for i in range(4):
            pygame.draw.line(world.screen, (255, 255, 255), (self.vertices[i].projection().vector[0] * 100 + 500, 
                                                             self.vertices[i].projection().vector[1] * 100 + 300),
                                                            (self.vertices[(i + 1) % 4].projection().vector[0] * 100 + 500,
                                                             self.vertices[(i + 1) % 4].projection().vector[1] * 100 + 300))
            pygame.draw.line(world.screen, (255, 255, 255), (self.vertices[i].projection().vector[0] * 100 + 500, 
                                                             self.vertices[i].projection().vector[1] * 100 + 300),
                                                            (self.vertices[i + 4].projection().vector[0] * 100 + 500,
                                                             self.vertices[i + 4].projection().vector[1] * 100 + 300))                                                 
        for j in range(4):
            pygame.draw.line(world.screen, (255, 255, 255), (self.vertices[j + 4].projection().vector[0] * 100 + 500, 
                                                             self.vertices[j + 4].projection().vector[1] * 100 + 300),
                                                            (self.vertices[(j + 1) % 4 + 4].projection().vector[0] * 100 + 500,
                                                             self.vertices[(j + 1) % 4 + 4].projection().vector[1] * 100 + 300))
        for i in range(4):
            pygame.draw.line(world.screen, (255, 255, 255), (self.vertices[i + 8].projection().vector[0] * 100 + 500, 
                                                             self.vertices[i + 8].projection().vector[1] * 100 + 300),
                                                            (self.vertices[(i + 1) % 4 + 8].projection().vector[0] * 100 + 500,
                                                             self.vertices[(i + 1) % 4 + 8].projection().vector[1] * 100 + 300))
            pygame.draw.line(world.screen, (255, 255, 255), (self.vertices[i + 8].projection().vector[0] * 100 + 500, 
                                                             self.vertices[i + 8].projection().vector[1] * 100 + 300),
                                                            (self.vertices[i + 12].projection().vector[0] * 100 + 500,
                                                             self.vertices[i + 12].projection().vector[1] * 100 + 300))                                                 
        for j in range(4):
            pygame.draw.line(world.screen, (255, 255, 255), (self.vertices[j + 12].projection().vector[0] * 100 + 500, 
                                                             self.vertices[j + 12].projection().vector[1] * 100 + 300),
                                                            (self.vertices[(j + 1) % 4 + 12].projection().vector[0] * 100 + 500,
                                                             self.vertices[(j + 1) % 4 + 12].projection().vector[1] * 100 + 300))
        for k in range(8):
            pygame.draw.line(world.screen, (255, 255, 255), (self.vertices[k].projection().vector[0] * 100 + 500, 
                                                             self.vertices[k].projection().vector[1] * 100 + 300),
                                                            (self.vertices[k + 8].projection().vector[0] * 100 + 500,
                                                             self.vertices[k + 8].projection().vector[1] * 100 + 300))   


    def rotateXY(self, theta):
        rotationMatrix = Matrix(4, 4)
        rotationMatrix.values = [[math.cos(theta), math.sin(theta), 0, 0],
                                 [(-1) * math.sin(theta), math.cos(theta), 0, 0],
                                 [0, 0, 1, 0],
                                 [0, 0, 0, 1]]
        for i in range(len(self.vertices)):
            self.vertices[i] = matMult(rotationMatrix, self.vertices[i])

    def rotateYZ(self, theta):
        rotationMatrix = Matrix(4, 4)
        rotationMatrix.values = [[1, 0, 0, 0],
                                 [0, math.cos(theta), math.sin(theta), 0],
                                 [0, (-1) * math.sin(theta), math.cos(theta), 0],
                                 [0, 0, 0, 1]]
        for i in range(len(self.vertices)):
            self.vertices[i] = matMult(rotationMatrix, self.vertices[i])

    def rotateXZ(self, theta):
        rotationMatrix = Matrix(4, 4)
        rotationMatrix.values = [[math.cos(theta), 0, (-1) * math.sin(theta), 0],
                                 [0, 1, 0, 0],
                                 [math.sin(theta), 0, math.cos(theta), 0],
                                 [0, 0, 0, 1]]
        for i in range(len(self.vertices)):
            self.vertices[i] = matMult(rotationMatrix, self.vertices[i])

    def rotateXW(self, theta):
        rotationMatrix = Matrix(4, 4)
        rotationMatrix.values = [[math.cos(theta), 0, 0, math.sin(theta)],
                                 [0, 1, 0, 0],
                                 [0, 0, 1, 0],
                                 [(-1) * math.sin(theta), 0, 0, math.cos(theta)]]
        for i in range(len(self.vertices)):
            self.vertices[i] = matMult(rotationMatrix, self.vertices[i])

    def rotateYW(self, theta):
        rotationMatrix = Matrix(4, 4)
        rotationMatrix.values = [[1, 0, 0, 0],
                                 [0, math.cos(theta), 0, (-1) * math.sin(theta)],
                                 [0, 0, 1, 0],
                                 [0, math.sin(theta), 0, math.cos(theta)]]
        for i in range(len(self.vertices)):
            self.vertices[i] = matMult(rotationMatrix, self.vertices[i])

    def rotateZW(self, theta):
        rotationMatrix = Matrix(4, 4)
        rotationMatrix.values = [[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, math.cos(theta), (-1) * math.sin(theta)],
                                 [0, 0, math.sin(theta), math.cos(theta)]]
        for i in range(len(self.vertices)):
            self.vertices[i] = matMult(rotationMatrix, self.vertices[i])

    





