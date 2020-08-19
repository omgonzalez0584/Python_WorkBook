#!/usr/bin/env python3

def reverse_lookup(soccer_player,val):
    claves = []
    for key,value in soccer_player.items():
        if val == value:
            claves.append(key)
    if len(claves) == 0:
        return "No hay jugadores registrados"
    else:
        return claves

soccer_player = {'Messi':10,'Hazard':10,'Suarez':9,'Benzema':9,
                'Iniesta':8,'Ronaldo':7,'Dybala':10,'Zlatan':10,
                'Xavi':6,'Mascherano':5,'Tevez':10,'Neymar':10}

players = reverse_lookup(soccer_player,2);
print(players)
