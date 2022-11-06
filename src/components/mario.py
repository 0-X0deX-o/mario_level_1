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

# Sets up timers for animation
	def setup_timers(self):
		self.walking_timer = 0
		self.invincible_animation_timer = 0
		self.fire_transitition_timer = 0
		self.death_timer = 0
		self.transition_timer = 0
		self.last_fireball_timer = 0
		self.hurt_invisible_timer2 = 0
		self.flag_pole_timer = 0

# Sets up booleans that affect Mario's behavior
	def setup_state_booleans(self):
		self.facing_right = True
		self.allow_jump = True
		self.dead = False
		self.invincible = False
		self.big = False
		self.fire = False
		self.allow_fireball = True
		self.in_transition_state = False
		self.hurt_invincible = False
		self.in_castle = False
		self.crouching = False
		self.losing_invincibility = False

# Sets  up forces that affect Marios's velocity
	def setup_forces(self):
		self.x_vel = 0
		self.y_vel = 0
		self.max_x_vel = c.MAX_WALK_SPEED
		self.max_y_vel = c.MAX_Y_VEL
		self.x_accel = c.WALK_ACCEL
		self.jump_vel = c.JUMP_VEL
		self.gravity = c.GRAVITY

# These keep track of various total for important values
	def setup_counters(self):
		self.frame_index = 0
		self.invincible_index = 0
		self.fire_transition_index = 0
		self.fireball_count = 0
		self.flag_pole_right = 0

# Extracts Mario images from his sprite sheet and assigns them to lists
	def load_images_from_sheet(self):
		self.right_frames = []
		self.left_frames = []
		
		self.right_small_normal_frames = []
		self.left_small_normal_ferames = []
		self.right_small_green_frames = []
		self.left_small_green_frames = []
		self.right_small_red_frames = []
		self.left_small_red_frames = []
		self.right_small_black_frames = []
		self.left_small_black_frames = []
	
		self.right_big_normal_frames = []
		self.left_big_normal_frames = []
		self.right_big_green_frames = []
		self.left_big_green_frames = []
		self.right_big_red_frames = []
		self.left_big_red_frames = []
		self.right_big_black_frames = []
		self.left_big_black_frames = []

		self.right_fire_frames = []
		self.left_big_fire_frames = []
		
# Images for normal small mario
	
	self.right_small_normal_frames.append(
		self.get_image(178, 32, 12, 16) # Right [0]
	)
	self.right_small_normal_frames.append(
		self.get_image(80, 32, 15, 16) # Right wlaking 1 [1]
	)
	self.right_small_normal_frames.append(
		self.get_image(96, 32, 16, 16) # Right walking 2 [2]
	)
	self.right_small_normal_ferames.append(
		self.get_image(112, 32, 16, 16) # Right wlaking 3 [3]
	)
	self.right_smale_normal_frames.append(
		self.get_image(144, 32, 16,16) # Right Jump [4]	
	)
	self.right_small_normal_frames.append(
		self.get_image(130, 32, 14, 16) # Right skid [5]
	)
	self.right_small_normal_frames.append(
		self.get_image(160, 32, 15, 16) # Death frame [6]
	)
	self.right_small_normal_frames.append(
		self.get_image(320, 8, 16, 24) # Transition small to big [7]
	)
	self.right_small_normal_frames.append(
		self.get_image(241, 33, 16, 16) # Transitionbig to small [8]
	)
	self.right_small_normal_frames.append(
		self.get_image(194, 32, 12, 16) # Frame 1 of flag pole Slide [9]
	)
	self.right_small_normal_frames.append(
		self.get_image_(210, 33, 12, 16) # Frame 2 of flag pole slide [10]
	)
	
# Images for small geen mario (for invincible animation)

	self.right_small_green_frames.append(
		self.get_image(178, 224, 12, 16) # Right standing [0]
	)
	self.right_small_green_frames.append(
		self.get_image(80, 224, 15, 16) # Right walking 1 [1]
	)
	self.right_small_green.append(
		self.get_image(96, 224, 16, 16) # Right walking 2 [2] 
	)
	self.right_small_green_frames.append(
		self.get_image(112, 224, 25, 16) # Right walking 3 [3]
	)
	self.right_small_green_frames.append(
		self.get_image(144, 224, 16,16) # Right jump [4]
	)
	self.right_small_green_frames.append(
		self.get_iamge(130, 224, 14, 16) # Right skid [5]
	)

# Images for red mario (for invincible animation)
 
	self.right_small_red_frames.append(
		self.get_image(178, 272, 12, 16) # Right standing [0]
	)
	self.right_small_red_frames.append(
		self.get_iamge(80,, 272, 15, 16) # Right walking 1 [1]
	)
	self.right_small_red_frames.append(
		self.get_image(96, 272, 16, 16) # Right walking 2 [2]
	)
	left.right_small_red_frames.append(
		self.get_image(112, 272, 15,16) # Right walking 3 [3]
	)
	self.right_small_red_frames.append(
		self.get_image(144, 272, 16, 16) # Right jump [4]
	)
	self.right_small_red_frames.append(
		self.get_image(130, 272, 14, 16) # Right skid [5]
	)

