from Effects import *
from SimpleFuncs import *

def setup_Stun(target, targetTeam, effect):
    for i in range(len(targetTeam.team)):
        if (targetTeam.team[i].id == target.id and 
            isAlive(targetTeam.team[i]) and
            not checkEffectExist(effect, targetTeam.battleEffect[i])):
                targetTeam.battleEffect[i].append(effect)
                return

def is_Stun(pokemon, Team):
    for i in range(len(Team.battleEffect)):
        if (Team.team[i].id==pokemon.id):
            for effect in Team.battleEffect[i]:
                if effect.name == 'Stun':
                    Team.battleEffect[i].remove(effect)
                    return True
    return False