import pygame

from pygame.locals import *

class Text:
    
    def __init__(self):
        self.text = "For a couple of years Maxwell Salmon has been working on a game and making a raycaster engine."

    def update_text_position(self):
        pass
    
    def view_text_surface(self):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(self.text, False, (100, 100, 100))
        return textsurface

class App:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 640

        self.text_class = Text()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self._display_surf.blit(self.text_class.view_text_surface(),(0,0))
        pygame.display.flip()


 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()