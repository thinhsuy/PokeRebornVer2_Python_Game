from email import header


from header import *

class Effect:
    def __init__(self, name, rate, rangeEffect):
        self.name = name
        self.loadEffect()
        self.rate = rate
        self.rangeEffect=rangeEffect
        try:
            self.sprite = pygame.image.load(PATH+'source/Effects/'+self.name+'.png').convert()
            self.sprite = pygame.transform.scale(self.sprite, (20,20))
        except:
            self.sprite = 'none'
            
    def loadEffect(self):
        sql = "SELECT * FROM Effect WHERE effectName=\'"+self.name+"\'"
        cursor.execute(sql)
        for cur in cursor:
            name, self.describe, self.typeEffect = tuple(cur)
    