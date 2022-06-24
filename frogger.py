import turtle

image_dir = "/Users/kacper/Downloads/VSCode Practice/hello/Frogger/"

wn = turtle.Screen()
wn.title("Frogger")
wn.setup(600, 800)
wn.bgcolor("black")
wn.tracer(0)

wn.register_shape(image_dir + "frog.gif")
wn.register_shape(image_dir + "car_left.gif")

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

class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)

    def up(self):
        self.y += 45

    def down(self):
        self.y -= 45
    
    def right(self):
        self.x += 45
    
    def left(self):
        self.x -= 45

class Car(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
    

player = Player(0, -300, 40, 40, image_dir + "frog.gif")
player.render(pen)

car_left = Car(0, -255, 40, 121, image_dir + "car_left.gif", 45)

wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.right, "Right")
wn.onkeypress(player.left, "Left")

while True:
    player.render(pen)
    car_left.render(pen)
    wn.update()
    pen.clear()

wn.mainloop()