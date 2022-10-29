__author__ = 'David Liddle'
# David Liddle - COM S 127
# Assignment 4 - 10/29/2022

import pygame as pg
from .. import setup
from .. import constants as c
from . import flashing_coin

# Parent class for all characters used for the overhead level info
class Character(pg.sprite.Sprite):
    
    def __init__(self, image):
        super(Character, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()

# Class for level information like score, coins, time remaining
class OverheadInfor(object):

    def __init__(self, game_info, state):
        self.sprite_sheet = setup.GFX['text_images']
        self.coin_total = game_info[c.COIN_TOTAL]
        self.time = 401
        self.current_time = 0
        self.total_lives = game_info[c.LIVES]
        self.top_score = game_info[c.TOP_SCORE]
        self.state = state
        self.special_state = None
        self.game_info = game_info

        self.create_image_dict()
        self.create_score_group()
        self.create_info_labels()
        self.create_load_screen_labels()
        self.create_countdown_clock()
        self.create_coin_counter()
        self.create_flashing_coin()
        self.create_mario_image()
        self.create_game_over_label()
        self.create_time_out_label()
        self.create_main_menu_labels()

    # Creates the initial images for the score
    def create_image_dict(self):
        self.image_dict = {}
        image_list = []

        block_1 = [3,12,19,27,35,43,51,59,67,75,83,91,99,107,115,123]
        block_2 = [3,11,20,27,35,44,51,59,67,75,83,91,99,108,115,123]
        block_3 = [3,11,20,27]
        block_1 = [230, 238, 246]
        
        for elements in block_1:
            image_list.append(self.get_image(elements, 230, 7, 7))    

        for elements in block_2:
            image_list.append(self.get_image(elements, 238, 7, 7))
    
        for elements in block_3:
            image_list.append(self.get_image(elements, 246, 7, 7))

        image_list.append(self.get_image(48, 248, 7, 7))
        image_list.append(self.get_image(68, 249, 6, 2))
        image_list.append(self.get_image(75, 247, 6, 6))
        
        character_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -*'

        for character, image in zip(character_string, image_list):
            self.image_dict[character] = image
    # Extreacts image from sprite sheet
    def get_image(self, x, y, width, height):
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (a, y, width, height))
        image.set_colorkey((92, 148, 252))
        image = pg.transform.scale(
            image,
            (
                int(rect.width * 2.9),
                int(rect.height * 2.9)
            )
        )
        return image

    # Creates the initial empty score(000000)
    def create_score_group(self):
        self.score_images = []
        self.create_label(self.score_images, '000000', 75, 55)

    # Creates the labels that describe each info
    def create_info_labels(self):
        self.mario_label = []
        self.world_label = []
        self.time_label = []
        self.stage_label = []

        self.create_label(self.mario_label, 'MARIO', 75, 30)
        self.create_label(self.world_label, 'WORLD', 450, 30)
        self.create_label(self.time_label, 'TIME', 625, 30)
        self.create_label(self.stage_label, '1-1', 472, 55)

        self.label_list = [
            self.mario_label,
            self.world_label,
            self.time_label,
            self.stage_label
        ]

    # Creates labels for the center info of a load screen
    def create_load_screen_labels(self):
        world_label = []
        number_label = []

        self.create_label(world_label, 'WORLD', 280, 200)
        self.create_label(number_label, '1-1', 430, 200)

        self.center_labels = [
            world_label,
            number_label
        ]
    
    # Creates the countdown clock for the level
    def create_countdown_clock(self):
        self.count_down_images = []
        self.create_label(self.count_down_images, str(self.time), 645, 55)

    # Creates the label (WORLD, TIME, MARIO)
    def create_label(self, label_list, string, x, y):
        for letter in string:
            label_list.append(Character(self.image_dict[letter]))
        
        self.set_label_reacts(label_list, x, y)

    # Set the location of each individual character
    def set_label_reacts(self, label_list, x, y):
        for i, letter in enumerate(label_list):
            letter.rect.x = x + ((letter.rect.width + 3) * i)
            letter.rect.y = y
            if letter.image == self.image_dict['-']:
                letter.rect.y += 7
                letter.rect.x += 2

    # Creates the infor that tracks the number of coins Mario Collects
    def create_coin_counter(self):
        self.coin_count_images  = []
        self.create_label(self.coin_count_images, '*00', 300, 55)

    # Creates the flashing coin next to the coin total
    def create_flashing_coin(self):
        self.flashing_coin = flashing_coin.Coin(280, 53)

    # Get the Mario image
    def create_mario_image(self):
        self.life_times_image = self.get_image(75, 247, 6, 6)
        self.life_times_rect = self.life_times_image.get_rect(center = (378, 295))
        self.life_total_label = []
        self.create_label(self.life_total_label, str(self.total_lives), 450, 285)
        self.sprite_sheet = setup.GFX['mario_bros']
        self.mario_image = self.get_image(178, 32, 12, 16)
        self.mario_rect = self.mario_image.get_rect(center = (320, 290))

    # Create the label for the GAME OVER screen
    def create_game_over_label(self):
        game_label = []
        over_label = []

        self.create_label(game_label, 'GAME', 280, 300)
        self.create_label(over_label, 'OVER', 400, 300)
        self.game_over_label = [
            game_label,
            over_label
        ]

    # Create the label for the time out screen
    def create_time_out_label(self):
        time_out_label = []
        self.create_label(time_out_label, 'TIME OUT', 290, 310)
        self.time_out_label = [ time_out_label ]

    # Create labels for the MAIN MENU screen
    def create_main_menu_labels(self):
        player_one_game = []
        player_two_game = []
        top = []
        top_score = []

        self.create_label(player_one_game, '1 PLAYER GAME', 272, 360)
        self.create_label(player_two_game, '2 PLAYER GAME', 272, 405)
        self.create_label(top, 'TOP - ', 290, 465)
        self.create_label(top_score, '000000', 400, 465)
        self.main_menu_labels = [
            player_one_game,
            player_two_game,
            top,
            top_score
        ]

    # Updates infor based on what state the game is in
    def update(self, level_info, mario = None):
        self.mario = mario
        self.handle_level_state(level_info)

    