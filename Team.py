from Pokemons import *
from LifeBar import *

class Team:
    def __init__(self, teamList, pos, gap=100):
        self.team = teamList
        self.posX, self.posY = pos
        self.gap = 150
        self.generateHPbar()
        self.battleEffect = [[] for _ in range(len(self.team))]
        # this variable would store the position of each pokemon
        self.teamPos = [{'id': pokemon.id, 'pos': (self.getNewPosx(i), self.posY)} for pokemon, i in zip(teamList, range(len(teamList)))]
        
    def getNewPosx(self, iter):
        return self.posX+self.gap*iter

    def getConstPos(self, pokemon):
        for posPack in self.teamPos:
            if (posPack['id']==pokemon.id):
                return posPack['pos']

    def generateHPbar(self):
        y = self.posY-130 if self.posY<=SCREEN_HEIGHT/2 else self.posY+30
        self.HPbar = [LifeBar(pokemon.id, pokemon.hp, (self.getNewPosx(i)-70, y)) for pokemon, i in zip(self.team, range(len(self.team)))]