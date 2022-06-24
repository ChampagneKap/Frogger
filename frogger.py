import turtle

wn = turtle.Screen()
wn.title("Frogger")
wn.setup(600, 800)
wn.bgcolor("black")

class Sprite():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

wn.mainloop()