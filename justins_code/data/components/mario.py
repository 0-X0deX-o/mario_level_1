    def adjust_rect(self):
        """Makes sure new Rect has the same bottom and left
        location as previous Rect"""
        x = self.rect.x
        bottom = self.rect.bottom
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = bottom


    def become_small(self):
        self.big = False
        self.right_frames = self.right_small_normal_frames
        self.left_frames = self.left_small_normal_frames
        bottom = self.rect.bottom
        left = self.rect.x
        image = self.right_frames[0]
        self.rect = image.get_rect()
        self.rect.bottom = bottom
        self.rect.x = left


    def flag_pole_sliding(self):
        """State where Mario is sliding down the flag pole"""
        self.state = c.FLAGPOLE
        self.in_transition_state = True
        self.x_vel = 0
        self.y_vel = 0

        if self.flag_pole_timer == 0:
            self.flag_pole_timer = self.current_time
        elif self.rect.bottom < 493:
            if (self.current_time - self.flag_pole_timer) < 65:
                self.image = self.right_frames[9]
            elif (self.current_time - self.flag_pole_timer) < 130:
                self.image = self.right_frames[10]
            elif (self.current_time - self.flag_pole_timer) >= 130:
                self.flag_pole_timer = self.current_time

            self.rect.right = self.flag_pole_right
            self.y_vel = 5
            self.rect.y += self.y_vel

            if self.rect.bottom >= 488:
                self.flag_pole_timer = self.current_time

        elif self.rect.bottom >= 493:
            self.image = self.right_frames[10]


    def sitting_at_bottom_of_pole(self):
        """State when mario is at the bottom of the flag pole"""
        if self.flag_pole_timer == 0:
            self.flag_pole_timer = self.current_time
            self.image = self.left_frames[10]
        elif (self.current_time - self.flag_pole_timer) < 210:
            self.image = self.left_frames[10]
        else:
            self.in_transition_state = False
            if self.rect.bottom < 485:
                self.state = c.END_OF_LEVEL_FALL
            else:
                self.state = c.WALKING_TO_CASTLE


    def set_state_to_bottom_of_pole(self):
        """Sets Mario to the BOTTOM_OF_POLE state"""
        self.image = self.left_frames[9]
        right = self.rect.right
        #self.rect.bottom = 493
        self.rect.x = right
        if self.big:
            self.rect.x -= 10
        self.flag_pole_timer = 0
        self.state = c.BOTTOM_OF_POLE


    def walking_to_castle(self):
        """State when Mario walks to the castle to end the level"""
        self.max_x_vel = 5
        self.x_accel = c.WALK_ACCEL

        if self.x_vel < self.max_x_vel:
            self.x_vel += self.x_accel

        if (self.walking_timer == 0 or (self.current_time - self.walking_timer) > 200):
            self.walking_timer = self.current_time

        elif (self.current_time - self.walking_timer) > \
                self.calculate_animation_speed():
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 1
            self.walking_timer = self.current_time


    def falling_at_end_of_level(self, *args):
        """State when Mario is falling from the flag pole base"""
        self.y_vel += c.GRAVITY



    def check_for_special_state(self):
        """Determines if Mario is invincible, Fire Mario or recently hurt"""
        self.check_if_invincible()
        self.check_if_fire()
        self.check_if_hurt_invincible()
        self.check_if_crouching()


    def check_if_invincible(self):
        if self.invincible:
            if ((self.current_time - self.invincible_start_timer) < 10000):
                self.losing_invincibility = False
                self.change_frame_list(30)
            elif ((self.current_time - self.invincible_start_timer) < 12000):
                self.losing_invincibility = True
                self.change_frame_list(100)
            else:
                self.losing_invincibility = False
                self.invincible = False
        else:
            if self.big:
                self.right_frames = self.right_big_normal_frames
                self.left_frames = self.left_big_normal_frames
            else:
                self.right_frames = self.invincible_small_frames_list[0][0]
                self.left_frames = self.invincible_small_frames_list[0][1]


    def change_frame_list(self, frame_switch_speed):
        if (self.current_time - self.invincible_animation_timer) > frame_switch_speed:
            if self.invincible_index < (len(self.invincible_small_frames_list) - 1):
                self.invincible_index += 1
            else:
                self.invincible_index = 0

            if self.big:
                frames = self.invincible_big_frames_list[self.invincible_index]
            else:
                frames = self.invincible_small_frames_list[self.invincible_index]

            self.right_frames = frames[0]
            self.left_frames = frames[1]

            self.invincible_animation_timer = self.current_time


    def check_if_fire(self):
        if self.fire and self.invincible == False:
            self.right_frames = self.fire_frames[0]
            self.left_frames = self.fire_frames[1]


    def check_if_hurt_invincible(self):
        """Check if Mario is still temporarily invincible after getting hurt"""
        if self.hurt_invincible and self.state != c.BIG_TO_SMALL:
            if self.hurt_invisible_timer2 == 0:
                self.hurt_invisible_timer2 = self.current_time
            elif (self.current_time - self.hurt_invisible_timer2) < 2000:
                self.hurt_invincible_check()
            else:
                self.hurt_invincible = False
                self.hurt_invisible_timer = 0
                self.hurt_invisible_timer2 = 0
                for frames in self.all_images:
                    for image in frames:
                        image.set_alpha(255)


    def hurt_invincible_check(self):
        """Makes Mario invincible on a fixed interval"""
        if self.hurt_invisible_timer == 0:
            self.hurt_invisible_timer = self.current_time
        elif (self.current_time - self.hurt_invisible_timer) < 35:
            self.image.set_alpha(0)
        elif (self.current_time - self.hurt_invisible_timer) < 70:
            self.image.set_alpha(255)
            self.hurt_invisible_timer = self.current_time


    def check_if_crouching(self):
        """Checks if mario is crouching"""
        if self.crouching and self.big:
            bottom = self.rect.bottom
            left = self.rect.x
            if self.facing_right:
                self.image = self.right_frames[7]
            else:
                self.image = self.left_frames[7]
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.x = left


    def animation(self):
        """Adjusts Mario's image for animation"""
        if self.state == c.DEATH_JUMP \
            or self.state == c.SMALL_TO_BIG \
            or self.state == c.BIG_TO_FIRE \
            or self.state == c.BIG_TO_SMALL \
            or self.state == c.FLAGPOLE \
            or self.state == c.BOTTOM_OF_POLE \
            or self.crouching:
            pass
        elif self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]











