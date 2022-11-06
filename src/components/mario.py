import pygame as pg
from .. import setup, tools
from .. import constants as c
from .  import powerups

class Mario(pg.sprit.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.sprite_sheet = setup.GFX['mario_bros']

		self.setup_timers()
		self.setup_state_booleans()
		self.setup_forces()
		self.setup_counters()
		self.load_images_from_sheet()
	
		self.state = c.WALK
		self.image = self.right_frames[self.frame_index]
		self.rect = self.image.get_rect()
		self.mask = pg.mask.from_surface(self.image)

		self.key_timer = 0 
