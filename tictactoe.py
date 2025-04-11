import sys
import pygame
import  constants
pygame.init()
screen=pygame.display.set_mode((constants.WIDTH,constants.HEIGHT))
pygame.display.set_caption("TIC TAC TOE AI")
screen.fill(constants.BG_COLOR)
class Game:
     def __init__(self):
        self.show_line()  
     
     def show_line(self):
          pygame.draw.line(screen,(0,0,0),(constants.SQ_SIZE,0),(constants.SQ_SIZE,constants.HEIGHT ),4)
          #pygame.display.update()
          pygame.draw.line(screen,(0,0,0),(constants.WIDTH-constants.SQ_SIZE,0),(constants.WIDTH-constants.SQ_SIZE,constants.HEIGHT ),4)
          pygame.draw.line(screen,(0,0,0),(0,constants.SQ_SIZE),(constants.WIDTH,constants.SQ_SIZE ),4)
          pygame.draw.line(screen,(0,0,0),(0,constants.WIDTH-constants.SQ_SIZE),(constants.WIDTH,constants.WIDTH-constants.SQ_SIZE),4)
     
def main():
     
     game=Game()
     while True:
          

         for event in pygame.event.get():
              
               if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

         pygame.display.update()             
main()                    