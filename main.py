from time import sleep as wait
import numpy as np

class Server:

    Players = 0

with open('totalplayers.txt', 'r') as file:
    Server.Players = int(int(file.read()) + 1)

with open('totalplayers.txt', 'w') as file:
    file.write(str(Server.Players))

def printloop(x: int, y: str):
    for i in range(x):
        print(y)

class NewPlayer():

    def __init__(self, name, id):
        self.name = name
        self.id = id

        self.x = 0
        self.y = 0

        self.locationbefore = None
    
    def __repr__(self) -> str:
        return self.name + f' Player: x = {self.x}, y = {self.y}, id = {self.id}'

player: NewPlayer = NewPlayer('Player1', Server.Players)

current_map: list = []

xs = 10
ys = 5

for i in range(ys):
    current_map.append([]) 

for y in range(ys):
    for x in range(xs):

        current_map[y].append([' '])

while True:
    
    printloop(50, '')

    wait(0.1)

    print(player)
    print()
    
    px = player.x
    py = player.y

    if player.locationbefore == None:

        current_map[py][px].remove(' ')
        current_map[py][px].append('A')
        
        player.locationbefore = [py, px]
    else:

        current_map[player.locationbefore[0]][player.locationbefore[1]].remove('A')
        current_map[player.locationbefore[0]][player.locationbefore[1]].append(' ')

        current_map[py][px].remove(' ')
        current_map[py][px].append('A')
        
        player.locationbefore = [py, px]
    
    
    for i in current_map:
        print(i)

    userinput: str = input('Use WASD to move >>: ')

    if userinput.lower() == "w":
        player.y -= 1
    
    elif userinput.lower() == "s":
        player.y += 1
    
    elif userinput.lower() == "a":
        player.x -= 1
    
    elif userinput.lower() == "d":
        player.x += 1
