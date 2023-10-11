import pygame as pg
import sys
import math

class Player:
    def __init__(self,game):
          self.game = game
          self.px,self.py = self.game.PLAYER_POS
          self.ground = (self.game.floor)
          self.gravity = self.game.GRAVITY
          self.dy_a = 0 #for gravity

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
        #Gravity logic without any tutorial wuuuuuuuuu
        #WOrks well dont touch
        dy += self.gravity
        if self.py < (self.ground - self.game.PLAYER_SIZE) and self.dy_a >= 0:
            t_a = math.sqrt(2*self.dy_a/self.gravity)
            dy = 0.5*self.gravity*(t_a+1)**2
        self.dy_a = dy
        ##
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
        if (self.py + dy * scale) < self.ground - self.game.PLAYER_SIZE:
            self.py += dy
        else:
            self.py = self.ground - self.game.PLAYER_SIZE
        


    def draw(self):
        pg.draw.circle(self.game.screen,self.game.WHITE,(self.px,self.py),
                        self.game.PLAYER_SIZE,5)
        
    def update(self):
        self.movement()

    @property 
    def pos(self):
        return self.px

class Points:
    def __init__(self,game):
        self.game = game
        self.ground = (self.game.HEIGHT*2//3 - 10)


class Game:
    def __init__(self):
          
        pg.init()
          
        #GAME SETTINGS
        self.WIDTH, self.HEIGHT = RES = (1200,800)
        self.HALF_HEIGHT = self.HEIGHT //2
        self.HALF_WIDTH = self.WIDTH //2
        self.FPS = 60
        self.floor = self.HEIGHT*4//5 - 10
        #Player Settings
        self.PLAYER_SIZE = 10
        self.ox, self.oy = self.PLAYER_POS = self.HALF_WIDTH, self.floor - self.PLAYER_SIZE
        self.PLAYER_SPEED = 1.5
        self.GRAVITY = 0.98 /40
        

        #COLORS
        self.WHITE   = (255, 255, 255)
        self.BLUE    = ( 51, 153, 255)
        self.GREEN   = (  0, 102,   0)
        self.DIRT    = ( 77,  38,   0)
        self.WET_DIRT= ( 45,  28,   0)

        self.GREEN_1   = (  0, 130,   0)
        self.DIRT_1    = (156,  73,   0)
        self.WET_DIRT_1= (102,  51,   0)

        self.GREEN_2   = ( 17, 154,  17)
        self.DIRT_2    = (156,  73,  17)
        self.WET_DIRT_2= (102,  68,  34)


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
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def land_create(self,corner_1,corner_2,shade):
        a,b = corner_1
        c = corner_2
        if shade:
            pg.draw.rect(self.screen,self.DIRT_1,(a,b,c,(self.floor-b)))
            pg.draw.rect(self.screen,self.WET_DIRT_1,(a,b,c,(self.floor-b) // 4))
            pg.draw.rect(self.screen,self.GREEN_1,(a,b,c,(self.floor-b) // 10))
        else:
            pg.draw.rect(self.screen,self.DIRT_2,(a,b,c,(self.floor-b)))
            pg.draw.rect(self.screen,self.WET_DIRT_2,(a,b,c,(self.floor-b) // 4))
            pg.draw.rect(self.screen,self.GREEN_2,(a,b,c,(self.floor-b) // 10))

    def draw(self):
        #background
        self.screen.fill(self.BLUE)
        self.land_create((self.WIDTH*0.8,(2* self.HEIGHT//9)),self.HALF_WIDTH*2//3,1)
        self.land_create((0,(4 * self.HEIGHT//9)),self.HALF_WIDTH*2//3,0)
        self.land_create((self.WIDTH*2//3,(6 * self.HEIGHT//9)),(self.WIDTH//5),1)

        #foreground
        a,b,c,d =  (0,(self.floor),self.WIDTH,self.HEIGHT//3)
        pg.draw.rect(self.screen,self.DIRT,(a,b,c,d))
        pg.draw.rect(self.screen,self.WET_DIRT,(a,b,c,d // 4))
        pg.draw.rect(self.screen,self.GREEN,(a,b,c,d // 10))
        
        self.player.draw()

    def run(self):
            while True:
                self.check_event()
                self.update()
                self.draw()
            
if __name__ == '__main__':
     game = Game()
     game.run()

