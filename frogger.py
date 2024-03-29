import turtle
import math
import time
import random

image_dir = "/Users/kacper/Downloads/VSCode Practice/hello/Frogger/"

wn = turtle.Screen()
#wn.cv._rootwindow.resizable(False, False)
wn.title("Frogger")
wn.setup(600, 800)
wn.bgcolor("green")
#wn.bgpic(image_dir + "background.gif")
wn.tracer(0)

shapes = ["frog.gif", "car_right.gif", "car_left.gif", "log_full.gif", "turtle_left.gif", "turtle_right.gif", "turtle_left_half.gif", "turtle_right_half.gif", "turtle_submerged.gif", "goal.gif", "frog_home.gif", "frog_small.gif"]
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
        self.collision = False
        self.frogs_home = 0
        self.time_remaining = 60
        self.max_time = 60
        self.start_time = time.time()
        self.lives = 3

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
            self.go_home()

        self.time_remaining = self.max_time - round(time.time() - self.start_time)

        if self.time_remaining <= 0:
            player.lives -= 1
            self.go_home()

    def go_home(self):
        self.dx = 0
        self.x = 0
        self.y = -300
        self.time_remaining = 60
        self.start_time = time.time()

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

class Home(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)

class Timer():
    def __init__(self, max_time):
        self.x = 200
        self.y = -350
        self.max_time = max_time
        self.width = 200

    def render(self, time, pen):
        pen.color("red")
        pen.pensize(5)
        pen.penup()
        pen.goto(self.x, self.y)
        pen.pendown()
        percent = time/self.max_time
        dx = percent * self.width
        pen.goto(self.x - dx, self.y)
        pen.penup()

player = Player(0, -300, 40, 40, image_dir + "frog.gif")
timer = Timer(60)
car_speed = random.uniform(1.0,2.0)
log_speed = random.uniform(1.5,2.5)
turtle_speed = random.uniform(1.0,1.5)

level_1 = [
    Car(0, -250, 121, 40, image_dir + "car_left.gif", -car_speed),
    Car(random.randint(100, 200) + 121, -250, 121, 40, image_dir + "car_left.gif", -car_speed),

    Car(0, -200, 121, 40, image_dir + "car_right.gif", car_speed),
    Car(random.randint(100, 200) + 121, -200, 121, 40, image_dir + "car_right.gif", car_speed),

    Car(0, -150, 121, 40, image_dir + "car_left.gif", -car_speed),
    Car(random.randint(100, 200) + 121, -150, 121, 40, image_dir + "car_left.gif", -car_speed),

    Car(0, -100, 121, 40, image_dir + "car_right.gif", car_speed),
    Car(random.randint(100, 200) + 121, -100, 121, 40, image_dir + "car_right.gif", car_speed),

    Car(0, -50, 121, 40, image_dir + "car_left.gif", -car_speed),
    Car(random.randint(100, 200) + 121, -50, 121, 40, image_dir + "car_left.gif", -car_speed),

    Log(0, 50, 161, 40, image_dir + "log_full.gif", log_speed),
    Log(random.randint(100, 200) + 161, 50, 161, 40, image_dir + "log_full.gif", log_speed),

    Log(0, 150, 161, 40, image_dir + "log_full.gif", -log_speed),
    Log(random.randint(100, 200) + 161, 150, 161, 40, image_dir + "log_full.gif", -log_speed),

    Log(0, 250, 161, 40, image_dir + "log_full.gif", log_speed),
    Log(random.randint(100, 200) + 161, 250, 161, 40, image_dir + "log_full.gif", log_speed),

    Turtle(0, 100, 155, 40, image_dir + "turtle_right.gif", turtle_speed),
    Turtle(random.randint(100, 200) + 155, 100, 155, 40, image_dir + "turtle_right.gif", turtle_speed),

    Turtle(0, 200, 250, 40, image_dir + "turtle_left.gif", -turtle_speed),
    Turtle(random.randint(100, 200) + 155, 200, 250, 40, image_dir + "turtle_left.gif", -turtle_speed)
]

homes = [
    Home(0, 300, 50, 50, image_dir + "goal.gif"),
    Home(-100, 300, 50, 50, image_dir + "goal.gif"),
    Home(-200, 300, 50, 50, image_dir + "goal.gif"),
    Home(100, 300, 50, 50, image_dir + "goal.gif"),
    Home(200, 300, 50, 50, image_dir + "goal.gif")
]

sprites = level_1 + homes
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

    timer.render(player.time_remaining, pen)

    pen.goto(-250, -350)
    pen.shape(image_dir + "frog_small.gif")
    for life in range(player.lives):
        pen.goto(-275 + (life * 30), -350)
        pen.stamp()

    player.dx = 0
    player.collision = False

    for sprite in sprites:
        if player.is_collision(sprite):
            if isinstance(sprite, Car):
                player.lives -= 1
                player.go_home()
                break
            elif isinstance(sprite, Log):
                player.dx = sprite.dx
                player.collision = True
                break
            elif isinstance(sprite, Turtle) and sprite.state != "submerged":
                player.dx = sprite.dx
                player.collision = True
                break
            elif isinstance(sprite, Home):
                player.go_home()
                player.frogs_home += 1
                sprite.image = image_dir + "frog.gif"
                break
    
    if player.y > 0 and not player.collision:
        player.lives -= 1
        player.go_home()

    if player.frogs_home == 5:
        player.go_home()
        player.frogs_home = 0
        for home in homes:
            home.image = image_dir + "goal.gif"

    if player.lives == 0:
        player.go_home()
        player.frogs_home = 0
        for home in homes:
            home.image = image_dir + "goal.gif"
        player.lives = 3
    
    wn.update()
    pen.clear()