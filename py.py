import pygame
import random
from pygame.locals import *
from rect_numbers import check_if_mines
import hollow_grid
pygame.display.init()
pygame.font.init()


grey = (128, 128, 128)
greyer = (220, 220, 220)
darkgrey = (50, 50, 50)
black = (0,0,0)
lgrey = (190,190,190)

x = 0
y = 50
w = 400
h = 360

hollow_index_rect = 1
WIDTH = 105
HEIGHT = 105
game_end = False
xx = 180
yy = 10
rectx = 2
recty = 50
indexnum = 1
rectw = 23
recth = 23
rectDict = {indexnum:{x: 1, y :50}}
mines = {}
crsindex = 1 
clickedrects = {}
indexRect = 1
changedRect = None
rightclickedrects = {}
wind = pygame.display.set_mode(size=(382 ,401))
pygame.display.set_caption("Minesweeper")
TRANSPARENT = pygame.Surface([WIDTH, HEIGHT])

#Game background
class game:
    def __init__(self,x, y, w, h, color):
        self.y = y
        self.x = x
        self.w = w
        self.h = h
        self.color = color
    def gamegrid(self):
        pygame.draw.rect(wind,self.color, [self.x, self.y, self.w, self.h])
       
# Show square if mine or number
class change:
    def __init__(self,rect):
        self.rect = rect
        
    def changecolor(self):
        rectLeft = self.rect.left
        rectTop = self.rect.top
       
        hollows = hollow_grid.check_if_hollow(
        rleft = rectLeft,
        rtop = rectTop,
        mines = mines,
        wind = wind,
        cindex = hollow_index_rect
        )
       
        check_if_mines(
        checkXneg = rectLeft - 21,
        checkXplus = rectLeft + 21,
        checkYneg = rectTop - 22,
        checkYplus = rectTop + 22,
        mines = mines,
        recttop = rectTop,
        rectleft = rectLeft,
        wind = wind,
        hollows = hollows
        )



    def foundmine(self):
        print(self.rect.left)
        pygame.display.update(pygame.draw.rect(wind, Color("blue"),[self.rect.left,self.rect.top,self.rect.width,self.rect.height]))
        pygame.display.update(pygame.draw.rect(wind, darkgrey,[self.rect.left,self.rect.top,self.rect.width,self.rect.height],1))

    def rightclick(self):
        font = pygame.font.Font(None,30)
        num = font.render('1',True,Color('red'))
        pygame.display.update(wind.blit(num,[self.rect.left + 5,self.rect.top]))
        print(self.rect.left + 5,self.rect.top)

    def unrightclick(self):
        font = pygame.font.Font(None,40)
        no = font.render('1',True,Color('Grey'))
        pygame.display.update(wind.blit(no,[self.rect.left + 4,self.rect.top - 2 ]))
        print(self.rect.left + 5,self.rect.top)


#Resets the grid
class reseter:
    def __init__(self,dic):
        self.dic = dic

    def resetgrid(self):
        index = 1
        one = 1
        mines.clear()
        mines.update({5:{'x':86, 'y':50}})
        mines.update({1:{'x':2, 'y':50}})
        # mines.update(random.sample(rectDict.items(), 50))
        
        

        clickedrects.clear()
        rightclickedrects.clear()

        for rectgrid in range(len(self.dic)):
            pygame.display.update(pygame.draw.rect(wind, Color("grey"),[self.dic[index]['x'],self.dic[index]['y'],rectw, recth]))
            pygame.display.update(pygame.draw.rect(wind, darkgrey,[self.dic[index]['x'],self.dic[index]['y'],rectw, recth],1))
            index = index + 1

def counter(count):
    wind.fill(grey, (90,15,30,30))
    font = pygame.font.Font(None,35)
    text = font.render(str(count),True,Color('red'))
    pygame.draw.rect(wind,black,[250,10,65,35])
    pygame.display.update(wind.blit(text,[280,15]))

wind.fill(grey)
grid = game(x, y, w, h, greyer)
grid.gamegrid()





# // Rect squares
reset = pygame.draw.rect(wind,lgrey, [xx, yy, 30, 30])

