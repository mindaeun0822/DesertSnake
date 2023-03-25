import js
p5 = js.window
program_state = 'start'
defalultFt = p5.loadFont('PressStart2P.otf')


#snake class
class Snake:
    x = 130
    y = 212
    snake_img = p5.loadImage('snake.png')
    
    def draw(self):
        p5.image(self.snake_img, self.x, self.y)


class SnakeDead(Snake):
    snakedead_img = p5.loadImage('snakedead.png')
    def draw(self, x, y):
        p5.image(self.snakedead_img, x, y)


#background class
class Background:
    x = 0
    y = 0
    bg_img = p5.loadImage('background.png')
    
    def draw(self):
        p5.image(self.bg_img, self.x, self.y)


class Projectile:
    x = 0
    y = 0
    speed = 0
    rain_img = p5.loadImage('raindrop.png')


    def __init__(self,x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        
class Raindrop(Projectile):
    rain_img = p5.loadImage('raindrop.png')
    def draw(self):
        p5.image(self.rain_img, self.x, self.y)


class Lightening(Projectile):
    light_img = p5.loadImage('lightening.png')
    def draw(self):
        p5.image(self.light_img, self.x, self.y)


#setup
def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 


snake = Snake()
snakedead = SnakeDead()
background = Background()
raindrop = Raindrop(p5.random(1,300),73,0.5)
light = Lightening(p5.random(1,300), 73, 0.5)

score = 0
life = 2

#draw
def draw():

    global program_state
    global score
    global life
    
    p5.background(255)
    background.draw()
    snake.draw()

    disRain = p5.dist(raindrop.x, raindrop.y, snake.x, snake.y)
    disLight = p5.dist(light.x, light.y, snake.x, snake.y)


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
        if (score > 0):
            light.draw()
            light.y += light.speed
        
        if (raindrop.y == 226):
            resetProj(raindrop)
        if (light.y == 226):
            resetProj(light)

        if (disRain <= 27):
            score += 1
            resetProj(raindrop)
        if (disLight <= 27):
            life -= 1
            resetProj(light)
            program_state = 'pause'

    elif (program_state == 'pause'):
        p5.fill(35, 38, 79)
        p5.textFont(defalultFt)
        p5.textSize(18)
        p5.text('Ouch!', 120, 115)
        p5.textSize(10)
        p5.text('press any key to continue.', 20,130) 

        p5.fill(255)
        p5.textFont(defalultFt)
        p5.textSize(10)
        p5.text('Score:' + str(score), 15, 25)
        p5.text('Life:x' + str(life), 218, 25)

        snakedead.draw(snake.x, snake.y)




def resetProj(proj):
    proj.y = 73
    proj.x = p5.random(20,280)
    
def keyPressed(event):
    global program_state
    
    if (program_state == 'start'):
        program_state = 'play'

    if (program_state =='play'):
        if (p5.key == 'ArrowLeft' and snake.x >-5 and snake.x < 251):
            snake.x -= 10

        if (p5.key == 'ArrowRight' and snake.x >-5 and snake.x < 251):

            snake.x += 10


def keyReleased(event):
    pass


def mousePressed(event):
    pass


def mouseReleased(event):
    pass
