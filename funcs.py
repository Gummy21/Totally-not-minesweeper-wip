import pygame
import itertools
from pygame.locals import *

def eight(xneg,xplus,yneg,yplus,btop,bleft,mined,indexnum1,wind):
    xneg3 = xneg
    yneg2 = yneg
    yneg3 = yneg
    xplus3 = xplus
    yplus2 = yplus
    yplus3 = yplus
    rect_list1 = list(itertools.combinations([xneg,xplus,yplus,yneg,bleft,btop],2))
    
    for combo in rect_list1:
                    
        if (                        
        combo[0] in mined[indexnum1].values()
        and combo[1] in mined[indexnum1].values()                 
        ):
            rect_list1.remove(combo)
            for indexnum2 in mined.keys():
                for combo2 in rect_list1:
                            
                    if(
                    combo2[0] in mined[indexnum2].values()
                    and combo2[1] in mined[indexnum2].values() 
                    ):
                                
                        rect_list1.remove(combo2)
                        for indexnum3 in mined.keys():
                            for combo3 in rect_list1:
                                    
                                if(
                                combo3[0] in mined[indexnum3].values()
                                and combo3[1] in mined[indexnum3].values() 
                                ):
                                    rect_list1.remove(combo3)
                                    for indexnum4 in mined.keys():
                                        for combo4 in rect_list1:
                                    
                                            if(
                                            combo4[0] in mined[indexnum4].values()
                                            and combo4[1] in mined[indexnum4].values() 
                                            ):
                                                rect_list1.remove(combo4)
                                                for indexnum5 in mined.keys():
                                                    for combo5 in rect_list1:

                                                        if(
                                                        combo5[0] in mined[indexnum5].values()
                                                        and combo5[1] in mined[indexnum5].values() 
                                                        ):
                                                            rect_list1.remove(combo5)
                                                            for indexnum6 in mined.keys():
                                                                for combo6 in rect_list1:

                                                                    if(
                                                                        combo6[0] in mined[indexnum6].values()
                                                                        and combo6[1] in mined[indexnum6].values() 
                                                                        ):
                                                                            rect_list1.remove(combo6)
                                                                            for indexnum7 in mined.keys():
                                                                                for combo7 in rect_list1:

                                                                                    if(
                                                                                        combo7[0] in mined[indexnum7].values()
                                                                                        and combo7[1] in mined[indexnum7].values() 
                                                                                        ):
                                                                                            rect_list1.remove(combo7)
                                                                                            for indexnum8 in mined.keys():
                                                                                                for combo8 in rect_list1:

                                                                                                    if(
                                                                                                        combo8[0] in mined[indexnum8].values()
                                                                                                        and combo8[1] in mined[indexnum8].values() 
                                                                                                        ):               
                                                                                                            font = pygame.font.Font(None,30)
                                                                                                            num = font.render('8',True,Color('Blue'))
                                                                                                            pygame.display.update(wind.blit(num,[bleft + 5,btop]))
                                                                                                            return True
                                                                                                            break                
                                                                            
                

