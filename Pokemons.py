from Skills import *
from Effects import *
from BlitPart import *

class Pokemon:
    def __init__(self, id):
        self.FrontSprite = split_animated_gif('source/Pokemon/'+id+'/Front.gif')
        self.BackSprite = split_animated_gif('source/Pokemon/'+id+'/Back.gif')
        self.StatusSprite = split_animated_gif('source/Pokemon/'+id+'/Status.gif')
        self.AttackSprite = split_animated_gif('source/Pokemon/'+id+'/Attack.gif')
        self.SpecialAnimationSprite = split_animated_gif('source/Pokemon/'+id+'/SpecialAnimation.gif')

        self.StatusSprite['list'] = ScaleTimes(self.StatusSprite['list'], 2)
        self.AttackSprite['list'] = ScaleTimes(self.AttackSprite['list'], 2)

        self.width = self.FrontSprite['list'][0].get_width()
        self.height = self.FrontSprite['list'][0].get_height()
        self.id = id
        self.loadElement()
        self.loadBase()
        self.loadStats()
        self.loadSkills()
    
    def loadElement(self):
        sql = "SELECT e.Name FROM Pokemon AS p INNER JOIN PokeType AS pt ON p.pokeId=pt.pokeId and p.pokeId=\'"+self.id+"\' INNER JOIN Element AS e ON e.eleId=pt.eleId"
        cursor.execute(sql)
        self.Element = []
        for i in cursor: 
            self.Element.append(tuple(i)[0])

    def loadBase(self):
        sql = "SELECT es.Based FROM ElementSource AS es INNER JOIN Element as e ON e.eleId=es.eleId and e.Name=\'"+str(self.Element[0])+"\'"
        cursor.execute(sql)
        for cur in cursor:
            path = tuple(cur)[0]
            self.Based = pygame.image.load(path).convert_alpha()
            break
        
    def loadStats(self):
        sql = "SELECT p.Name, pi.* FROM Pokemon AS p INNER JOIN PokeInfor AS pi ON p.pokeId=pi.pokeId and p.pokeId=\'"+self.id+"\'"
        cursor.execute(sql)
        for cur in cursor:
            self.name, id, self.hp, self.attack, self.spAttack, self.defense, self.spDefense, self.speed = tuple(cur)
            self.maxHp = self.hp
            break
    
    def loadSkills(self):
        sql = "SELECT ps.* FROM PokeSkill AS ps INNER JOIN Pokemon AS p ON ps.pokeId=p.pokeId and p.pokeId=\'"+self.id+"\'"
        cursor.execute(sql)
        self.skillList = []
        for cur in cursor:
            self.skillList.append(tuple(cur)[1])
        self.skillList = [Skill(id) for id in self.skillList]