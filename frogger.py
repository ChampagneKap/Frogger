import turtle
import math
import time
import random

image_dir = "/Users/kacper/Downloads/VSCode Practice/hello/Frogger/"

wn = turtle.Screen()
wn.cv._rootwindow.resizable(False, False)
wn.title("Frogger")
wn.setup(600, 800)
wn.bgcolor("green")
wn.tracer(0)

shapes = ["frog.gif", "car_right.gif", "car_left.gif", "log_full.gif", "turtle_left.gif", "turtle_right.gif", "turtle_left_half.gif", "turtle_right_half.gif", "turtle_submerged.gif", "goal.gif"]
for shape in shapes:
    wn.register_shape(image_dir + shape)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

class Sprite():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()

    def is_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

    def update(self):
        pass

class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0

    def up(self):
        self.y += 50

    def down(self):
        self.y -= 50
    
    def right(self):
        self.x += 50
    
    def left(self):
        self.x -= 50

    def update(self):
        self.x += self.dx

        if self.x < -300 or self.x > 300 or self.y < -300:
            self.x = 0
            self.y = -300

class Car(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx

    def update(self):
        self.x += self.dx

        if self.x < -400:
            self.x = 400
        elif self.x > 400:
            self.x = -400

class Log(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx

    def update(self):
        self.x += self.dx

        if self.x < -400:
            self.x = 400
        elif self.x > 400:
            self.x = -400

class Turtle(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
        self.state = "full"
        self.full_time = random.randint(8,12)
        self.half_time = random.randint(4,6)
        self.submerged_time = random.randint(4,6)
        self.start_time = time.time()

    def update(self):
        self.x += self.dx

        if self.x < -400:
            self.x = 400
        elif self.x > 400:
            self.x = -400

        if self.state == "full":
            if self.dx > 0:
                self.image = image_dir + "turtle_right.gif"
            else:
                self.image = image_dir + "turtle_left.gif"
        elif self.state.__contains__("half"):
            if self.dx > 0:
                self.image = image_dir + "turtle_right_half.gif"
            else:
                self.image = image_dir + "turtle_left_half.gif"
        else:
            self.image = image_dir + "turtle_submerged.gif"

        if self.state == "full" and time.time() - self.start_time > self.full_time:
            self.state = "half_down"
            self.start_time = time.time()
        elif self.state == "half_down" and time.time() - self.start_time > self.half_time:
            self.state = "submerged"
            self.start_time = time.time()
        elif self.state == "submerged" and time.time() - self.start_time > self.submerged_time:
            self.state = "half_up"
            self.start_time = time.time()
        elif self.state == "half_up" and time.time() - self.start_time > self.half_time:
            self.state = "full"
            self.start_time = time.time()

    

player = Player(0, -300, 40, 40, image_dir + "frog.gif")

car_left = Car(0, -250, 121, 40, image_dir + "car_left.gif", -random.uniform(0.5,2.0))
car_right = Car(0, -200, 121, 40, image_dir + "car_right.gif", random.uniform(0.5,2.0))
car_left_2 = Car(0, -150, 121, 40, image_dir + "car_left.gif", -random.uniform(0.5,2.0))
car_right_2 = Car(0, -100, 121, 40, image_dir + "car_right.gif", random.uniform(0.5,2.0))
car_left_3 = Car(0, -50, 121, 40, image_dir + "car_left.gif", -random.uniform(0.5,2.0))

log_right = Log(0, 50, 121, 40, image_dir + "log_full.gif", random.uniform(1.5,2.5))
log_left = Log(0, 150, 121, 40, image_dir + "log_full.gif", -random.uniform(1.5,2.5))
log_right_2 = Log(0, 250, 250, 40, image_dir + "log_full.gif", random.uniform(1.5,2.5))

turtle_right = Turtle(0, 100, 155, 40, image_dir + "turtle_right.gif", random.uniform(1.0,1.5))
turtle_left = Turtle(0, 200, 250, 40, image_dir + "turtle_left.gif", -random.uniform(1.0,1.5))

goal_1 = Sprite(0, 300, 50, 50, "goal.gif")
goal_2 = Sprite(-100, 300, 50, 50, "goal.gif")
goal_3 = Sprite(-200, 300, 50, 50, "goal.gif")
goal_4 = Sprite(-300, 300, 50, 50, "goal.gif")
goal_5 = Sprite(-400, 300, 50, 50, "goal.gif")

sprites = [car_left, car_right, car_left_2, car_right_2, car_left_3, log_left, log_right, log_right_2, turtle_right, turtle_left, goal_1, goal_2, goal_3, goal_4, goal_5]
sprites.append(player)

wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.right, "Right")
wn.onkeypress(player.left, "Left")

while True:
    for sprite in sprites:
        sprite.render(pen)
        sprite.update()

    player.dx = 0

    for sprite in sprites:
        if player.is_collision(sprite):
            if isinstance(sprite, Car):
                player.x = 0
                player.y = -300
                break
            elif isinstance(sprite, Log):
                player.dx = sprite.dx
                break
            elif isinstance(sprite, Turtle) and sprite.state != "submerged":
                player.dx = sprite.dx
                break
    
    wn.update()
    pen.clear()