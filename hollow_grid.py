import pygame
from pygame.locals import *

hollow_rects = {}




def check_if_hollow(rleft,rtop,mines,wind,cindex):
    for index in mines.keys():
        if (
        check_if_hollowxp(rleft,rtop,mines,index,cindex)
        or
        check_if_hollowxm(rleft,rtop,mines,index,cindex)
        ):
            for rect in hollow_rects.keys():

                pygame.display.update(pygame.draw.rect(wind, (180, 180, 180),[hollow_rects[rect]['x'],hollow_rects[rect]['y'],23,23]))
                pygame.display.update(pygame.draw.rect(wind, [50,50,50],[hollow_rects[rect]['x'],hollow_rects[rect]['y'],23,23],1))
            break
        else:
            break
        



def check_if_hollowxp(rleft,rtop,mines,index,cindex):
    for num in range(18):
        if (
            rleft in mines[index].values()
            and rtop in mines[index].values()
        ):
            print(rleft,rtop)
            return True
            break
        elif (rleft > 359):
            rtop += 22
            rleft = 2
        else:
            
            hollow_rects.update({cindex: {'x':rleft,'y':rtop}})
            cindex += 1
            rleft += 21


def check_if_hollowxm(rleft,rtop,mines,index,cindex):
    for num in range(18):
        if (
            rleft in mines[index].values()
            and rtop in mines[index].values()
        ):
            print(rleft,rtop)
            return True
            break
        elif (rleft < 2):
            if rtop == 22:
                rtop = 22
            else:
                rtop -= 22
            rleft = 2
        else:
            hollow_rects.update({cindex: {'x':rleft,'y':rtop}})
            cindex -= 1
            rleft -= 21