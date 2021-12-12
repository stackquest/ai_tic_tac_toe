from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config
from .logic import *


Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)

class HomePage(Screen):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        cell_num, rv = computer_move(COMPUTER)
        cell = f"cell_{cell_num}"
        x = getattr(self.ids, cell)
        x.text = COMPUTER
    def refresh(self):
        app = App.get_running_app()
        app.won = False
        clear_board()
        # clear gui board
        for i in range(1, 10):
            cell_id = f"cell_{i}"
            x = getattr(self.ids, cell_id)
            x.text = ' '
        self.ids.play_again.opacity = 0
        self.ids.info.text = ''
        cell_num, rv = computer_move(COMPUTER)
        cell = f"cell_{cell_num}"
        x = getattr(self.ids, cell)
        x.text = COMPUTER
        
    def gui_human_move(self, cell_id):
        pos = int(cell_id.split('_')[1])
        is_human_move_completed = False
        rv = None
        app = App.get_running_app()
        print(f"{app.won=}")
        if not app.won:
            if is_available(pos):
                rv = human_move(pos, HUMAN)
                # HomePage.show_result(rv)
                x = getattr(self.ids, cell_id)
                x.text = HUMAN
                is_human_move_completed = True
                self.ids.info.text = ""
            else:
                if rv is not None:
                    self.ids.info.text = f"[b][color={COLORS[rv.split('-')[1]]}]{rv.split('-')[0]}[/color][/b]"
            if is_human_move_completed:
                self.ids.info.text = ""
                cell_num, rv = computer_move(COMPUTER)
                # HomePage.show_result(rv)
                cell = f"cell_{cell_num}"
                x = getattr(self.ids, cell)
                x.text = COMPUTER
            if rv is not None:
                self.ids.info.text = f"[b][color={COLORS[rv.split('-')[1]]}]{rv.split('-')[0]}[/color][/b]"
                self.ids.play_again.opacity = 1
                app = App.get_running_app()
                app.won = True
                print(f"{app.won=}")
        

class Game(App):
    sm = ScreenManager()
    won = False
    def build(self):
        Game.sm.add_widget(HomePage(name ="homescreen"))
        return Game.sm