from SimpleFuncs import *
from EffectSetup import *

def Specific_calculation_damage(SkillPercent, stab, attack, defense):
    critical = random.randint(1,2)
    power = GetPercentage(attack, SkillPercent)
    return ((((((2*critical)/5)+2)*power*(attack/defense))/50)+2)*stab


def Calculate_skilldamage(user, skill, target):
    stab = CheckingStab(user, target)
    if skill.kind == 'Physical':
        attack, defense = user.attack, target.defense
    else:
        attack, defense = user.spAttack, target.spDefense
    skill_damage = skill.damage
    return Specific_calculation_damage(skill_damage, stab, attack, defense)


def Healing_Amount(user, userTeam, amount, rangeSkill='Self'):
    for i in range(len(userTeam.team)):
        amount = GetPercentage(userTeam.team[i].maxHp, amount)
        if (rangeSkill=='AOE Self' and isAlive(userTeam.team[i])):
            userTeam.HPbar[i].get_health(amount)
            userTeam.team[i].hp+=amount
            continue
        elif rangeSkill=='Self' and isAlive(userTeam.team[i]) and userTeam.team[i].id==user.id:
            userTeam.HPbar[i].get_health(amount)
            userTeam.team[i].hp+=amount
            return

def Recieve_damage(userUnpackage, targetUnpackage, skill):
    user = userUnpackage['pokemon']
    target, targetTeam = targetUnpackage['pokemon'], targetUnpackage['team']
    for i in range(len(targetTeam.team)):
        damage = Calculate_skilldamage(user, skill, targetTeam.team[i])
        if (skill.range=='AOE Targets' and isAlive(targetTeam.team[i])):
            targetTeam.HPbar[i].get_damage(damage)
            targetTeam.team[i].hp-=damage
            if (not isAlive(targetTeam.team[i])):
                print(f"{targetTeam.team[i].name} is defeated!")
            continue
        elif (skill.range=='Single Target' and isAlive(targetTeam.team[i]) and targetTeam.team[i].id==target.id):
            targetTeam.HPbar[i].get_damage(damage)
            targetTeam.team[i].hp-=damage
            if (not isAlive(targetTeam.team[i])):
                print(f"{targetTeam.team[i].name} is defeated!")
            return


def SetEffects(userUnpackage, targetUnpackage, effect, amount=0):
    if effect.name=='Heal':
        Healing_Amount(userUnpackage['pokemon'], userUnpackage['team'], amount, effect.rangeEffect)
    elif effect.name=='Stun':
        setup_Stun(targetUnpackage['pokemon'], targetUnpackage['team'], effect)

def Skill_Calculation(userPackage, skillSelected, targetPackage, A, B):
    userUnpackage = UnpackPackage(userPackage, A, B)
    targetUnpackage = UnpackPackage(targetPackage, A, B)
    skill = userUnpackage['pokemon'].skillList[skillSelected]
    print(userUnpackage['pokemon'].name, "using", skill.name)
    amountEffect = userUnpackage['pokemon'].skillList[skillSelected].damage
    Recieve_damage(userUnpackage, targetUnpackage, skill)
    [SetEffects(userUnpackage, targetUnpackage, effect, amount=amountEffect) for effect in userUnpackage['pokemon'].skillList[skillSelected].EffectList]


def CheckAliveMembers(Team, MoveOrder):
    index = 0
    while index < len(Team.team):
        if Team.team[index].hp<=0:
            print(f"{Team.team[index].name} is defeated!")
            for order in MoveOrder:
                if order['id']==Team.team[index].id:
                    MoveOrder.remove(order)
            Team.team.pop(index)
            Team.HPbar.pop(index)
            Team.battleEffect.pop(index)
            index-=1
        else: index+=1
    return Team, MoveOrder