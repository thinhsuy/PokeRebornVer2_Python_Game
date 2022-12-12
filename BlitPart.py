from SimpleFuncs import *

def split_animated_gif(gif_file_path):
    ret = []
    gif = Image.open(gif_file_path)
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(
            frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode
        )
        ret.append(pygame_image)
    return {'list': ret, 'frame': 0}
    

def BlitGif(screen, object, pos, speed=1.0, isOneAction=False, scalePoint='midbottom'):
    if object['frame']>=len(object['list']):
        object['frame'] = len(object['list'])-1 if isOneAction else 0
    img = object['list'][int(object['frame'])]
    rect = img.get_rect(midbottom=pos) if scalePoint=='midbottom' else img.get_rect(center=pos)
    screen.blit(img, rect)
    object['frame']+=speed
    return object


def BlitBased(screen, pokemon, pos):
    rect = pokemon.Based.get_rect(midbottom=(pos[0], pos[1]))
    screen.blit(pokemon.Based, rect)


def BlitText(screen, text, pos, size=20,color=(255,255,255), FontFamily='sans'):
    font=pygame.font.SysFont(FontFamily, size)
    string = font.render(text, True, color)
    screen.blit(string, pos)


def BlitBox(screen, pos, size, color=(0,0,0), border=5, borderColor=(255,255,255)):
    boxX, boxY = pos
    boxWidth, boxHeight = size
    pygame.draw.rect(screen, borderColor, (boxX,boxY,boxWidth,boxHeight))
    pygame.draw.rect(screen, color, (boxX+border, boxY+border, boxWidth-(border*2), boxHeight-(border*2)))


def Blit_mutiline_text(surface, text, pos, limit, size=20, FontFamily='sans', color=(255,255,255)):
    font = pygame.font.SysFont(FontFamily, size)
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = limit
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height
