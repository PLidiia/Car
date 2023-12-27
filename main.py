import pygame

FPS = 30
VELOCITY = 10


class Car(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.const_image = pygame.image.load('data/car.png')
        self.image = self.const_image
        self.rect = self.image.get_rect()
        self.side = 'right'

    def update(self):
        if self.side == 'right':
            if self.rect.right < 600:
                self.rect.move_ip(VELOCITY, 0)
            else:
                self.side = 'left'
                # flip_x, flip_y
                # обновляем фотографию
                self.image = pygame.transform.flip(self.const_image, True, False)
        else:
            if self.rect.left > 0:
                self.rect.move_ip(-VELOCITY, 0)
            else:
                self.side = 'right'
                self.image = self.const_image


if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Машинка')
    group = pygame.sprite.Group()
    car = Car(group)
    car.rect.x = 0
    car.rect.y = 0
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        group.update()
        screen.fill((255, 255, 255))
        group.draw(screen)
        pygame.display.flip()