# Images for black mario (for invincible animation)
	
	self.right_small_black_frames.append(
		self.get_image(178, 176, 12, 16) # Right standing [0]
	)
	self.right_small_black_frames.append(
		self.get_image(80, 176, 15, 16) # Right walking 1 [1]
	)
	self.right_small_black_frames.append(
		self.get_image(96, 176, 16, 16) # Right walking 2 [2]
	)
	self.right_small_black_frames.append(
		self.get_image(112, 176, 15, 16) # Right walking 3 [3]
	)
	self.right_small_black_frames.append(
		self.get_image(144, 176, 16, 16) # Right jump [4]
	)
	self.right_small_black_frames.append(
		self.get_image(130, 176, 14, 16) # Right skid [5]
	)

# Images for normal big Mario
	
	self.right_big_normal_frames.append(
		self.get_image(176, 0, 16, 32) # Right standing [0]
	)
	self.right_big_normal_frames.append(
		self.get_image(81, 0, 16, 32) # Right walking 1 [1]
	)
	self.right_big_normal_frames.append(
		self.get_image(97, 0, 15, 32) # Right walking 2 [2]
	)
	self.right_big_normal_frames.append(
		self.get_image(113, 0, 15, 32) # Right walking 3 [3]
	)
	self.right_big_normal_frames.append(
		self.get_image(144, 0, 16, 32) # Right jump [4]
	)	
	self.right_big_normal_frames.append(
		self.get_image(128, 0, 16, 32) # Right skid [5]
	)
	self.right_big_normal_frames.append(
		self.get_image(336, 0, 16, 32) # Right  throwing [6]
	)
	self.right_big_normal_frames.append(
		self.get_image(160, 10, 16, 22) # Right crouching [7]
	)
	self.right_big_normal_frames.append(
		self.get_image(272, 2, 16, 29) # Transition big to small [8]
	)
	self.right_big_normal_frames.append(
		self.get_image(193, 2, 16, 30) # Ferame 1 of flag pole slide [9]
	)
	self.right_big_normal_frames.append(
		self.get_image(209, 2, 16, 29) # Frame 2 of flag pole slide [10]
	)

# Images for big green Mario

	self.right_big_green_frames.append(
		self.get_image(176, 19, 16, 32) # Right standing [0]
	)
	self.right_big_green_frames.append(
		self.get_image(81, 192, 16, 32) #Right walking 1 [1]
	)
	self.right_big_green_frames.append(
		self.get_image(97, 192, 15, 32) #Right walking 2 [2]
	)
	self.right_big_green_frames.append(
		self.get_image(113, 192, 15, 32) #Right walking 3 [3]
	)
	self.right_big_green_frames.append(
		self.get_image(144, 192, 16, 32) #Right jump [4]
	)
	self.right_big_green_frames.append(
		self.get_image(128, 192, 16, 32) #Right skid [5]
	)
	self.right_big_green_frames.append(
		self.get_image(336, 192, 16, 32) #Right throwing [6]
	)
	self.right_big_green_frames.append(
		self.get_image(160, 202, 16, 22) #Right Crouching [7] 
	)

# Images for red big Mario
	
	self.right_big_red_frames.append(self.get_image(176,240,16,32)) # Right standing [0]
	self.right_big_red_frames.append(self.get_image(81,240,16,32)) # Right walking 1 [1]
	self.right_big_red_frames.append(self.get_image(97,240,16,32)) # Right walking 2 [2]
	self.right_big_red_frames.append(self.get_image(113,240,15,32)) # Right walking 3 [3]
	self.right_big_red_frames.append(self.get_image(144,240,16,32)) # Right jump [4]
	self.right_big_red_frames.append(self.get_image(128,240,16,32)) # Right skid [5]
	self.right_big_red_frames.append(self.get_image(336,240,16,32)) # Right throwing [6]
	self.right_big_red_frames.append(self.get_image(160,250,16,22)) # Right crouching [7]

# Images for black big mario
	
	self.right.big_black_mario_frames.append(self.get_image(176,144,16,32)) # Right walking 0 [0]
	self.right.big_black_mario_frames.append(self.get_image(81,144,16,32)) # Right walking 1 [1]
	self.right.big_black_mario_frames.append(self.get_image(i87,144,15,32)) # Right walking 2 [2]
	self.right.big_black_mario_frames.append(self.get_image(113,144,15,32)) # Right walking 3 [3]
	self.right.big_black_mario_frames.append(self.get_image(144,144,16,32)) # Right jump  [4]
	self.right.big_black_mario_frames.append(self.get_image(128,144,16,32)) # Right skid [5]
	self.right.big_black_mario_frames.append(self.get_image(336,144,16,32)) # Right throwing  [6]
	self.right.big_black_mario_frames.append(self.get_image(160,154,16,22)) # Right Crouching  [7]