def seven(xneg,xplus,yneg,yplus,btop,bleft,mined,indexnum1,wind):
    xneg3 = xneg
    yneg2 = yneg
    yneg3 = yneg
    xplus3 = xplus
    yplus2 = yplus
    yplus3 = yplus
    rect_list1 = list(itertools.combinations([xneg,xplus,yplus,yneg,bleft,btop],2))
    
    for combo in rect_list1:
           
        if (                        
        combo[0] in mined[indexnum1].values()
        and combo[1] in mined[indexnum1].values()                 
        ):
            rect_list1.remove(combo)
            for indexnum2 in mined.keys():
                for combo2 in rect_list1:
                     
                    if(
                    combo2[0] in mined[indexnum2].values()
                    and combo2[1] in mined[indexnum2].values() 
                    ):
                                
                        rect_list1.remove(combo2)
                        for indexnum3 in mined.keys():
                            for combo3 in rect_list1:
                              
                                if(
                                combo3[0] in mined[indexnum3].values()
                                and combo3[1] in mined[indexnum3].values() 
                                ):
                                    rect_list1.remove(combo3)
                                    for indexnum4 in mined.keys():
                                        for combo4 in rect_list1:
                                            
                                            if(
                                            combo4[0] in mined[indexnum4].values()
                                            and combo4[1] in mined[indexnum4].values() 
                                            ):
                                                rect_list1.remove(combo4)
                                                for indexnum5 in mined.keys():
                                                    for combo5 in rect_list1:
                                                        
                                                        if(
                                                        combo5[0] in mined[indexnum5].values()
                                                        and combo5[1] in mined[indexnum5].values() 
                                                        ):
                                                            rect_list1.remove(combo5)
                                                            for indexnum6 in mined.keys():
                                                                for combo6 in rect_list1:
                                                                    
                                                                    if(
                                                                        combo6[0] in mined[indexnum6].values()
                                                                        and combo6[1] in mined[indexnum6].values() 
                                                                        ):
                                                                            rect_list1.remove(combo6)
                                                                            for indexnum7 in mined.keys():
                                                                                for combo7 in rect_list1:
                                                                                    
                                                                                    if(
                                                                                        combo7[0] in mined[indexnum7].values()
                                                                                        and combo7[1] in mined[indexnum7].values() 
                                                                                        ):             
                                                                                            font = pygame.font.Font(None,30)
                                                                                            num = font.render('7',True,Color('Blue'))
                                                                                            pygame.display.update(wind.blit(num,[bleft + 5,btop]))
                                                                                            return True
                                                                                            break                
                                                                                         
                                                                      
                                                

def six(xneg,xplus,yneg,yplus,btop,bleft,mined,indexnum1,wind):
    xneg3 = xneg
    yneg2 = yneg
    yneg3 = yneg
    xplus3 = xplus
    yplus2 = yplus
    yplus3 = yplus
    rect_list1 = list(itertools.combinations([xneg,xplus,yplus,yneg,bleft,btop],2))
    
    for combo in rect_list1:
                    
        if (                        
        combo[0] in mined[indexnum1].values()
        and combo[1] in mined[indexnum1].values()                 
        ):
            rect_list1.remove(combo)
            for indexnum2 in mined.keys():
                for combo2 in rect_list1:
                            
                    if(
                    combo2[0] in mined[indexnum2].values()
                    and combo2[1] in mined[indexnum2].values() 
                    ):
                                
                        rect_list1.remove(combo2)
                        for indexnum3 in mined.keys():
                            for combo3 in rect_list1:
                                    
                                if(
                                combo3[0] in mined[indexnum3].values()
                                and combo3[1] in mined[indexnum3].values() 
                                ):
                                    rect_list1.remove(combo3)
                                    for indexnum4 in mined.keys():
                                        for combo4 in rect_list1:
                                    
                                            if(
                                            combo4[0] in mined[indexnum4].values()
                                            and combo4[1] in mined[indexnum4].values() 
                                            ):
                                                rect_list1.remove(combo4)
                                                for indexnum5 in mined.keys():
                                                    for combo5 in rect_list1:
                                    
                                                     if(
                                                        combo5[0] in mined[indexnum5].values()
                                                         and combo5[1] in mined[indexnum5].values() 
                                                         ):
                                                            rect_list1.remove(combo5)
                                                            for indexnum6 in mined.keys():
                                                                for combo6 in rect_list1:

                                                                    if(
                                                                        combo6[0] in mined[indexnum6].values()
                                                                        and combo6[1] in mined[indexnum6].values() ):             
                                                                            font = pygame.font.Font(None,30)
                                                                            num = font.render('6',True,Color('Blue'))
                                                                            pygame.display.update(wind.blit(num,[bleft + 5,btop]))
                                                                            return True
                                                                            break       
                                

