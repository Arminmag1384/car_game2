import pygame
import sys
import time

pygame.init()

# VARIABLE
width = 1000
length = 700
road_y = 0
car_movment = 0
road_image = pygame.image.load('Assets/car_image/road_up.jpg')
road = pygame.transform.scale(road_image, (350, 1000))
red_car_image = pygame.image.load('Assets/car_image/Audi.png')
red_car = pygame.transform.scale(red_car_image, (230, 250))


# WINDOW
main_scrin = pygame.display.set_mode((length, width))

def draw_window(red_car_rect,road, road_y):
    road_y += 1
    main_scrin.blit(road, (0, road_y))
    main_scrin.blit(road, (350, road_y))
    main_scrin.blit(road, (0, road_y - 1004))
    main_scrin.blit(road, (350, road_y - 1004))
    if road_y >= 1000:
        road_y = 0

    main_scrin.blit(red_car, (red_car_rect.x , red_car_rect.y))

    pygame.display.update()


def main():
    red_car_rect = pygame.Rect(100, 730, 230, 250) 

    # GAME TIME
    clock = pygame.time.Clock() 
    run = True
    while True:
        clock.tick(95)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.K_a:
                red_car_rect.x -= 10
   
        draw_window(red_car_rect, road, road_y)


    main()

if __name__ == "__main__":
    main()

