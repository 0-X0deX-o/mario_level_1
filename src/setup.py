__author__ = 'David Liddle'

"""
This module initialized the display and creates dictionaries of resources
"""

import os
import pygame as pg
from tools import tools
from . import constants as c

ORIGINAL_CAPTION = c.ORIGINAL_CAPTION

os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

FONTS = tools.load_all_fonts(os.path.join("av","fonts"))
MUSIC = tools.load_all_music(os.path.join("av", "sound/music"))
GFX = tools.load_all_music(os.path.join("av", "png"))
SFX = tools.load_all_music(os.path.join("av", "sound/sfx"))
