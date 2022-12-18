import pygame
import math
import random

pygame.init()
pygame.display.set_caption('laba2')
width = 1400
height = 800
resizeble = True
window = pygame.display.set_mode((width, height), resizeble)

class glo:
    count_sqrt = 0
    count_balls = 0
balls = random.randint(5, 6)
radius_balls = []
mass_balls = []
x_position_balls = []
y_position_balls = []
acceleration_balls = []
velocity_balls = []
color_balls = []


def create_balls():
    for i in range(0, balls):
        radius_balls.append(random.randint(10, 100))
        mass_balls.append(radius_balls[i] / 100)
        x_position_balls.append(random.randint(0+radius_balls[i], width-radius_balls[i]))
        y_position_balls.append(random.randint(0+radius_balls[i], height-radius_balls[i]))
        acceleration_balls.append(math.pi*random.randint(0, 5)/3)
        velocity_balls.append(random.randint(1, 2))
        color_balls.append((random.randint(0, 225), random.randint(0, 225), random.randint(0, 225)))

sqrt = random.randint(5, 6)
mass_sqrt = []
x_position_sqrt = []
y_position_sqrt = []
width_sqrt = []
height_sqrt = []
acceleration_sqrt = []
velocity_sqrt = []
color_sqrt = []
def create_sqrt():
    for i in range(0, sqrt):
        width_sqrt.append(random.randint(5, 100))
        height_sqrt.append(random.randint(50, 100))
        mass_sqrt.append(width_sqrt[i]*height_sqrt[i] / 100)
        x_position_sqrt.append(random.randint(0, width))
        y_position_sqrt.append(random.randint(0, height))
        acceleration_sqrt.append(math.pi*random.randint(0, 5)/3)
        velocity_sqrt.append(random.randint(1, 2))
        color_sqrt.append((random.randint(0, 225), random.randint(0, 225), random.randint(0, 225)))


def position_balls():        
    for i in range(0, balls):
        x_position_balls[i] += velocity_balls[i] * math.cos(acceleration_balls[i])
        y_position_balls[i] += velocity_balls[i] * math.sin(acceleration_balls[i])
        pygame.draw.circle(window, color_balls[i], (x_position_balls[i], y_position_balls[i]), radius_balls[i])
        

def position_sqrt():        
    for i in range(0, sqrt):
        x_position_sqrt[i] += velocity_sqrt[i] * math.cos(acceleration_sqrt[i])
        y_position_sqrt[i] += velocity_sqrt[i] * math.sin(acceleration_sqrt[i])
        pygame.draw.rect(window ,color_sqrt[i], (x_position_sqrt[i], y_position_sqrt[i], width_sqrt[i], height_sqrt[i]))


def check_wall_balls():
    for i in range(0, balls):
        if x_position_balls[i] <= radius_balls[i] and (acceleration_balls[i] > math.pi / 2 or acceleration_balls[i] < - math.pi / 2):
            acceleration_balls[i] = math.pi - acceleration_balls[i]
            glo.count_balls += 1
        if x_position_balls[i] >= width-radius_balls[i] and (acceleration_balls[i] > -math.pi / 2 and acceleration_balls[i] < math.pi/2):
            glo.count_balls += 1
            
            acceleration_balls[i] = math.pi - acceleration_balls[i]
        if y_position_balls[i] <= radius_balls[i] and (acceleration_balls[i] < 0 and acceleration_balls[i]>-math.pi):
            glo.count_balls += 1
            acceleration_balls[i] = -acceleration_balls[i]
        if y_position_balls[i] >= height - radius_balls[i] and (acceleration_balls[i] >0 and acceleration_balls[i] < math.pi):
            glo.count_balls += 1
            acceleration_balls[i] = -acceleration_balls[i]

        while acceleration_balls[i] > math.pi: acceleration_balls[i] -= 2 * math.pi
        while acceleration_balls[i] < -math.pi: acceleration_balls[i] += 2*math.pi


