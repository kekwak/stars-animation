from tkinter import *
from math import sin,cos,pi  # sqrt,acos,degrees
from random import uniform

size = (600, 600)

root = Tk()
canvas = Canvas(root, background='black', width=size[0], height=size[1])
root.title('Space Explorer (W/S to Manipulate)')
canvas.pack()

center = (size[0]/2, size[1]/2)

class Star():
    speed = 1
    angle_degrees = 0
    X, Y = 0, 0
    
    def __init__(self, dist, custom_center=center):
        self.dist = dist
        self.size = 0
        
        self.center = custom_center
        
        if Star.angle_degrees:
            self.dir = pi / 180 * uniform(Star.angle_degrees-15, Star.angle_degrees+15)
        else:
            self.dir = pi / 180 * uniform(0, 360)
        
        self.x, self.y = cos(self.dir)*self.dist, sin(self.dir)*self.dist
        
        self.counter = 1
        
        self.star = canvas.create_oval(
            self.center[0] + self.x - self.size,
            self.center[1] + self.y - self.size,
            self.center[0] + self.x + self.size,
            self.center[1] + self.y + self.size,
            fill='white'  # lightblue
            )
        
    def keypress(event):
        match event.keycode:
            case 218103927 | 2113992448:  # w or up
                Star.speed += 0.4
            case 16777331 | 2097215233:  # s or down
                Star.speed -= 0.4
        if Star.speed < 0:
            Star.speed = 0
        # print(event.keycode)
    
    # def motion(event):
    #     X, Y = event.x - center[0], event.y - center[1]
        
    #     if X**2 + Y**2 <= 100 or abs(X) > 300 or abs(Y) > 300:
    #         Star.angle_degrees = None
    #         return
        
    #     vector1 = [1, 0]
    #     vector2 = [X, Y]

    #     dot_product = sum(x * y for x, y in zip(vector1, vector2))

    #     magnitude1 = sqrt(sum(x ** 2 for x in vector1))
    #     magnitude2 = sqrt(sum(x ** 2 for x in vector2))

    #     cosine_angle = dot_product / (magnitude1 * magnitude2)

    #     angle_degrees = degrees(acos(cosine_angle))
        
    #     Star.angle_degrees = 360 - angle_degrees
    #     if Y >= 0:
    #         Star.angle_degrees = angle_degrees
    
    def move(self):
        dif = 1 + self.dist / 100
        self.dist += (dif**2) * Star.speed
        self.size += (self.counter / dif / 150) * Star.speed
        
        self.counter += 1 * Star.speed
        
        # self.size += log(self.counter / self.dist, e) / 15
        
        self.x, self.y = cos(self.dir)*self.dist, sin(self.dir)*self.dist
        
        canvas.coords(
            self.star,
            self.center[0] + self.x - self.size,
            self.center[1] + self.y - self.size,
            self.center[0] + self.x + self.size,
            self.center[1] + self.y + self.size
            )
        
        if self.dist >= 480*1.5:
            return False
        return True

def move():
    for star_iter in Stars:
        move_result = star_iter.move()
        
        if not move_result:
            Stars[Stars.index(star_iter)] = Star(uniform(0, 450))
    
    root.after(16, move)


if __name__ == '__main__':
    Stars = [Star(uniform(0, 450)) for _ in range(50)]

    move()
        
    root.bind('<KeyPress>', Star.keypress)
    # root.bind('<Motion>', Star.motion)
    
    root.mainloop()