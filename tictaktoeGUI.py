import pygame
import os

computer=False
game_still_going=False
current_player='X'
mode=False
winner=None
draw=True
hardness=10 # set to 1 for easy  and maxmimum can set to 10
match_win=[[0,(10,80),(300,80)],
           [0,(10,180),(300,180)],
           [0,(10,280),(300,280)],
           [0,(55,45),(55,325)],
           [0,(155,45),(155,325)],
           [0,(255,45),(255,325)],
           [0,(20,45),(293,318)],
           [0,(288,48),(22,312)],]
           
board=board=["_","_","_",
           "_","_","_",
           "_","_","_"]

pygame.init()
pygame.display.set_caption("tic-tac-toe")
win = pygame.display.set_mode((320,400))
font = pygame.font.SysFont('comicsans', 30)
clock = pygame.time.Clock()

try:
  X=pygame.transform.scale(pygame.image.load(os.getcwd()+"\\"+os.path.join("imgs","cross1.png")).convert_alpha(),(60,60))
  O=pygame.transform.scale(pygame.image.load(os.getcwd()+"\\"+os.path.join("imgs","circle.png")).convert_alpha(),(60,60))
  ch=pygame.transform.scale(pygame.image.load(os.getcwd()+"\\"+os.path.join("imgs","arrow.png")).convert_alpha(),(30,30))
except Exception:
  print("File not found")

def draw_board():
    gap=100
    pygame.draw.rect(win,(255,255,255),(0,0,320,400))
    
    for i in range(1,3):#board lines
        pygame.draw.line(win,(0,0,0),(10,i*gap+30),(3*gap,i*gap+30),2)
        pygame.draw.line(win,(0,0,0),(i*gap,40),(i*gap,3*gap+30),2)
    
    win.blit(ch,(280,5))
    
    # win.blit(X,(200,200))

    I=0
    line_no=0
    for i,val in enumerate(board):#the x and o
        
        
        if val!="_":
            if val=="X":
                win.blit(X,((I*gap) +25,(line_no*gap)+50))
            
            else:
                win.blit(O,((I*gap) +25,(line_no*gap)+50))
            # print((I,line_no))

        I+=1
        if (i+1)%3==0:
            I=0
            line_no+=1
        
    if winner:#prints who is the winner
        # print(winner)
        if winner!="_":
          if mode and winner=="O":
            win.blit(font.render("You Won !!!!!",1, (255,0,0)), (10, 5))
          else:
            win.blit(font.render(winner+" Won !!!!!",1, (255,0,0)), (10, 5))
         
        else:

            win.blit(font.render("It's is Tie",3, (255,0,0)), (10, 5))

    else:#prints the whose turn is it
      if mode and current_player=="O":
        win.blit(font.render("It's  your move ", 1, (0,0,0)), (10, 5)) #moving player
      else:
        win.blit(font.render("It's  "+ current_player+"'s move ", 1, (0,0,0)), (10, 5))

    #buttons.....
    if mode:
      if computer:
        pygame.draw.rect(win, (0,205,0), (20,350, 120, 40))
      else:
        pygame.draw.rect(win, (205,0,0), (20,350, 120, 40))
      pygame.draw.rect(win, (102,205,205), (160,350, 120, 40))
    else:
      pygame.draw.rect(win, (102,205,205), (20,350, 120, 40))
      pygame.draw.rect(win, (205,0,0), (160,350, 120, 40))

    pygame.draw.rect(win, (0,0,0), (20,350, 120, 40), 1)
    win.blit(font.render('Computer', 1, (0,0,0)), (30, 360))

    
    pygame.draw.rect(win, (0,0,0), (160,350, 120, 40), 1)
    win.blit(font.render('Friend', 1, (0,0,0)), (190, 360))

    for val in  match_win:
      if val[0]==1:
        # print (val)
        pygame.draw.line(win,(0,0,0),val[1],val[2],5)

def handle_turn(player,pos):
    
    if computer and player=="computer":
        board[computer_plays()]="X"
        return True
    
    x=(pos[0]-10)//100
    y=(pos[1]-40)//100
    
    if board[y*3+x]=="_":
      board[y*3+x]=player
      return True
    
    return False

def flip_player():
  global current_player
  if  current_player=='X' or current_player=="computer" :
    current_player='O'
  elif computer:
    current_player="computer"
  else:
    current_player='X'

def check_if_game_over(bo):
  if check_if_win(bo):
      return True
  elif check_if_tie(bo):
      return True
  
  return False

def check_if_win(bo):

  if check_row(bo):
    return  True
  elif check_colums(bo):
    return True
  elif check_diagonal(bo):
    return True

  return False

