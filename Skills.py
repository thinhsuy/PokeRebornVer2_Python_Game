from Effects import *

class Skill:
    def __init__(self, skillId) -> None:
        self.id = skillId
        self.loadSkillInfor()
        self.loadSkillStats()
        self.loadEffectSkill()
        # self.skillSprite = pygame.image.load(path).convert_alpha()

    def loadSkillInfor(self):
        sql = "SELECT * FROM Skill WHERE skillId=\'"+self.id+"\'"
        cursor.execute(sql)
        for cur in cursor: 
            id, self.name, self.kind, self.eleId, self.explain, self.category = tuple(cur)

    def loadSkillStats(self):
        sql = "SELECT * FROM SkillInfor WHERE skillId=\'"+self.id+"\'"
        cursor.execute(sql)
        for cur in cursor:
            id, self.damage, self.accuracy, self.countdown, self.range = tuple(cur)

    def loadEffectSkill(self):
        sql = "SELECT * FROM SkillEffect WHERE skillId=\'"+self.id+"\'"
        cursor.execute(sql)
        self.EffectList = []
        for cur in cursor:
            cur = list(cur)
            effect = Effect(cur[1], cur[2], cur[3])
            self.EffectList.append(effect)