for re in range(16):
    for rect in range(18):
        pygame.draw.rect(wind, Color("grey"), [rectx, recty, rectw, recth])
        pygame.draw.rect(wind, darkgrey, [rectx, recty, rectw, recth], 1)
        pygame.display.flip()
        rectDict.update({indexnum:{'x':rectx, 'y': recty}})
        indexnum = indexnum + 1
        rectx = rectx + 21

    recty = recty + 22
    rectx = 2
    pygame.draw.rect(wind, Color("grey"), [rectx, recty, rectw, recth])
    pygame.draw.rect(wind, darkgrey, [rectx, recty, rectw, recth],1)
    rectDict.update({indexnum:{'x':rectx, 'y': recty}})
    indexnum = indexnum + 1
    pygame.display.flip()

print(range(len(rectDict)))
clickedRect = pygame.Rect(rectDict[indexRect]['x'],rectDict[indexRect]['y'],rectw, recth)

pygame.display.flip()

mines.update({1:{'x':2, 'y':50}})
mines.update({5:{'x':86, 'y':50}})
# mines.update(random.sample(rectDict.items(), 1))


dictlength = len(clickedrects)


# Game
while not game_end:
    pos = pygame.mouse.get_pos()
    mouse = pygame.draw.circle(TRANSPARENT, (0, 0, 0), pos, 0) 
    counter(dictlength)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            
            if reset.contains(mouse):
                clear = reseter(rectDict)
                clear.resetgrid()
                clickedRect = pygame.Rect(rectDict[indexRect]['x'],rectDict[indexRect]['y'],rectw, recth)
                dictlength = len(clickedrects)
                clickedrects.clear()
                crsindex = 1
                pygame.display.flip()
           
            while clickedRect is not None:
                if clickedRect.contains(mouse) and indexRect in mines and indexRect not in rightclickedrects.keys():
                    print(indexRect)
                    changedRect = clickedRect
                    p1 = change(changedRect)
                    
                    p1.foundmine()
                    indexRect = 1
                    clickedRect = None
                    dictlength = dictlength + 1
                    break
                elif clickedRect.contains(mouse):
                    
                    if indexRect in rectDict.keys() and indexRect not in rightclickedrects.keys() and indexRect not in clickedrects.keys():
                        changedRect = clickedRect
                        p1 = change(changedRect)
                        hollow_index_rect = indexRect
                        print(clickedRect)
                        p1.changecolor()
                        if indexRect not in clickedrects.keys():
                            dictlength += 1
                            clickedrects.update({indexRect: {'x':changedRect.left, 'y': changedRect.top}})
                        break
                    
                    else: 
                        print(dictlength)
                        break
                        
                   
                else: 
                    indexRect += 1
                    if indexRect in rectDict:
                        clickedRect = pygame.Rect(rectDict[indexRect]['x'],rectDict[indexRect]['y'],rectw, recth)
                        
                    else:
                        indexRect = 1
                        clickedRect = pygame.Rect(rectDict[indexRect]['x'],rectDict[indexRect]['y'],rectw, recth)
                        break
                            
        if event.type == MOUSEBUTTONDOWN and event.button == 3:
            while clickedRect is not None:
                if clickedRect.contains(mouse) and indexRect not in clickedrects.keys():
                    changedRect = clickedRect
                    
                    p1 = change(changedRect)
                    p1.rightclick()
                    if indexRect not in rightclickedrects.keys():
                        rightclickedrects.update({indexRect: {'x':changedRect.left, 'y': changedRect.top}})
                        break
                    if indexRect in rightclickedrects.keys():
                        p1.unrightclick()
                     
                        del rightclickedrects[indexRect]
                        
                        
                    break
                else: 
                    indexRect += 1
                    if indexRect in rectDict:
                        clickedRect = pygame.Rect(rectDict[indexRect]['x'],rectDict[indexRect]['y'],rectw, recth)
                    else:
                       indexRect = 1
                       clickedRect = pygame.Rect(rectDict[indexRect]['x'],rectDict[indexRect]['y'],rectw, recth) 
                        
                       break
                    
                    