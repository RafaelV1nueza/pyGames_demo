# pyGames_demo
PyGames pip installed

intro.py 
---------------------------------------------
  Initiate game in class "Game"
  - pg.init()
  Create Screen with RES resolution
  - self.screen = pg.display.set_mode(RES)
  Add clock for animation events and delta time with FPS to unlink animation from fps
  - self.clock = pg.time.Clock()
  - self.delta_time = 1
  - self.delta_time = self.clock.tick(self.FPS)
  Draw elements background, rectangle and player circle
  - self.screen.fill(self.BLUE)
  Develop Run Loop to en after quit or escape
  - def run(self):
            while True:
                self.check_event()
                self.update()
                self.draw()
     def check_event(self):
        ##To exit propperly
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.QUIT
                sys.exit()
    
