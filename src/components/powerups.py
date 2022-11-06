import pygame as pg
from .. import constants as c
from .. import setup

# Base Class for all powerup_group
class Powerup(pg.sprite.Sprite):
	def __init__(self, x, y):
		super(Powerup, self).__init__()


# This seperate setup function allows me ot pass a different setup_frames method...
#...depending on what the powerup is
	def setup_powerup(self, x, y, name, setup_frames):
		self.sprite_sheet = setup.GFX['item_objects']
		self.frames = []
		self.frame_index = 0
		setup_frames()
		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.y = y
		self.state = c.REVEAL
		self.y_vel = -1
		self.x_vel = 0
		self.direction = c.RIGHT
		self.box_height = y
		self.gravity = 1
		self.max_y_vel = 8
		self. animate_timer = 0
		self.name = name

#Get the image frmaes from the sprite sheet
	def get_image(self, x, y, width, height):
		
		image = pg.Surface([width, height]).convert()
		rect = image.get_rect()
	
		image.blit(self.sprit_sheet, (0, 0), (x, y, width, height))
		image.set_colorkey(c.BLACK)
		
		image = pg.transform.scale(
			(int(rect.width * c.SIZE_MULTIPLIER),
			 int(rect.height*c.SIZE_MULTIPLIER))
		)
		return image
		
# Updates powerup behavior
	def update(slef, game_info, *args):
		self.current_time = game_info[c.CURRENT_TIME]
		self.handle_state()

	def handle_state(self):
		pass

# Action when power leaves the coin box or brick
	def revealing(self, *args):
		self.rect.y += self.y_vel
		
		if self.rect.bottom <= self.box_height:
			self.rect.bottom = self.box_height
			self.y_vel = 0
			self.state = c.SLIDE

# Action for when powerup slides along the gorund
	def sliding(self):
		if self.direction == c.RIGHT:
			self.x_vel = 3
		else:
			self.xc_vel = -3


