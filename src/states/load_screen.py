from .. import setup, tools
from .. import constants as c
from .. import game_sound
from .. components import info

class LoadScreen(tools._State):
	def __init__(self):
		tools._State.__init__(self)

	def startup(self, current_time, persist):
		self.start_time = current_time
		self.persist = persist
		self.game_info = self.persist
		self.next = self.set_next_state()

		info_state = self.set_overhead_info_state()

		self.overhead_info = info.OverheadInfo(self.game_info, info_state)
		self.sound_manager = game_sound.Sound(self.overhead_info)
	
# Sets the next state
	def set_net_state(self):
		return c.LEVEL1

# sets the state to send to the overhead info object
	def set_overhead_info_state(self):
		return c.LOAD_SCREEN

# sets the state to send to the overhead into object
	def set_overhead_info_state(self):
		return c.LOAD_SCREEN

# Updates the loading screen
	def updagte(elf, surface, keys, current_time):
		if (current_time - self.start_time) < 2400:
			surface.fill(c.BLACK)
			self.overhead_info.update(self.game_info)
			self.overhead_info.draw(surface)

		elif (surrent_time - self.start_time) < 2600:
			surface.fill(c.BLACK)

		elif (current_time - self.start_time) < 2635:
			surface.fill((106, 150, 252))

		else:
			self.done = True


#A loading screen with Game Over
class GameOver(LoadScreen):
	def __init__(self):
		super(GameOver, self).__init__()

# Sets next state
	def set_next_state(self):
		return c.MAIN_MENU
		
# sets the state to send to the overhead info object
	def set_overhead_info_state(self):
		return c.GAME_OVER

# changes state of the background color 
	def update(self, surface, keys, current_time):
		self.current_time = current_time
		self.sound_manager.update(self.persist, None)

		if (self.current_time - self.start_time) < 7000:
			surface.fill(c.BLACK)
			self.overhead_info.update(self.game_info)
			self.overhead_info.draw(surface)
		elif (self.current_time - self.start_time) < 7200:
			surface.fill(c.BLACK)
		elif (self.current_time - self.start_time) < 7235:
			surface.fill((106, 150, 252))
		else:
			self.done = True

# Load Screen from 'Time Out' State change
class TimeOut(LoadScreen):
	def __init__(self):
		super(TimeOut, self).__init__()

# Sets next state
	def set_next_state(self):
		if self.persist[c.LIVES] == 0:
			return c.GAME_OVER
		else:
			return c.LOAD_SCREEN
# sets the state to send to the overhead info object		
	def set_overhead_info_state(self):
		return c.TIME_OUT

	def update(self, surface, keys, current_time):
		self.current_time = current_time

		if (self.current_time - self.start_time) < 2400:
			surface.fill(c.BLACK)
			self.overhead_info.update(self.game_info)
			self.overhead_info.draw(surface)
		else:
			self.done = True
	
