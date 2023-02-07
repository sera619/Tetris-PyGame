from src.settings import *
import pygame.freetype as ft

BASE_DIR = os.path.dirname(__file__)
class Button:
    def __init__(self, x, y, width, height, buttonText="Button", onclickFunction = None, onePress =True):
        self.x = x
        self.y = y

        self.width = width
        self.font = pg.font.SysFont('Arial', 18, True)
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.btn_text = buttonText
        self.fillColors = {
            'normal': 'orange',
            'hover': 'darkred',
            'pressed': 'yellow'
        }
        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect((self.x, self.y, self.width, self.height))
        self.buttonSurf = self.font.render(buttonText, True, (255, 20, 20))

    def process(self, screen):
        mousePos = pg.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        self.buttonSurf = self.font.render(self.btn_text, True, (255, 20, 20))
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            self.buttonSurf = self.font.render(self.btn_text, True, (255, 20, 20))
            if pg.mouse.get_pressed(num_buttons=3)[0] and self.alreadyPressed == False:
                self.buttonSurface.fill(self.fillColors['pressed'])
                self.buttonSurf = self.font.render(self.btn_text, True, (255, 255, 255))

                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        
        screen.blit(self.buttonSurface, self.buttonRect)

class MenuText:
    def __init__(self, app) -> None:
        self.app = app
        #self.font = ft.Font(MAINFONT_PATH+"/mainFont.otf")
        self.font = ft.Font(os.path.join(BASE_DIR + "/" + MAINFONT_PATH, 'mainFont.otf'))
   
    def draw(self):
        self.font.render_to(self.app.screen,(
                WIN_W * 0.155, WIN_H * 0.35
                ),text='TETRIS',
                fgcolor='red',
                size=TILE_SIZE * 2.75,
                bgcolor=SCORE_BOARD_COLOR)
        self.font.render_to(self.app.screen,(
                WIN_W * 0.355, WIN_H * 0.98
                ),text=TITLESTRING,
                fgcolor='grey',
                size=TILE_SIZE * 0.275,
                bgcolor=SCORE_BOARD_COLOR)
    
    def draw_help(self):
        self.font.render_to(self.app.screen,(
                WIN_W * 0.345, WIN_H * 0.05
                ),text='Help',
                fgcolor='red',
                size=TILE_SIZE * 1.65,
                bgcolor=SCORE_BOARD_COLOR)
        self.font.render_to(self.app.screen,(
                WIN_W * 0.355, WIN_H * 0.98
                ),text=TITLESTRING,
                fgcolor='grey',
                size=TILE_SIZE * 0.275,
                bgcolor=SCORE_BOARD_COLOR)
        
        height = 0.225
        for t in HELP_TEXT:
            self.font.render_to(self.app.screen,(
                WIN_W * 0.175, WIN_H * height
                ),text=f'{t}',
                fgcolor=TEXT_COLOR,
                size=TILE_SIZE * 0.5,
                bgcolor=SCORE_BOARD_COLOR)
            height += 0.050

