#!/usr/bin/env python3
__author__ 'David Liddle'

"""
This is a rendition of the Mario Level 1
"""

import sys, cProfile
import pygame as pg
from data.mail import main

if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()