#!/usr/bin/python3
# -*- coding: utf-8 -*-

colors = {
    'n/a' : '\033[0m',
    'red' : '\033[31m', 
    'gre' : '\033[32m', 
    'ora' : '\033[33m', 
    'blu' : '\033[34m', 
    'pur' : '\033[35m', 
    'cya' : '\033[36m', 
    'gra' : '\033[37m',  
    'end' : '\033[0m'
}



def p(text, color):
    '''
        Print de "text" en el color elegido (color)
    '''
    if color in colors :
        color_text = colors[color] + text + colors["end"] 
        print(color_text)    


def p2(text1, color1, text2, color2):
    '''
        Print de "text1" en "color1" y "text2" en "color2" (con un espacio entre ambas cadenas)
    '''
    if color1 in colors  and color2 in colors:
        color_text = colors[color1] + text1 + colors["end"] 
        color_text += " " + colors[color2] + text2 + colors["end"] 
        print(color_text)    





