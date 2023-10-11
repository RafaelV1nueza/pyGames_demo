import pygame as pg
import sys

class Player:
    def __init__(self,game):
          self.game = game
          self.px,self.py = self.game.PLAYER_POS
          self.ground = (self.game.HEIGHT*2//3 - 10)

    def movement(self):
        dx = 0
        dy = 0
        speed = self.game.PLAYER_SPEED * self.game.delta_time

        #WASD Movement
        keys = pg.key.get_pressed()
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            dx -= speed
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            dx += speed
        if keys[pg.K_w] or keys[pg.K_UP]:
            dy -= speed
        dy += self.game.GRAVITY

        self.collision(dx,dy)

    def collision(self,dx,dy):
        scale = self.game.PLAYER_SIZE / self.game.delta_time
        #para X
        if 0 < (self.px + dx * scale) < self.game.WIDTH:
            self.px += dx
        elif self.px < 0:
            self.px = 0 + self.game.PLAYER_SIZE
        elif self.px > self.game.WIDTH:
            self.px = self.game.WIDTH - self.game.PLAYER_SIZE
        #Para Y
        if (self.py + dy * scale) < self.ground:
            self.py += dy
        else:
            self.py = self.ground
        


    def draw(self):
        pg.draw.circle(self.game.screen,self.game.WHITE,(self.px,self.py),
                        self.game.PLAYER_SIZE,5)
        
    def update(self):
        self.movement()

    @property 
    def pos(self):
        return self.px

class Game:
    def __init__(self):
          
        pg.init()
          
        #GAME SETTINGS
        self.WIDTH, self.HEIGHT = RES = (1200,800)
        self.HALF_HEIGHT = self.HEIGHT //2
        self.HALF_WIDTH = self.WIDTH //2
        self.FPS = 60
        #Player Settings
        self.ox, self.oy = self.PLAYER_POS = self.HALF_WIDTH, (self.HEIGHT*2//3 - 10)
        self.PLAYER_SPEED = 1.5
        self.PLAYER_SIZE = 10
        self.GRAVITY = 10
        

        #COLORS
        self.BLACK   = (  0,   0,   0)
        self.WHITE   = (255, 255, 255)
        self.BLUE    = ( 51, 153, 255)
        self.GRAY    = ( 34,  34,  34)
        self.GREEN   = (  0, 102,   0)
        self.DIRT    = ( 77,  38,   0)
        self.WET_DIRT= ( 45,  28,   0)

        pg.mouse.set_visible(True)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()      
        self.delta_time = 1 
        self.new_game()

    def new_game(self):
        self.player = Player(self)

    def check_event(self):
        ##To exit propperly
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.QUIT
                sys.exit()
    
    def update(self):
        self.player.update()
        pg.display.flip()     #Update display
        self.delta_time = self.clock.tick(self.FPS)

    def draw(self):
        self.screen.fill(self.BLUE)
        pg.draw.rect(self.screen,self.DIRT,(0,(2*self.HEIGHT//3),self.WIDTH,self.HEIGHT//3))
        pg.draw.rect(self.screen,self.WET_DIRT,(0,(2*self.HEIGHT//3),self.WIDTH,self.HEIGHT//12))
        pg.draw.rect(self.screen,self.GREEN,(0,(2*self.HEIGHT//3),self.WIDTH,self.HEIGHT//30))

        self.player.draw()

    def run(self):
            while True:
                self.check_event()
                self.update()
                self.draw()
            


if __name__ == '__main__':
     game = Game()
     game.run()

