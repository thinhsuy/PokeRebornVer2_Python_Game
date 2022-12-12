from BlitPart import *

def BlitPokemonWithBased(screen, pokemon, pos, direct='Front'):
    BlitBased(screen, pokemon, (pos[0], pos[1]+30))
    if direct=='Front':
        pokemon.FrontSprite = BlitGif(screen, pokemon.FrontSprite, (pos[0], pos[1]))
    elif direct=='Back':
        pokemon.BackSprite = BlitGif(screen, pokemon.BackSprite, (pos[0], pos[1]))


def BLitSkill(screen, pokemon, selection=0):
    BlitBox(screen, (0, 450), (400, 150))
    posX, posY = 40, 425
    for skill, i in zip(pokemon.skillList, range(len(pokemon.skillList))):
        if (i==selection):
            BlitText(screen, skill.name, (posX, posY), color=(255, 30, 0))
            Blit_mutiline_text(screen, skill.explain, (10, 460), (400, 150))
        else:
            BlitText(screen, skill.name, (posX, posY))
        posX+=120


def BlitTeam(screen, A, B):
    for pokemon in A.team:
        pos = A.getConstPos(pokemon)
        BlitPokemonWithBased(screen, pokemon, pos)
    for pokemon in B.team:
        pos = B.getConstPos(pokemon)
        BlitPokemonWithBased(screen, pokemon, pos, direct='Back')


def BlitNotification(screen):
    global notification
    BlitBox(screen, (450, 450), (300, 150))
    Blit_mutiline_text(screen, notification, (460, 460), (450+300, 450+150))
    notification=""
    

def getSpecialAnimation(pokemonId, A, B, isAct=False):
    special = []
    for pokemonA, pokemonB in zip(A.team, B.team):
        if (pokemonA.id == pokemonId):
            special = pokemonA.SpecialAnimationSprite
            break
        if (pokemonB.id == pokemonId): 
            special = pokemonB.SpecialAnimationSprite
            break 
    special['frame']=0
    return {
        'animation': special,
        'isAnimating': isAct
    }


def BlitSpecialAnimation(screen, user, A, B, AnimatePackage):
    animation = BlitGif(screen, AnimatePackage['animation'], 
                (SCREEN_LENGTH/2, SCREEN_HEIGHT/2-70), 
                speed=0.2, 
                scalePoint='center',
                isOneAction=True)

    isAct = True if (animation['frame']<len(animation['list'])-1) else False
    return {'animation': animation, 'isAnimating': isAct}

def BlitArrowTurn(screen, arrowObject, currentPlayerPackage, A, B):
    if (currentPlayerPackage=='none'): return
    gap = 150 if (currentPlayerPackage['team']=='A') else 90
    player = UnpackPackage(currentPlayerPackage, A, B)
    pos = player['team'].getConstPos(player['pokemon'])
    BlitGif(screen, arrowObject, (pos[0], pos[1]-gap))

def BlitEffectPerTeam(screen, Team, gapX=0, gapY=0):
    for i in range(len(Team.battleEffect)):
        posX, posY = Team.getConstPos(Team.team[i])
        for effect in Team.battleEffect[i]:
            if (effect.sprite=='none'): continue
            screen.blit(effect.sprite, effect.sprite.get_rect(center=(posX+gapX, posY+gapY)))
            posX+=25

def BlitEffects(screen, A, B):
    BlitEffectPerTeam(screen, A, -60, -145)
    BlitEffectPerTeam(screen, B, -60, 60)