# Images for Fire Mario

	self.right_fire_frames.append(self.get_image(176,48,16,32)) # Right standing [0]
	self.right_fire_frames.append(self.get_image(81,48,16,32)) # Right walking 1 [1]
	self.right_fire_frames.append(self.get_image(97,48,15,32)) # Right walking 2 [2]
	self.right_fire_frames.append(self.get_image(113,48,15,32)) # Right walking 3 [3]
	self.right_fire_frames.append(self.get_image(144,48,16,32)) # Right jump  [4]
	self.right_fire_frames.append(self.get_image(128,48,16,32)) # Right skid [5]
	self.right_fire_frames.append(self.get_image(336,48,16,32)) # Right Throwing [6]
	self.right_fire_frames.append(self.get_image(160,58,16,22) # Right Crouching [7]
	self.right_fire_frames.append(self.get_image(0,0,0,0) # Place hodler [8]
	self.right_fire_frames.append(self.get_image(193,50,16,29)) # Frame 1 of flag pole slide  [9]
	
	self.right_fire_frames.append(self.get_image(209,50,16,29)) # Frame 2 of flag pole slide [10]

# The left image frames are numbered the same as the right frames only reversed

	for frame in self.right_small_normal_frames:
		new_image = pg.transform.flip(frame, True, False)
		self.left_small_normal_frames.append(new_image)

	for frame in self.right_small_green_frames:
		new_image = pg.transform.flip(frame, True, False)
		self.left_small_green_frames.append(new_image)

	for frame in self.right_small_red_frames:
		new_image = pg.transform.flip(frame, True, False)
		self.left_small_red_frames.append(new_image)

	for frame in self.right_small_black_frames:
		new_image = pg.transform.flip(frame, True, False)
		self.left_small_black_frames.append(new_image)

	for frame in self.right_big_normal_frames:
		new_image = pg.transform.flip(frame, True, False)
		self.left_big_normal_frames.append(new_image)

	for frame in self.right_big_green_frames:
		new_image = pg.transform.flip(frame, True, False)
		self.left_big_green_frames.append(new_image)

	for frame in self.right_big_red_frames:
		new_image = pg.transform.flip(frame, True, False)
		self.left_big_red_frames.append(new_image)
	
	for frame in self.right_big_black_frames:
		new_image = pg.transform.flip(frame, True, False)
		self.left_big_black_frames.append(new_image)

	for frame in self.right_fire_frames:
		new_image = pg.transform.flip(frame, True, False)
		self.left_fire_frames.append(new_image)

	self.normal_small_frames = [self.right_small_normal_frames,self.left_small_normal_frames]
	self.green_small_frames = [self.right_small_normal_frames,self.left_small_normal_frames]
	self.red_small_frames = [self.right_small_red_frames,self.left_small_red_frames]
	self.black_small_frames = [self.right_small_black_frames,self.left_small_black_frames]
	self.invincible_small_frames_list = [
		self.normal_small_frames,
		self.green_small_frames,
		self.red_small_frames,
		self.black_small_frames
	]
	self.normal_big_frames = [
		self.right_big_normal_frames,
		self.left_big_normal_frames
	]
	self.green_big_frames = [self.right_big_green_frames,self.left_big_red_frames]
	self.red_big_frames = [self.right_big_red_frames,self.left_big_black_frames]
	self.black_big_frames = [self.right_big_black_frames,self.left_big_black_frames]
	self.fire_frames = [self.right_fire_frames,self.left_fire_frames]
	self.invincible_big_frames_list = [
		self.normal_big_frames,
		self.green_big_frames,
		self.red_big_frames,
		self.black_big_frames
	]
	self.all_images = [
		self.right_big_normal_frames,
		self.right_big_black_frames,
		self.right_big_red_frames,
		self.right_big_green_frames,,
		self.right_small_normal_frames,
		self.right_small_green_frames,
		self.right_small_red_frames,
		self.right_small_black_frames,
		self.left_big_normal_frames,
		self.left_big_black_frames,
		self.left_big_red_frames,
		self.left_big_green_frames,
		self.left_small_normal_frames,
		self.left_small_red_frames,
		self.left_small_green_frames,
		self.left_small_black_frames
	]
	self.right_frames = self.normal_small_frames[0]
	self.left_frames = self.normal_small_frames[1]

# Extracts image from sprite sheet
	def get_image(self, x, y, width, height):
		image = pg.Surface([width, height])
		rect = image.get_rect()

		image.blit(self.sprite_sheet, (0,0), (x, y, width, height))
		image.set_colorkey(c.BLACK)
		image = pg.transform.scale(
			image,
			(int(rect.width * c.SIZE_MULTIPLIER),
			int(rect.height * c.SIZE_MULTIPLIER))
		)
		return image

# Upadtes Mario's states and animations once per frame
	def update(self, keys, game_info, fire_group):
		self.current_time = game_info[c.CURRENT_TIME]
		self.handle_state(keys, fire_group)
		self.check_for_special_state()
		self.animation()


	
