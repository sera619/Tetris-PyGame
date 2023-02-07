import sys,os
from src.settings import *
from src.tetris import TetrisGame
from src.menu import Button, MenuText, GameText
import pathlib

BASE_DIR = os.path.dirname(__file__)

class GameApp:
    def __init__(self) -> None:
        pg.init()
        self.appicon = pg.image.load(os.path.join(BASE_DIR+'/assets/img/' ,'AppIcon.png'))
        pg.display.set_icon(self.appicon)
        pg.display.set_caption(TITLESTRING)
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.anim_interval = ANIM_TIME_INTERVAL
        self.set_timer()
        self.sprites = self.load_sprites()
        self.tetris = TetrisGame(self)
        self.paused = False
        self.game_started = False
        self.on_helpView = False
        self.text = GameText(self)
        self.m_text = MenuText(self)

    def load_sprites(self):
        files = [item for item in pathlib.Path(SPRITE_DIR_PATH).rglob('*.png') if item.is_file()]
        sprites = [pg.image.load(file).convert_alpha() for file in files]
        sprites = [pg.transform.scale(sprite, (TILE_SIZE, TILE_SIZE)) for sprite in sprites]
        return sprites

    def increase_anim_speed(self):
        self.anim_interval -= self.anim_interval * ANIM_MULTIPLIKATOR
        return True

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.pause_event = pg.USEREVENT + 2
        self.gameover_event = pg.USEREVENT +3
        self.anim_trigger = False
        self.fast_anim_trigger = False
        self.pause_trigger = False
        self.gameover_trigger = False
        pg.time.set_timer(self.user_event, self.anim_interval)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.pause_event, 500)
        pg.time.set_timer(self.gameover_event, 600)

    def update(self):
        self.clock.tick(FPS)
        if self.paused or not self.game_started:
            return           
        self.text.draw()
        self.tetris.update()


    def draw(self):
        if self.on_helpView:
            self.screen.fill(SCORE_BOARD_COLOR)
            self.help_btn = Button(WIN_W * 0.415, WIN_H * 0.85, 150, 40, 'Back',self.show_help, onePress=True)
            self.help_btn.process(self.screen)
            self.m_text.draw_help()
        elif self.game_started == False and not self.on_helpView:
            self.screen.fill(color=SCORE_BOARD_COLOR)
            self.start_btn = Button(WIN_W * 0.415, WIN_H * 0.55, 150, 40, 'Sart',self.start_game, onePress=True)
            self.help_btn = Button(WIN_W * 0.415, WIN_H * 0.6, 150, 40, 'Help',self.show_help, onePress=True)
            self.exit_btn =Button(WIN_W * 0.415, WIN_H * 0.65, 150, 40, 'Exit',self.exit_game, onePress=True) 
            self.m_text.draw()
            self.start_btn.process(self.screen)
            self.help_btn.process(self.screen)
            self.exit_btn.process(self.screen)
        elif self.tetris.game_over and self.paused:
            self.screen.fill(SCORE_BOARD_COLOR)
            self.text.draw()
        else:
            self.screen.fill(color=SCORE_BOARD_COLOR)
            self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RES))
            self.tetris.draw()
            self.text.draw()
        pg.display.flip()

    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit
                sys.exit(0)
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                if not self.tetris.game_over:
                    self.paused = not self.paused
            elif event.type == pg.KEYDOWN:
                self.tetris.control(event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True
            elif event.type == self.pause_event:
                self.pause_trigger = not self.pause_trigger
            elif event.type == self.gameover_event:
                self.gameover_trigger = not self.gameover_trigger
            
            if self.tetris.game_over:
                if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                    self.paused = False
                    self.tetris.new_game()
    
    def start_game(self):
        self.game_started = True

    def show_help(self):
        self.on_helpView = not self.on_helpView
        print("Helpview Show: ", self.on_helpView)
        pg.time.wait(150)
    
    def exit_game(self):
        pg.quit()
        sys.exit(0)


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    try:
        app = GameApp()
        app.run()
    except KeyboardInterrupt:
        print("Keyboard quit from user")
        pg.quit()
        sys.exit(0)