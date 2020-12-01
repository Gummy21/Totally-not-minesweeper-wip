import pygame
from pygame.locals import *
from rect_numbers import check_if_mines
hollow_rects = {}




def check_if_hollow(rleft,rtop,mines,wind,cindex,dictlen):
    hollow_rects.clear()
    for index in mines:      
        checker(rleft,rtop,mines,cindex,dictlen)
        for rect in hollow_rects.keys():
            pygame.display.update(pygame.draw.rect(wind, (180, 180, 180),[hollow_rects[rect]['x'],hollow_rects[rect]['y'],23,23]))
            pygame.display.update(pygame.draw.rect(wind, [50,50,50],[hollow_rects[rect]['x'],hollow_rects[rect]['y'],23,23],1))
            recttop = hollow_rects[rect]['y'] 
            rectleft = hollow_rects[rect]['x']
            if (check_if_mines(
            checkXneg = rectleft - 21,
            checkXplus = rectleft + 21,
            checkYneg = recttop - 22,
            checkYplus = recttop + 22,
            mines = mines,
            recttop = recttop,
            rectleft = rectleft,
            wind = wind,
            )):
                pass
            
           
       
        hollows = hollow_rects
        
      
        return hollows
        break
            
        
        



def checker(rleft,rtop,mines,cindex,dictlen):
   if bot_right(rleft,rtop,mines,cindex,dictlen):
       pass
   if top_left(rleft,rtop,mines,cindex,dictlen):
       pass
   if top(rleft,rtop,mines,cindex,dictlen):
      pass
   if top_right(rleft,rtop,mines,cindex,dictlen):
       pass
   if mid_left(rleft,rtop,mines,cindex,dictlen):
      pass
   if mid(rleft,rtop,mines,cindex,dictlen):
       pass
   if mid_right(rleft,rtop,mines,cindex,dictlen):
      pass
   if bot_left(rleft,rtop,mines,cindex,dictlen):
       pass
   if bot(rleft,rtop,mines,cindex,dictlen):
      pass
   
   pass
    

def top_left(rleft,rtop,mines,cindex,dictlen):
   for num in range(dictlen):
      rleftp = rleft - 21
      rtopp = rtop - 22
      cindex = cindex - 20
      if (rleftp not in mines.values()
         and rtopp not in mines.values()):
         rleftpp = rleftp - 21
         rtoppp = rtopp - 22
         hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})
         if (rleftpp in mines.values()
            and rtoppp in mines.values()):
            hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})
            return 
         else:
            return
      else:
         hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})
         return

def top_right(rleft,rtop,mines,cindex,dictlen):
   for num in range(dictlen):
      rleftp = rleft + 21
      rtopp = rtop - 22
      cindex = cindex + 1
      cindex = cindex - 19
      if (rleftp not in mines.values()
         and rtopp not in mines.values()):
         rleftpp = rleftp + 21
         rtoppp = rtopp - 22
         hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})
         if (rleftpp in mines.values()
            and rtoppp in mines.values()):
            hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})
            return 
         else:
            return
      else:
         hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})
         return

def top(rleft,rtop,mines,cindex,dictlen):
    for num in range(dictlen):
      rtopp = rtop - 22
      cindex = cindex - 19
      if (rleft not in mines.values()
         and rtopp not in mines.values()):
         hollow_rects.update({cindex: {'x':rleft,'y':rtopp}})
         rtoppp = rtopp - 22
         if (rleft in mines.values()
            and rtoppp in mines.values()):
            hollow_rects.update({cindex: {'x':rleft,'y':rtopp}})
            return
         else:
            return
      else:
         hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})
         return
      


def mid_left(rleft,rtop,mines,cindex,dictlen):
   for num in range(dictlen):
      rleftp = rleft - 21
      cindex = cindex - 1
      if (rleftp not in mines.values()
         and rtop not in mines.values()):
         rleftpp = rleftp - 21
         hollow_rects.update({cindex: {'x':rleftp,'y':rtop}})
         if (rleftpp in mines.values()
            and rtop in mines.values()):
            hollow_rects.update({cindex: {'x':rleftp,'y':rtop}})
            return 
         else:
            return
      else:
         hollow_rects.update({cindex: {'x':rleftp,'y':rtop}})
         return
      
def mid(rleft,rtop,mines,cindex,dictlen):
   if (rleft not in mines.values()
      and rtop not in mines.values()):
         hollow_rects.update({cindex: {'x':rleft,'y':rtop}})
         return 


def mid_right(rleft,rtop,mines,cindex,dictlen):
   for num in range(dictlen):
      rleftp = rleft + 21
      cindex = cindex + 1
      if (rleftp not in mines.values()
         and rtop not in mines.values()):
         rleftpp = rleftp + 21
         hollow_rects.update({cindex: {'x':rleftp,'y':rtop}})
         if (rleftpp in mines.values()
            and rtop in mines.values()):
            hollow_rects.update({cindex: {'x':rleftp,'y':rtop}})
            return 
         else:
            return
      else:
         hollow_rects.update({cindex: {'x':rleftp,'y':rtop}})
         return
      


def bot_left(rleft,rtop,mines,cindex,dictlen):
   for num in range(dictlen):
      rleftp = rleft - 21
      rtopp = rtop + 22
      cindex = cindex - 1
      cindex = cindex + 19
      if (rleftp not in mines.values()
         and rtopp not in mines.values()):
         rleftpp = rleftp - 21
         rtoppp = rtopp + 22
         hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})

         if (rleftpp in mines.values()
            and rtoppp in mines.values()):
            hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})
            return 
         else:
            return
      else:
         hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})
         return
      

def bot(rleft,rtop,mines,cindex,dictlen):
   for num in range(dictlen):
      
      rtopp = rtop + 22
      cindex = cindex + 19
      if (rleft not in mines.values()
         and rtopp not in mines.values()):

         rtoppp = rtopp + 22
         hollow_rects.update({cindex: {'x':rleft,'y':rtopp}})

         if (rleft in mines.values()
            and rtoppp in mines.values()):
            hollow_rects.update({cindex: {'x':rleft,'y':rtopp}})
            return 
         else:
            return
      else:
         hollow_rects.update({cindex: {'x':rleft,'y':rtopp}})
         return
      

def bot_right(rleft,rtop,mines,cindex,dictlen):
   for num in range(dictlen):
      rleftp = rleft + 21
      rtopp = rtop + 22
      cindex = cindex + 20
      if (rleftp not in mines.values()
         and rtopp not in mines.values()):
         rleftpp = rleftp + 21
         rtoppp = rtopp + 22
         hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})
         if (rleftpp in mines.values()
            and rtoppp in mines.values()):
            hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})
            return 
         else:
            return
      else:
         hollow_rects.update({cindex: {'x':rleftp,'y':rtopp}})
         return
      



      
            
       
    
    
