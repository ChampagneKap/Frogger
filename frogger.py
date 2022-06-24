import turtle
import math

image_dir = "/Users/kacper/Downloads/VSCode Practice/hello/Frogger/"

wn = turtle.Screen()
wn.cv._rootwindow.resizable(False, False)
wn.title("Frogger")
wn.setup(600, 800)
wn.bgcolor("black")
wn.tracer(0)

shapes = ["frog.gif", "car_right.gif", "car_left.gif", "log_full.gif", "turtle_left.gif", "turtle_right.gif"]
for shape in shapes:
    wn.register_shape(image_dir + shape)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

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

    def update(self):
        self.x += self.dx

        if self.x < -400:
            self.x = 400
        elif self.x > 400:
            self.x = -400
    

player = Player(0, -300, 40, 40, image_dir + "frog.gif")
car_left = Car(0, -250, 121, 40, image_dir + "car_left.gif", -1)
car_right = Car(0, -200, 121, 40, image_dir + "car_right.gif", 1)
log_right = Log(0, -150, 121, 40, image_dir + "log_full.gif", 2)
log_left = Log(0, -100, 121, 40, image_dir + "log_full.gif", -2)
turtle_right = Turtle(0, -50, 121, 40, image_dir + "turtle_right.gif", 1.5)
turtle_left = Turtle(0, 0, 121, 40, image_dir + "turtle_left.gif", -1.5)

sprites = [car_left, car_right, log_left, log_right, turtle_right, turtle_left]
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
            elif isinstance(sprite, Turtle):
                player.dx = sprite.dx
                break
    
    wn.update()
    pen.clear()