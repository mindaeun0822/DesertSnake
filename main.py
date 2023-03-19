import js
p5 = js.window


class Snake:
    x = 150
    y = 150

    snake_img = p5.loadImage('snake.png')
    
    def draw(self):
        p5.image(self.snake_img, self.x, self.y)

def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 

snake = Snake()
    
def draw():
    p5.background(255)
    background_img = p5.loadImage('background.png')
    p5.image(background_img,0,0)

    snake.draw()

def keyPressed(event):
    pass 

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass
