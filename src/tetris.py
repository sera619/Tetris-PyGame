from src.settings import *
from src.tetromino import Tetromino


class TetrisGame:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino: Tetromino = Tetromino(self)
        self.next_tetromino: Tetromino = Tetromino(self, False)
        self.speed_up = False
        self.game_over = False
        self.level = 1
        self.score_needed = NEEDED_SCORES[1]
        self.score = 0
        self.full_lines = 0
        self.all_lines = 0
        self.points_per_line = {0: 0, 1: 100, 2: 200, 3: 700, 4:1500}

    def get_score(self):
        self.score += self.points_per_line[self.full_lines]
        self.all_lines += self.full_lines 
        self.full_lines = 0
        if self.score >= self.score_needed:
            self.level += 1
            self.score_needed = NEEDED_SCORES[self.level]
            self.app.increase_anim_speed()

    def check_full_lines(self):
        row = FIELD_H - 1
        for y in range(FIELD_H - 1, -1, -1):
            for x in range(FIELD_W):
                self.field_array[row][x] = self.field_array[y][x]

                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x, y)
            
            if sum(map(bool, self.field_array[y])) < FIELD_W:
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0
                self.full_lines += 1    
            
    def add_tetromino_to_field(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def is_game_over(self):
        if self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]:
            pg.time.wait(300)
            return True

    def new_game(self):
        self.__init__(self.app)

    def check_tetromino_landing(self):
        if self.tetromino.landing:
            if self.is_game_over():
                # self.game_over = True
                self.game_over = True
                self.app.paused = True
            else:                    
                self.speed_up = False            
                self.add_tetromino_to_field()
                self.next_tetromino.current = True
                self.tetromino = self.next_tetromino
                self.next_tetromino = Tetromino(self, False)

    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT or pressed_key == pg.K_a:
            self.tetromino.move(direction='left')
        elif pressed_key == pg.K_RIGHT or pressed_key == pg.K_d:
            self.tetromino.move(direction='right')
        elif pressed_key == pg.K_UP or pressed_key == pg.K_w:
            self.tetromino.rotate()
        elif pressed_key == pg.K_DOWN or pressed_key == pg.K_s:
            self.speed_up = True

    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black', (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        if self.app.paused:
            return
        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger][self.speed_up]
        if trigger:
            self.check_full_lines()
            self.tetromino.update()
            self.check_tetromino_landing()
            self.get_score()
        self.sprite_group.update()

    def draw(self):
        if not self.app.paused:
            self.draw_grid()
            self.sprite_group.draw(self.app.screen)