class GameText:
    def __init__(self, app) -> None:
        self.app = app
        #self.font = ft.Font(MAINFONT_PATH+"/mainFont.otf")
        self.font = ft.Font(os.path.join(BASE_DIR + "/" + MAINFONT_PATH, 'mainFont.otf'))
   
    def draw(self):
        self.font.render_to(self.app.screen,(
                WIN_W * 0.535, WIN_H * 0.02
                ),text='TETRIS',
                fgcolor='red',
                size=TILE_SIZE * 1.65,
                bgcolor=SCORE_BOARD_COLOR)
        self.font.render_to(self.app.screen,(
                WIN_W * 0.635, WIN_H * 0.98
                ),text=TITLESTRING,
                fgcolor='grey',
                size=TILE_SIZE * 0.275,
                bgcolor=SCORE_BOARD_COLOR)         

        if self.app.paused and self.app.tetris.game_over:
            self.font.render_to(self.app.screen,(
                WIN_W  * 0.1, WIN_H * 0.275
                ),text='GAME OVER',
                fgcolor='red',
                size=TILE_SIZE * 1.85,
                bgcolor=SCORE_BOARD_COLOR)
            if self.app.gameover_trigger:
                self.font.render_to(self.app.screen,(
                    WIN_W * 0.165, WIN_H * 0.450
                    ),text='Press Enter',
                    fgcolor='red',
                    size=TILE_SIZE * 1.35,
                    bgcolor=SCORE_BOARD_COLOR)
                self.font.render_to(self.app.screen,(
                    WIN_W * 0.45, WIN_H * 0.525
                    ),text='or',
                    fgcolor='red',
                    size=TILE_SIZE * 1.35,
                    bgcolor=SCORE_BOARD_COLOR)
                self.font.render_to(self.app.screen,(
                    WIN_W * 0.235, WIN_H * 0.6
                    ),text='Press Exit',
                    fgcolor='red',
                    size=TILE_SIZE * 1.35,
                    bgcolor=SCORE_BOARD_COLOR)

        elif self.app.paused and not self.app.tetris.game_over:
            self.font.render_to(self.app.screen,(
                        WIN_W * 0.25, WIN_H * 0.425
                        ),text='PAUSED',
                        fgcolor=PAUSE_COLOR,
                        size=TILE_SIZE * 1.75,
                        bgcolor=None)
            if self.app.pause_trigger:
                self.font.render_to(self.app.screen,(
                    WIN_W * 0.15, WIN_H * 0.55
                    ),text='Press Space',
                    fgcolor=PAUSE_COLOR,
                    size=TILE_SIZE * 1.35,
                    bgcolor=None)
        else:
            self.font.render_to(self.app.screen,(
                    WIN_W * 0.635, WIN_H * 0.15
                    ),text='Next',
                    fgcolor=HEADER_COLOR,
                    size=TILE_SIZE * 1.25,
                    bgcolor=SCORE_BOARD_COLOR)

            self.font.render_to(self.app.screen,(
                    WIN_W * 0.595, WIN_H * 0.5
                    ),text='Score',
                    fgcolor=HEADER_COLOR,
                    size=TILE_SIZE * 1.25,
                    bgcolor= SCORE_BOARD_COLOR)
                
            self.font.render_to(self.app.screen,(
                    WIN_W  * 0.595, WIN_H * 0.575
                    ),text=f'{self.app.tetris.score}',
                    fgcolor=TEXT_COLOR,
                    size=TILE_SIZE * 1.25,
                    bgcolor=SCORE_BOARD_COLOR)
            
            self.font.render_to(self.app.screen,(
                    WIN_W * 0.5975, WIN_H * 0.65
                    ),text='Level',
                    fgcolor=HEADER_COLOR,
                    size=TILE_SIZE * 1.25,
                    bgcolor= SCORE_BOARD_COLOR)
                
            self.font.render_to(self.app.screen,(
                    WIN_W  * 0.5975, WIN_H * 0.725
                    ),text=f'{self.app.tetris.level}',
                    fgcolor=TEXT_COLOR,
                    size=TILE_SIZE * 1.25,
                    bgcolor=SCORE_BOARD_COLOR)

            self.font.render_to(self.app.screen,(
                    WIN_W * 0.5975, WIN_H * 0.8
                    ),text='Lines:',
                    fgcolor=HEADER_COLOR,
                    size=TILE_SIZE * 1.25,
                    bgcolor= SCORE_BOARD_COLOR)
                
            self.font.render_to(self.app.screen,(
                    WIN_W  * 0.5975, WIN_H * 0.875
                    ),text=f'{self.app.tetris.all_lines}',
                    fgcolor=TEXT_COLOR,
                    size=TILE_SIZE * 1.25,
                    bgcolor=SCORE_BOARD_COLOR)