def check_wall_sqrt():
    for i in range(0, sqrt):
        if x_position_sqrt[i] <= 0 and (acceleration_sqrt[i]>math.pi/2 or acceleration_sqrt[i] < -math.pi/2):
            acceleration_sqrt[i] = math.pi - acceleration_sqrt[i]
            glo.count_sqrt += 1
        if x_position_sqrt[i] >= width-width_sqrt[i] and (acceleration_sqrt[i] > -math.pi / 2 and acceleration_sqrt[i] < math.pi/2):
            glo.count_sqrt += 1
            acceleration_sqrt[i] = math.pi - acceleration_sqrt[i]
        if y_position_sqrt[i] <= 0 and (acceleration_sqrt[i] < 0 and acceleration_sqrt[i]>-math.pi):
            glo.count_sqrt += 1
            acceleration_sqrt[i] = -acceleration_sqrt[i]
        if y_position_sqrt[i] >= height - height_sqrt[i] and (acceleration_sqrt[i] >0 and acceleration_sqrt[i] < math.pi):
            glo.count_sqrt += 1
            acceleration_sqrt[i] = -acceleration_sqrt[i]

        while acceleration_sqrt[i] > math.pi: acceleration_sqrt[i] -= 2 * math.pi
        while acceleration_sqrt[i] < -math.pi: acceleration_sqrt[i] += 2*math.pi



def check_other_object():
    for i in range(0, balls):
        for j in range (1, balls):
            rast = ((x_position_balls[i]-x_position_balls[j])**2 + (y_position_balls[i]-y_position_balls[j])**2)**0.5
            if rast <= radius_balls[i] + radius_balls[j]:
                x_position_balls_1_new = x_position_balls[i] + velocity_balls[i]*0.9* math.cos(acceleration_balls[i])
                y_position_balls_1_new = y_position_balls[i] + velocity_balls[i]*0.9* math.sin(acceleration_balls[i])
                x_position_balls_2_new = x_position_balls[j] + velocity_balls[j]*0.9* math.cos(acceleration_balls[j])
                y_position_balls_2_new = y_position_balls[j] + velocity_balls[j]*0.9* math.sin(acceleration_balls[j])
                rast_new = ((x_position_balls_1_new - x_position_balls_2_new)**2 + (y_position_balls_1_new - y_position_balls_2_new)**2)**0.5
                if rast > rast_new:
                    bb = math.atan((y_position_balls[j] - y_position_balls[i])/(x_position_balls[j]-x_position_balls[i]))
                    if x_position_balls[j] - x_position_balls[i]<0:
                        bb += math.pi
                        while bb > math.pi/2: bb -=2*math.pi
                        while bb < -math.pi/2: bb +=2*math.pi
                    w1 = acceleration_balls[i] - bb
                    w2 = acceleration_balls[j] - bb
                    vw1 = velocity_balls[i]*math.cos(w1)
                    vw2 = velocity_balls[j]*math.cos(w2)
                    vwt1 = velocity_balls[i]*math.sin(w1)
                    vwt2 = velocity_balls[j]*math.sin(w2)

                    vw1 = (2 * mass_balls[j]*velocity_balls[j]*math.cos(w2))+(mass_balls[i]-mass_balls[j])*velocity_balls[i]*math.cos(w1)/(mass_balls[i]+mass_balls[j])
                    vw2 = (2 * mass_balls[i]*velocity_balls[i]*math.cos(w1))+(mass_balls[j]-mass_balls[i])*velocity_balls[j]*math.cos(w2)/(mass_balls[i]+mass_balls[j])

                    # velocity_balls[i] = (vw1 ** 2+ vwt1 **2) **0.5
                    # velocity_balls[j] = (vw2**2+vwt2**2)**0.5

                    w1 = math.atan(vwt1/vw1)
                    if vw1 <0:w1 += math.pi
                    w2 = math.atan(vwt2/vw2)
                    if vw2 < 0: w2 += math.pi

                    acceleration_balls[i] = bb + w1
                    while acceleration_balls[i] > math.pi: acceleration_balls[i] -= 2*math.pi
                    while acceleration_balls[i] < - math.pi: acceleration_balls[i] += 2*math.pi
                    acceleration_balls[j]= bb + w2
                    while acceleration_balls[j] > math.pi: acceleration_balls[j] -= 2*math.pi
                    while acceleration_balls[j] < - math.pi: acceleration_balls[j] += 2*math.pi


def main():
    create_balls()
    create_sqrt()
    var = True
    while var:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                var = False
                print(f"Всего отскоков: {glo.count_sqrt+glo.count_balls}\nОтскоки шариков: {glo.count_balls}\nОтскоки прямоугольников: {glo.count_sqrt}")
        window.fill((225, 225, 225))
        position_balls() 
        position_sqrt()       
        pygame.time.delay(10)
        pygame.display.update()
        check_wall_balls()
        check_other_object()
        check_wall_sqrt()
    
    pygame.quit()


if __name__ == '__main__':
    main()