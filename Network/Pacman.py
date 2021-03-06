import numpy as np
import networkx as nx
import Network
'''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%......................................%
%.%%%%.%%%%.%%%%.%%%%%.%%%%.%%%%.%%%%%.%
%.%%%%......%%%%.%%%%%......%%%%.%%%%%.%
%......%%%%.%%%%.......%%%%.%%%%.......%
%.%%%%.%%%%......%%%%%.%%%%......%%%%%.%
%.%%%%......%%%%.%%%%%..P...%%%%.%%%%%.%
%.%%%%.%%%%.%%%%.%%%%%.%%%%.%%%%.%%%%%.%
%......................................%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''
##Move function to calculate next move
##Takes in 2d-array:broad, int:count number of remaining o,int x,y: x y position of '>'
##return tuple (2d-array:broad , int:count number of remaining o)
def Move(broad,count,x,y):
    #next move
    broad[x][y] = ' '
    if(broad[x+1][y] == '.'):
        broad[x + 1][y] = 'P'
        x = x+1
        count -= 1
    elif(broad[x-1][y] == '.'):
        broad[x - 1][y] = 'P'
        x = x-1
        count -= 1
    elif(broad[x][y+1] == '.'):
        broad[x][y + 1] = 'P'
        y = y+1
        count -= 1
    elif(broad[x][y-1] == '.'):
        broad[x][y - 1] = 'P'
        y = y-1
        count -= 1
    else:
        count -= count
    return (broad,count,x,y)

##Main function
##Take in string:path file location
##return nothing
def Pacman(path):
    #load text
    count = 0
    broad = [[]]
    with open(path) as f:
        content = list(f.read())
    j = 0
    for i in content:
        if(i == '\n'):
            broad.append([])
            j += 1
        else:
            broad[j].append(i)
    # print
    for i in broad:
        print(*i)
    #search for '>'
    x,y = 0,0
    for i in range(len(broad)):
        for j in range(len(broad[i])):
            if(broad[i][j] == 'P'):
                x,y = i,j
            if(broad[i][j] == '.'):
                count += 1
    #move it
    while(count > 0):
        (broad,count,x,y) = Move(broad,count,x,y)
        #print
        for i in broad:
            print(*i)

##runit
Pacman('broad.txt')
