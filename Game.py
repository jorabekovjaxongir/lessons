from time import sleep 
from random import choice
    
def move(x, y,B=True):
    if B:   
        print(f"\033[{y};{x}H\033[0m",end="")
    else:
        print(f"\033[{y};{x}H",end="")
def clear_screen():
    print("\033c\033[0m",end="")
def ramka():
    a =("-"*120)   
    a+=(f"|"+" "*118+"|")*27
    a+=("-"*120)
    print(a)
def status():
    move(0,0)
    with open('main.txt','r') as f:
        print(f.read()[8:3516])
def status2(x:dict,lt:list):
    status()
    green=f"\033[1;32m"
    red='\033[1;31m'
    yelow='\033[1;33m'
    reset='\033[0m'
    p1,p2=x.keys()
    #p1
    if x[p1]['hp']>=75:
        print(green,end='')
    elif 25<=x[p1]['hp'] and x[p1]['hp']<75:
        print(yelow,end='')
    else:
        print(red,end='')
    move(8,2,False)
    print(p1)
    move(7,3,False)
    print(x[p1]['gun'])
    move(6,4,False)
    print(x[p1]['hp'])
    move(7,5,False)
    print(x[p1]['ammo'])
    print(reset)
    #p2
    if x[p2]['hp']>=75:
        print(green,end='')
    elif 25<=x[p2]['hp'] and x[p2]['hp']<75:
        print(yelow,end='')
    else:
        print(red,end='')
    move(110,2,False)
    print(p2)
    move(109,3,False)
    print(x[p2]['gun'])
    move(108,4,False)
    print(x[p2]['hp'])
    move(109,5,False)
    print(x[p2]['ammo'])
        
    move(2,26)
    print(f"1){lt[-3]}",end="")
    move(2,27)
    print(f"2){lt[-2]}",end="")
    move(2,28)
    print(f"3){lt[-1]}",end="")
    move(0,0)
    print('_')
    print(reset,end='')
class Start:
    def __init__(self):
        with open('main.txt','r') as f:
            loby=f.read()[3523:7027]
            print(loby)
            move(51,13)
            p1=input()
            move(51,15)
            p2=input()
            move(10,27)
            max_hp=input()
        start=Players(p1,p2)
        while len(start.players)!=1:
            start.dmg()
        sleep(5)
        with open('main.txt','r') as f:
            print(f.read()[7037:])
            move(54,15)
            print(start.players[0])
            move(0,50)
        with open('history.txt','a') as fayl:
            fayl.write("###############################################\n")
            fayl.write(start.file)
class Players:
    def __init__(self,*players,max_hp=100):
        self.players=list(players)
        self.player_dict={}
        self.file=str()
        self.gundmg={
            "pistol": {
                "ammo":15,
                "dmg":10,
                "fire":5
                },
            "shotgun": {
                "ammo":7,
                "dmg":40,
                "fire":1
                },
            "sniper": {
                "ammo":5,
                "dmg":80,
                "fire":1
                }
            }
        self.playerdmg={
            'head':2,
            'heart':1.7,
            'arm':1,
            'leg':0.7,
            'hand':0.5,
            'promah1':0,
            'promah2':0,
            }
        self.score=["","",""]
        for i in self.players:
            self.player_dict[i]={
                "gun": "",
                "hp": max_hp,
                "ammo": 0,
                "fire": 0
                }
        for i in self.players:
            self.player_dict[i]['gun']=choice(list(self.gundmg.keys()))
            self.file+=(f"{i} player gun:{self.player_dict[i]['gun']}\n")
            self.player_dict[i]['ammo']=self.gundmg[self.player_dict[i]['gun']]['ammo']
            self.player_dict[i]['fire']=self.gundmg[self.player_dict[i]['gun']]['fire']
        clear_screen()
        status2(self.player_dict,self.score)  
        move(0,50)
    def dmg(self):
        for i in self.players:
            sleep(1)
            x=i
            while x==i:
                x=choice(self.players)
            for j in range(self.player_dict[i]['fire']):
                sleep(1)
                if self.player_dict[i]['ammo']!=0:
                    self.player_dict[i]['ammo']-=1
                    shoot=choice(list(self.playerdmg.keys()))
                    dmg=self.gundmg[self.player_dict[i]['gun']]['dmg']*self.playerdmg[shoot]
                    self.player_dict[x]['hp']-=dmg
                    self.file+=(f"player {i} shoot to {shoot} {dmg} of player {x} HP:{self.player_dict[x]['hp']}\n")
                    self.score.append(f"{i}->{shoot}:{x}")
                    if self.player_dict[x]['hp']<=0:
                        self.file+=(f"{x} player dead from {i}\n")
                        self.score.append(f"{x} dead")
                        self.players.pop(self.players.index(x))
                        continue
                else:
                    self.player_dict[i]['ammo']=self.gundmg[self.player_dict[i]['gun']]['ammo']
                    self.file+=(f"{i} Reloading")
                    break
                clear_screen()
                status2(self.player_dict,self.score)
            clear_screen()
            status2(self.player_dict,self.score)  







