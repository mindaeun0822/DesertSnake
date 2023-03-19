import js
p5 = js.window
program_state = 'start'
defalultFt = p5.loadFont('PressStart2P.otf')

#snake class
class Snake:
    x = 130
    y = 212
    snake_img = p5.loadImage('snake.png')
    snakedead_img = p5.loadImage('snakedead.png')
    
    def draw(self):
        p5.image(self.snake_img, self.x, self.y)

#background class
class Background:
    x = 0
    y = 0
    bg_img = p5.loadImage('background.png')
    
    def draw(self):
        p5.image(self.bg_img, self.x, self.y)


class Raindrop:
    x = 0
    y = 0
    speed = 0
    rain_img = p5.loadImage('raindrop.png')

    def __init__(self,x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        
    def draw(self):
        p5.image(self.rain_img, self.x, self.y)

class Lightening:
    x = 0
    y = 0
    speed = 0
    light_img = p5.loadImage('lightening.png')

    def __init__(self,x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        
    def draw(self):
        p5.image(self.light_img, self.x, self.y)

#setup
def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 

snake = Snake()
background = Background()
raindrop = Raindrop(p5.random(1,300),73,0.5)
light = Lightening(p5.random(1,300), 73, 0.5)

#draw
def draw():

    global program_state
    
    p5.background(255)
    background.draw()
    snake.draw()
    score = 0
    life = 2

    if (program_state == 'start'):
        p5.fill(35, 38, 79)
        p5.textFont(defalultFt)
        p5.textSize(18)
        p5.text('Desert Snake', 46, 115)
        p5.textSize(10)
        p5.text('press any key to start!', 40,130) 

    elif (program_state == 'play'):
        p5.fill(255)
        p5.textFont(defalultFt)
        p5.textSize(10)
        p5.text('Score:' + str(score), 15, 25)
        p5.text('Life:x' + str(life), 218, 25)

        raindrop.draw()
        raindrop.y += raindrop.speed
        if (raindrop.y == 226):
            raindrop.y = 73
            raindrop.x = p5.random(1,300)

        
        light.draw()
        light.y += light.speed
        if (light.y == 226):
            light.y = 73
            light.x = p5.random(1,300)

def keyPressed(event):
    global program_state
    
    if (program_state == 'start'):
        program_state = 'play'

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass
