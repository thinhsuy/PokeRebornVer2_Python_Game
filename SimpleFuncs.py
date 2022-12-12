from header import *

def Scale2xGif(object):
    return [pygame.transform.scale2x(frame) for frame in object]

def ScaleTimes(object, time):
    for _ in range(time):
        object = Scale2xGif(object)
    return object

def GetSTAB(eleAttack, eleDefense):
    for i in range(len(STAB['element'])):
        if STAB['element'][i]==eleAttack:
            return STAB[eleDefense][i]

def CheckingStab(user, target):
    stab = 1
    for userEle in user.Element:
        for targetEle in target.Element:
            stab *= GetSTAB(userEle, targetEle)
    return stab

def UnpackPackage(Package, A, B):
    userTeam = A if Package['team']=='A' else B
    user = getPokemonById(Package['id'], A, B, team=userTeam.team)
    return {'pokemon': user, 'team': userTeam}

def GetPercentage(value, portion):
    return portion*value/100

def getPokemonById(id, A, B, team='none', index=-1):
    if (team!='none'):
        for pokemon in team:
            if (pokemon.id == id):
                return pokemon
    if (team!='none' and index!=-1): 
        return team[index]
    for pokemonA, pokemonB in zip(A.team, B.team):
        if (pokemonA.id == id):
            return pokemonA
        if (pokemonB.id == id):
            return pokemonB

def getTeamById(id, A, B):
    return A if id=='A' else B

def isAlive(pokemon):
    return True if pokemon.hp>0 else False

def checkEffectExist(effect, effectList):
    for eff in effectList:
        if eff.name==effect.name:
            return True
    return False