def five(xneg,xplus,yneg,yplus,btop,bleft,mined,indexnum1,wind):
    xneg3 = xneg
    yneg2 = yneg
    yneg3 = yneg
    xplus3 = xplus
    yplus2 = yplus
    yplus3 = yplus
    rect_list1 = list(itertools.combinations([xneg,xplus,yplus,yneg,bleft,btop],2))
    
    for combo in rect_list1:
                    
        if (                        
        combo[0] in mined[indexnum1].values()
        and combo[1] in mined[indexnum1].values()                 
        ):
            rect_list1.remove(combo)
            for indexnum2 in mined.keys():
                for combo2 in rect_list1:
                            
                    if(
                    combo2[0] in mined[indexnum2].values()
                    and combo2[1] in mined[indexnum2].values() 
                    ):
                                
                        rect_list1.remove(combo2)
                        for indexnum3 in mined.keys():
                            for combo3 in rect_list1:
                                    
                                if(
                                combo3[0] in mined[indexnum3].values()
                                and combo3[1] in mined[indexnum3].values() 
                                ):
                                    rect_list1.remove(combo3)
                                    for indexnum4 in mined.keys():
                                        for combo4 in rect_list1:
                                    
                                            if(
                                            combo4[0] in mined[indexnum4].values()
                                            and combo4[1] in mined[indexnum4].values() 
                                            ):
                                                rect_list1.remove(combo4)
                                                for indexnum5 in mined.keys():
                                                    for combo5 in rect_list1:
                                    
                                                     if(
                                                        combo5[0] in mined[indexnum5].values()
                                                         and combo5[1] in mined[indexnum5].values() ):            
                                                            
                                                            font = pygame.font.Font(None,30)
                                                            num = font.render('5',True,Color('Blue'))
                                                            pygame.display.update(wind.blit(num,[bleft + 5,btop]))
                                                            return True
                                                            break            
                                              

def four(xneg,xplus,yneg,yplus,btop,bleft,mined,indexnum1,wind):
    xneg3 = xneg
    yneg2 = yneg
    yneg3 = yneg
    xplus3 = xplus
    yplus2 = yplus
    yplus3 = yplus
    rect_list1 = list(itertools.combinations([xneg,xplus,yplus,yneg,bleft,btop],2))
    
    for combo in rect_list1:
                    
        if (                        
        combo[0] in mined[indexnum1].values()
        and combo[1] in mined[indexnum1].values()                 
        ):
            rect_list1.remove(combo)
            for indexnum2 in mined.keys():
                for combo2 in rect_list1:
                            
                    if(
                    combo2[0] in mined[indexnum2].values()
                    and combo2[1] in mined[indexnum2].values() 
                    ):
                                
                        rect_list1.remove(combo2)
                        for indexnum3 in mined.keys():
                            for combo3 in rect_list1:
                                    
                                if(
                                combo3[0] in mined[indexnum3].values()
                                and combo3[1] in mined[indexnum3].values() 
                                ):
                                    rect_list1.remove(combo3)
                                    for indexnum4 in mined.keys():
                                        for combo4 in rect_list1:
                                    
                                            if(
                                            combo4[0] in mined[indexnum4].values()
                                            and combo4[1] in mined[indexnum4].values() 
                                            ):            
                                                
                                                font = pygame.font.Font(None,30)
                                                num = font.render('4',True,Color('Blue'))
                                                pygame.display.update(wind.blit(num,[bleft + 5,btop]))
                                                return True
                                                break
                

