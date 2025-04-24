import sys
import pygame
import  constants
import numpy as np
import random
import copy
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
          self.level=1
          self.player=2
     def getrand(self,mainboard):
          empty=mainboard.emptySquares()
          if(empty!=[]):
           idx=random.randrange(0,len(empty))
           return empty[idx]
     def minmax(self,mainboard,maximising):
           case=mainboard.checkWin()
           if case==1:
                return 1,None
           elif case==2:
                return -1,None
           else:
                if mainboard.isFull():
                     return 0,None
           if maximising:
               max_eval=-3
               best_move=None
               empty=mainboard.emptySquares()
               for(row,col) in empty:
                    temp=copy.deepcopy(mainboard)
                    temp.mark(row,col,1)
                    eval=self.minmax(temp,False)[0]
                    if(eval>max_eval):
                         max_eval=eval
                         best_move=(row,col)
               
               return max_eval, best_move
           else:
               min_eval=3
               best_move=None
               empty=mainboard.emptySquares()
               for(row,col) in empty:
                    temp=copy.deepcopy(mainboard)
                    temp.mark(row,col,self.player)
                    eval=self.minmax(temp,True)[0]
                    if(eval<min_eval):
                         min_eval=eval
                         best_move=(row,col)
               
               return min_eval, best_move
               
               
           
     def ai(self,board):
          if self.level==0:
               row,col=self.getrand(board)
               return row,col
          else:
         # minmax()
           eval,move=self.minmax(board,False)
           row, col = move
           print(f'the ai has chosen you will  {eval}')
           return row,col
          
               
               
          
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