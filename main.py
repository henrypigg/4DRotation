from matrix import HyperCube
import pygame
import math

def main():
    pygame.init()

    world = World([1000, 600])

    newCube = HyperCube(150)
    world.nodes.append(newCube)

    running = True
    pressedX = False
    pressedY = False
    pressedZ = False
    pressedW = False
    pressedV = False
    pressedU = False
    pressedLShift = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    pressedX = True
                if event.key == pygame.K_y:
                    pressedY = True
                if event.key == pygame.K_z:
                    pressedZ = True
                if event.key == pygame.K_w:
                    pressedW = True
                if event.key == pygame.K_v:
                    pressedV = True
                if event.key == pygame.K_u:
                    pressedU = True
                if event.key == pygame.K_LSHIFT:
                    pressedLShift = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_x:
                    pressedX = False
                if event.key == pygame.K_y:
                    pressedY = False
                if event.key == pygame.K_z:
                    pressedZ = False
                if event.key == pygame.K_w:
                    pressedW = False
                if event.key == pygame.K_v:
                    pressedV = False
                if event.key == pygame.K_u:
                    pressedU = False
                if event.key == pygame.K_LSHIFT:
                    pressedLShift = False
    
        if pressedX:
            if pressedLShift:
                newCube.rotateXY(math.pi / 64 * -0.1)
            else:
                newCube.rotateXY(math.pi / 64 * 0.1)
        if pressedY:
            if pressedLShift:
                newCube.rotateYZ(math.pi / 64 * -0.1)
            else:
                newCube.rotateYZ(math.pi / 64 * 0.1)
        if pressedZ:
            if pressedLShift:
                newCube.rotateXZ(math.pi / 64 * -0.1)
            else:
                newCube.rotateXZ(math.pi / 64 * 0.1)
        if pressedW:
            if pressedLShift:
                newCube.rotateXW(math.pi / 64 * -0.1)
            else:
                newCube.rotateXW(math.pi / 64 * 0.1)
        if pressedV:
            if pressedLShift:
                newCube.rotateYW(math.pi / 64 * -0.1)
            else:
                newCube.rotateYW(math.pi / 64 * 0.1)
        if pressedU:
            if pressedLShift:
                newCube.rotateZW(math.pi / 64 * -0.1)
            else:
                newCube.rotateZW(math.pi / 64 * 0.1)

        world.update()


class World:
    def __init__(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.fps = 240
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(self.fps)
        self.nodes = []

    def update(self):
        self.screen.fill((0, 0, 0))
        for node in self.nodes:
            node.display(self)
        
        pygame.display.flip()


if __name__ == "__main__":
    main()