def three(xneg,xplus,yneg,yplus,btop,bleft,mined,indexnum1,wind):
    xneg3 = xneg
    yneg2 = yneg
    yneg3 = yneg
    xplus3 = xplus
    yplus2 = yplus
    yplus3 = yplus
    rect_list1 = list(itertools.combinations([xneg,xplus,yplus,yneg,bleft,btop],2))
    
    for combo in rect_list1:
                    
        if (                        
        combo[0] in mined[indexnum1].values()
        and combo[1] in mined[indexnum1].values()                 
        ):
            rect_list1.remove(combo)
            for indexnum2 in mined.keys():
                for combo2 in rect_list1:
                            
                    if(
                    combo2[0] in mined[indexnum2].values()
                    and combo2[1] in mined[indexnum2].values() 
                    ):
                                
                        rect_list1.remove(combo2)
                        for indexnum3 in mined.keys():
                            for combo3 in rect_list1:
                                    
                                if(
                                combo3[0] in mined[indexnum3].values()
                                and combo3[1] in mined[indexnum3].values() 
                                ):       
                                    
                                    font = pygame.font.Font(None,30)
                                    num = font.render('3',True,Color('Blue'))
                                    pygame.display.update(wind.blit(num,[bleft + 5,btop]))
                                    return True
                                    break
                


def two(xneg,xplus,yneg,yplus,btop,bleft,mined,indexnum1,wind):
    xneg3 = xneg
    yneg2 = yneg
    yneg3 = yneg
    xplus3 = xplus
    yplus2 = yplus
    yplus3 = yplus
    rect_list1 = list(itertools.combinations([xneg,xplus,yplus,yneg,bleft,btop],2))
    for indexnum2 in mined.keys():
        for combo in rect_list1:
            
            if (
                        
                combo[0] in mined[indexnum1].values()
                and combo[1] in mined[indexnum1].values()
                
            ):
                rect_list1.remove(combo)
                for combo2 in rect_list1:
                    
                    if(
                    combo2[0] in mined[indexnum2].values()
                    and combo2[1] in mined[indexnum2].values() 
                    ):      
                        font = pygame.font.Font(None,30)
                        num = font.render('2',True,Color('Blue'))
                        pygame.display.update(wind.blit(num,[bleft + 5,btop]))
                        return True



def check_if_mines(**rects):
    mines = rects.get('mines')
    checkXneg = rects.get('checkXneg')
    checkXplus = rects.get('checkXplus')
    checkYneg = rects.get('checkYneg')
    checkYplus = rects.get('checkYplus')
    basetop = rects.get('recttop')
    baseleft = rects.get('rectleft')
    wind = rects.get('wind')
    for indexrect in mines.keys():
        if (eight(checkXneg,checkXplus,checkYneg,checkYplus,basetop,baseleft,mines,indexrect,wind)):
            break
        elif (seven(checkXneg,checkXplus,checkYneg,checkYplus,basetop,baseleft,mines,indexrect,wind)):
            break
        elif (six(checkXneg,checkXplus,checkYneg,checkYplus,basetop,baseleft,mines,indexrect,wind)):
            break
        elif (five(checkXneg,checkXplus,checkYneg,checkYplus,basetop,baseleft,mines,indexrect,wind)):
            break
        elif (four(checkXneg,checkXplus,checkYneg,checkYplus,basetop,baseleft,mines,indexrect,wind)):
            break
        elif (three(checkXneg,checkXplus,checkYneg,checkYplus,basetop,baseleft,mines,indexrect,wind)):
            break
        elif (two(checkXneg,checkXplus,checkYneg,checkYplus,basetop,baseleft,mines,indexrect,wind)):
            break    
        else:
            rect_list = list(itertools.combinations([checkXneg,checkXplus,checkYneg,checkYplus,basetop,baseleft],2))
            for combo in rect_list:      
                if (        
                    combo[0] in mines[indexrect].values()
                    and combo[1] in mines[indexrect].values()
                ):
                    font = pygame.font.Font(None,30)
                    num = font.render('1',True,Color('Blue'))
                    pygame.display.update(wind.blit(num,[baseleft + 5,basetop]))
                    break
                    
   

    