def check_row(board):
  global winner
  row_1=board[0]==board[1]==board[2] !='_'
  row_2=board[3]==board[4]==board[5] !='_'
  row_3=board[6]==board[7]==board[8] !='_'  
  if row_1 or row_2 or row_3:
    
    if row_1:
      winner=board[0]
      if draw:
        match_win[0][0]=1

    if row_2:
      winner=board[3]

      if draw:
        match_win[1][0]=1
    if row_3:
      winner=board[6]
      if draw:
        match_win[2][0]=1

    return True
  return False
  
def check_diagonal(bo):
  global winner
  dia_1=bo[0]==bo[4]==bo[8] !='_'
  dia_2=bo[2]==bo[4]==bo[6] !='_'

  if dia_1 or dia_2 :
    
    if dia_1:
      winner=bo[0]
      if draw:
        match_win[6][0]=1

    if dia_2:
      winner=bo[2]
      if draw:
        match_win[7][0]=1

    
    return True
  return False
    
def check_colums(board):
  global winner
  col_1=board[0]==board[3]==board[6] !='_'
  col_2=board[1]==board[4]==board[7] !='_'
  col_3=board[2]==board[5]==board[8] !='_'  
  if col_1 or col_2 or col_3:
    
    if col_1:
      winner=board[0]
      if draw:
        match_win[3][0]=1

    if col_2:
      winner=board[1]
      if draw:
        match_win[4][0]=1
    if col_3:
      winner=board[2]
      if draw:
        match_win[5][0]=1

    return True
  return False

def check_if_tie(board):
  global winner
  
  count=0
  for i in board:
    if i=='_':
      count=count+1
  
  if count==0:
    winner="_"
    
    
    return True
  return False

def min_max(bo,turn,dept):
  result=0
  max=(-10,None)
  min=(+10,None)
  
  if check_if_game_over(bo.copy()):
    
    if winner=="X":
      return 1
    elif winner=="O":
      return -1  
    else:
      return 0
  
      
  for i,val in enumerate(bo):
    

    if val=="_":
      if turn:
        bo[i]="X"
      else:
        bo[i]="O"

      if dept+1<=hardness:
        result=min_max(bo.copy(), not turn , dept+1)
      bo[i]="_"

      if turn:
        if result>max[0]:
          max=(result,i)
          if max[0]==1:
            break
          
      else:
        if result<min[0]:
          min=(result,i)
          if min[0]==-1:
            break
          
  if turn:
    if dept!=0:
      return max[0]
    else:
      return max[1]
               
  else:
    if dept!=0:
      return min[0]
    else:
      return min[1]
  
def computer_plays():
    global winner,draw
    draw=False
    pos=min_max(board.copy(),True,dept=0)
    draw=True
    winner=None
    

    if  board[pos]=="_":
      return pos
     
def main():
    global computer,game_still_going,board,current_player,winner,mode

    font = pygame.font.SysFont('comicsans', 30)

    run=True

    while run:
        clock.tick(30)
        draw_board()
        key_pos=None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()

                if pos[0]>20 and pos[0]<140 and pos[1]>350  and pos[1]<390 and not game_still_going and not winner:
                      
                    if current_player=="X":
                      current_player="computer"
                      
                    if mode:
                      computer=True
                      game_still_going=True
                    else:
                      mode=True
            
                if pos[0]>160 and pos[0]<280 and pos[1]>350 and pos[1]<390 and not game_still_going and not winner:
                    # print("friend")
                    current_player="X"
                    computer=False
                    mode=False
                
                if pos[0]>=10 and pos[0]<=300 and pos[1]>=40 and pos[1]<=330 and not winner and  (computer or not mode):
                    
                    game_still_going=True
                    key_pos=pos
                
                if pos[0]>=280 and pos[0]<=310 and pos[1]>=7 and pos[1]<=36 and not game_still_going and not winner:
                  # print("change palyer")
                  
                  if current_player=="O":
                    if mode:
                      current_player="coumputer"
                    else:
                      current_player="X"
                  else:
                    current_player="O"
                    
            if event.type == pygame.KEYDOWN and not game_still_going :
                if event.key == pygame.K_DELETE:
                    # print("reset")
                    for i,var in enumerate(board):
                      board[i]="_"
                    
                    current_player="X"
                    winner=None
                    computer=False
                    mode=False
                    for val in match_win:
                      val[0]=0

        if game_still_going:
            
            if key_pos or (computer and current_player=="computer"):
                # print(current_player)

                if handle_turn(current_player,key_pos):
                    
                    game_still_going= not check_if_game_over(board)
                    # print(game_still_going)
                    
                    flip_player()

        pygame.display.update()

if __name__=='__main__':
  main()

pygame.quit()