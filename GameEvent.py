from SimpleFuncs import *
from EffectSetup import *
from BlitCluster import *
from GameLogic import *

def SkillSelection(event, selection):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            return 0 if selection+1>=3 else selection+1
        elif event.key == pygame.K_LEFT:
            return 2 if selection-1<0 else selection-1
    return selection
    

def GetTurn(order, A, B):
    try:
        order = sorted(order, key=lambda d: d['speed'])
        currentPlayer = order.pop()
        #check pokemon is stun or not
        pokemon = getPokemonById(currentPlayer['id'], A, B)
        team = getTeamById(currentPlayer['team'], A, B)
        while(is_Stun(pokemon, team) or isAlive(pokemon)==False): 
            print(f'{pokemon.name} is stuning')
            currentPlayer = order.pop()
            pokemon = getPokemonById(currentPlayer['id'], A, B)
            team = getTeamById(currentPlayer['team'], A, B)
        print(f'Its {pokemon.name} turn!')
        return order, currentPlayer
    except:
        if len(order)>0:
            target = order.pop()
            return order, target
        return order, 'none'


def SetupTurn(screen, target, A, B, skillSelected):
    if target=='none': return
    global notification
    for pokemon in A.team:
        if pokemon.id==target['id']:
            BLitSkill(screen, pokemon, selection=skillSelected)
            return
    for pokemon in B.team:
        if pokemon.id==target['id']:
            BLitSkill(screen, pokemon, selection=skillSelected)
            return


def SetupNewTurn(screen, A, B, MoveOrder, isNewTurn):
    if isNewTurn==False: return MoveOrder
    for pokemon, i in zip(A.team, range(len(A.team))):
        MoveOrder.append({'id': pokemon.id, 'speed': pokemon.speed, 'team': 'A'})
    for pokemon, i in zip(B.team, range(len(B.team))):
        MoveOrder.append({'id': pokemon.id, 'speed': pokemon.speed, 'team': 'B'})
    return MoveOrder


def SetupHoverWithPokemon(screen, A, B, mouse):
    for pokemon in A.team:
        pos = A.getConstPos(pokemon)
        if (mouse[0]>(pos[0]-pokemon.width/2) and 
            mouse[0]<(pos[0]+pokemon.width/2) and
            mouse[1]>(pos[1]-pokemon.height) and mouse[1]<pos[1]):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                pygame.draw.circle(screen, (240,240,240), (pos[0],pos[1]-20), 70) 
                return {'id': pokemon.id, 'team':'A'}
    for pokemon in B.team:
        pos = B.getConstPos(pokemon)
        if (mouse[0]>(pos[0]-pokemon.width/2) and 
            mouse[0]<(pos[0]+pokemon.width/2) and
            mouse[1]>(pos[1]-pokemon.height) and mouse[1]<pos[1]):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                pygame.draw.circle(screen, (240,240,240), (pos[0],pos[1]-20), 70) 
                return {'id': pokemon.id, 'team':'B'}
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    return {'id': '', 'team': ''}


def ClickTargetEvent(userPackage, hoverPackage, skillSelected, A, B):
    if hoverPackage['id'] == '' and hoverPackage['team'] == '': return
    Skill_Calculation(userPackage, skillSelected, hoverPackage, A, B)