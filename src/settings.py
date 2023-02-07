import pygame as pg
import os

VERSIONNUM = "1.2"
TITLESTRING = f"Tetris {VERSIONNUM} | 2023 © S3R43o3" 

vec = pg.math.Vector2
menu_objects = []

FPS: int = 90
FIELD_COLOR = (60, 60, 60)
BG_COLOR = (24, 89, 117)
SCORE_BOARD_COLOR = (39, 40, 41)
HEADER_COLOR = (240, 95, 5)
TEXT_COLOR = (227, 178, 2)
PAUSE_COLOR = (7, 191, 4)


SPRITE_DIR_PATH = "../assets/img/hq2"
MAINFONT_PATH = "../assets/fonts/"


TILE_SIZE: int = 40
FIELD_SIZE = FIELD_W, FIELD_H = 10, 22

FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 2.0, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

ANIM_TIME_INTERVAL = 350  
FAST_ANIM_TIME_INTERVAL = 1
ANIM_MULTIPLIKATOR = 0.175

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.47, FIELD_H * 0.35)

NEEDED_SCORES = {
    1: 2500,
    2: 7500,
    3: 15000,
    4: 30000,
    5: 50000,
    6: 75000
}

MOVE_DIRECTIONS: dict = {
    'left': vec(-1, 0),
    'right': vec(1, 0),
    'down': vec(0, 1)
} 

TETROS: dict = {
    'T':[ (0, 0), (-1, 0), (1, 0), (0, -1) ], 
    'O':[ (0, 0), (0, -1), (1, 0), (1, -1) ], 
    'J':[ (0, 0), (-1, 0), (0, -1), (0, -2) ], 
    'L':[ (0, 0), (1, 0), (0, -1), (0, -2) ], 
    'I':[ (0, 0), (0, 1), (0, -1), (0, -2) ], 
    'S':[ (0, 0), (-1, 0), (0, -1), (1, -1) ], 
    'Z':[ (0, 0), (1, 0), (0, -1), (-1, -1) ]
    }

TETROS_COLOR: dict = {
    'T': 2,
    'O': 0,
    'J': 1,
    'L': 3,
    'I': 4,
    'S': 5,
    'Z': 6
}

HELP_TEXT: list = [
    "Left Arrow / 'A'       -       Move Left",
    "Right Arrow / 'D'      -       Move Right",
    "Down Arrow / 'S'       -       Move Down",
    "Space                  -           Pause",
    "ESC                    -           Exit"
]