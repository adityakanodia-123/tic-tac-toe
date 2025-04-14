import sys
import pygame
import  constants
import numpy as np
import random
pygame.init()
screen=pygame.display.set_mode((constants.WIDTH,constants.HEIGHT))

pygame.display.set_caption("TIC TAC TOE AI")
screen.fill(constants.BG_COLOR)
class Board:
     def __init__(self):
          self.squares=np.zeros((3,3))
          self.markedSq=0
     def checkWin(self):
          #vertical win
          for i in range(3):
               if(self.squares[0][i]==self.squares[1][i]==self.squares[2][i]!=0):
                    return self.squares[0][i]
          #horizontal win 
          for i in range(3):
               if(self.squares[i][0]==self.squares[i][1]==self.squares[i][2]!=0):
                    return self.squares[i][1]
          #diagonal wins
          if(self.squares[0][0]==self.squares[1][1]==self.squares[2][2]!=0):
               return self.squares[0][0]
          if(self.squares[0][2]==self.squares[1][1]==self.squares[2][0]!=0):
                return self.squares[1][1]
          return 0#(nobody won till now(not a check for draw that is different will bw done thru is full function))
     def mark(self,rows,cols,player):
          self.squares[rows][cols]=player
          self.markedSq+=1
     def empty(self,row,col):
          return self.squares[row][col]==0
     def emptySquares(self):
          empty=[]
          for i in range(3):
               for j in range(3):
                    if(self.squares[i][j]==0):
                         empty.append((i,j))
          return empty
               
     def isFull(self):
      return self.markedSq==9
          
class AI:
     def __init__(self):
          self.level=0
          self.player=2
     def getrand(self,mainboard):
          empty=mainboard.emptySquares()
          if(empty!=[]):
           idx=random.randrange(0,len(empty))
           return empty[idx]
     def ai(self,board):
          if self.level==0:
               row,col=self.getrand(board)
               return row,col
          else:
               pass
               
          
class Game:
     def __init__(self):
        self.show_line()  
        self.board=Board()
        self.ai=AI()
        self.player=1
     def show_line(self):
          pygame.draw.line(screen,(0,0,0),(constants.SQ_SIZE,0),(constants.SQ_SIZE,constants.HEIGHT ),4)
          #pygame.display.update()
          pygame.draw.line(screen,(0,0,0),(constants.WIDTH-constants.SQ_SIZE,0),(constants.WIDTH-constants.SQ_SIZE,constants.HEIGHT ),4)
          pygame.draw.line(screen,(0,0,0),(0,constants.SQ_SIZE),(constants.WIDTH,constants.SQ_SIZE ),4)
          pygame.draw.line(screen,(0,0,0),(0,constants.WIDTH-constants.SQ_SIZE),(constants.WIDTH,constants.WIDTH-constants.SQ_SIZE),4)
          
     def changePlayer(self,player):
        self.player=self.player%2 +1
     
     def draw(self,row,col):
          if self.player==1:
            start_dec=(col*constants.SQ_SIZE+50,row*constants.SQ_SIZE+50)
            end_des=(col*constants.SQ_SIZE+constants.SQ_SIZE-50,row*constants.SQ_SIZE+constants.SQ_SIZE-50)
            pygame.draw.line(screen,(0,0,0),start_dec,end_des,10)
            #line 2
            start_dec=(col*constants.SQ_SIZE+50,row*constants.SQ_SIZE+constants.SQ_SIZE-50)
            end_des=(col*constants.SQ_SIZE+constants.SQ_SIZE-50,row*constants.SQ_SIZE+50)
            pygame.draw.line(screen,(0,0,0),start_dec,end_des,10)
               
          elif self.player==2:#circle for 2
              circle=(col*constants.SQ_SIZE+constants.SQ_SIZE//2,row*constants.SQ_SIZE+constants.SQ_SIZE//2)
              pygame.draw.circle(screen,(0,0,0),circle,constants.RADIUS,5)
                  
     
def main():
     
     game=Game()
     board=game.board
     ai=game.ai
     while True:
          

         for event in pygame.event.get():
              
               if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                     row=event.pos[1]//constants.SQ_SIZE
                     col=event.pos[0]//constants.SQ_SIZE
                     if(board.empty(row,col)):
                        board.mark(row,col,game.player)
                        game.draw(row,col)
                        game.changePlayer(game.player)
                        print(board.squares)
                     if game.player==ai.player:
                           pygame.display.update() 
                           row,col=ai.ai(board)
                           board.mark(row,col,game.player)
                           game.draw(row,col)
                           game.changePlayer(game.player)

         pygame.display.update()             
main()                    