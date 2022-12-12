from Pokemons import *
from header import *
from Team import *
from BlitCluster import *
from GameEvent import *
from GameLogic import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT))
running = True
clock = pygame.time.Clock()

# try:
A = Team([Pokemon('006'), Pokemon('807'), Pokemon('241')], (300, 175))
B = Team([Pokemon('003'), Pokemon('212'), Pokemon('009')], (200, 355))
Background = pygame.image.load('source/Background/CityBattleScreen.png').convert()
turnArrow = split_animated_gif('source/vfx/Arrow.gif')

skillSelected = 0
MoveOrder, currentPlayer = [], 'none'
AnimatePackage = getSpecialAnimation(A.team[0].id, A, B)

while running:
    screen.fill((0,0,0))
    screen.blit(Background, Background.get_rect(center=(SCREEN_LENGTH/2, SCREEN_HEIGHT/2-75)))
    isNewTurn = True if (len(MoveOrder)==0 and currentPlayer=='none') else False
    mouse = pygame.mouse.get_pos()
    
    # A, MoveOrder = CheckAliveMembers(A, MoveOrder)
    # B, MoveOrder = CheckAliveMembers(B, MoveOrder)
    hoverPackage = SetupHoverWithPokemon(screen, A, B, mouse)
    BlitTeam(screen, A, B)
    MoveOrder = SetupNewTurn(screen, A, B, MoveOrder, isNewTurn)
    if isNewTurn: MoveOrder, currentPlayer = GetTurn(MoveOrder, A, B)
    BlitNotification(screen)
    BlitArrowTurn(screen, turnArrow, currentPlayer, A, B)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        skillSelected = SkillSelection(event, skillSelected)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                MoveOrder, currentPlayer = GetTurn(MoveOrder, A, B)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                ClickTargetEvent(currentPlayer, hoverPackage, skillSelected, A, B)
                if (skillSelected==2):
                    AnimatePackage = getSpecialAnimation(currentPlayer['id'], A, B, isAct=True)
                MoveOrder, currentPlayer = GetTurn(MoveOrder, A, B)

    BlitEffects(screen, A, B)

    if (AnimatePackage['isAnimating']==False):
        SetupTurn(screen, currentPlayer, A, B, skillSelected)
        [hpbar.update(screen) for hpbar in A.HPbar]
        [hpbar.update(screen) for hpbar in B.HPbar]
    else:
        AnimatePackage = BlitSpecialAnimation(screen, currentPlayer, A, B, AnimatePackage)

    clock.tick(60)
    pygame.display.flip()
pygame.quit()

# except Exception as e:
#     print("Oops!", sys.exc_info()[0], "occurred.")
#     print("The Error:", e)
#     pygame.quit()