import js
p5 = js.window
program_state = 'start'
defalultFt = p5.loadFont('PressStart2P.otf')
rain_state = 0


#snake class
class Snake:
    x = 130
    y = 212
    snake_img = p5.loadImage('snake.png')
    snakedead_img = p5.loadImage('snakedead.png')
    
    def draw(self):
        global program_state

        if (program_state == 'start' or program_state == 'play'):
            p5.image(self.snake_img, self.x, self.y)

        if (program_state == 'pause' or program_state == 'gameOver'):
            p5.image(self.snakedead_img, self.x-29, self.y-25)



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

class Backdrop:  
    x = 0
    y = 0
    speed = 0

    def __init__(self, x = 0, y = 0, speed = 0):
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        if(self.y < 225):
            self.y += self.speed
        else:
            self.y = 80

    def draw(self):
        p5.rect(self.x, self.y, 2, 10) 

sprite_list = []  # empty list
selected_index = 0


    
#setup
def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 



snake = Snake()
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
    global sprite_list


        
    p5.background(255)
    background.draw()
    snake.draw()


    raineffect()

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
            
            if(life < 0):
                program_state = 'dead'
            else:
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

    elif (program_state == 'dead'):
        p5.fill(35, 38, 79)
        p5.textFont(defalultFt)
        p5.textSize(18)
        p5.text('Game Over!', 65, 115)
        p5.textSize(10)
        p5.text('Score: '+ str(score), 120,130) 




def raineffect():
    global rain_state

    if (rain_state == 0):
        sprite = Backdrop(x = 60, y = 60, speed = 1)  # create a Sprite object
        sprite_list.append(sprite)  # append sprite to sprite_list
        rain_state = 1

    if (rain_state ==1):
        sprite = Backdrop(x = 120, y = 120, speed = 1.5)  # create another Sprite object
        sprite_list.append(sprite)  # append sprite to sprite_list
        rain_state = 2

    if (rain_state ==2):
        sprite = Backdrop(x = 180, y = 180, speed = 1.2)  # create another Sprite object
        sprite_list.append(sprite)  # append sprite to sprite_list
        rain_state = 3

    if (rain_state ==3):
        sprite = Backdrop(x = 240, y = 240, speed = 1.7)  # create another Sprite object
        sprite_list.append(sprite)  # append sprite to sprite_list
        rain_state = 4
       
    p5.noStroke()
    # draw each item of number_list using a loop:
    for i in range(len(sprite_list)):
        if((i % 2) == 0):
            p5.fill(135, 150, 153)
        else:
            p5.fill(109, 122, 125)
        
        sprite = sprite_list[i]  # get sprite at index i from sprite_list
        sprite.update()
        sprite.draw()
        
def resetProj(proj):
    proj.y = 73
    proj.x = p5.random(20,280)
    
def keyPressed(event):
    global program_state
    
    if (program_state == 'start'):
        program_state = 'play'

    if (program_state =='play'):
        if (p5.key == 'ArrowLeft' and snake.x >= 0 ):
            snake.x -= 10

        if (p5.key == 'ArrowRight' and snake.x <= 250):
            snake.x += 10

    if (program_state == 'pause'):
        program_state = 'play'

def keyReleased(event):
    pass


def mousePressed(event):
    pass


def mouseReleased(event):
    pass
