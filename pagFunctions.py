from random import randint
import os, pygame


def load_images():

    def load_image_game(img_file_name):
        file_name = os.path.join('.', 'images', img_file_name)
        img = pygame.image.load(file_name)
        img.convert()
        return img

    return {'background': load_image_game('background_' + str(randint(1, 4)) + '.png'),
            'upFlap': load_image_game('upFlap.png'),
            'downFlap': load_image_game('downFlap.png'),
            'upPipe': load_image_game('upPipe.png'),
            'downPipe': load_image_game('downPipe.png'),
            'ground': load_image_game('ground.png')}