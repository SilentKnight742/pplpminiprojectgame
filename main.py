import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from game import *
import pickle

class groot(ScreenManager):
    def __init__(self,**kwargs):
        super(groot,self).__init__(**kwargs)     
        # yeh commented out stuff was sockets wala part...abhi chodo yeh
        # self.n = Client()
        # self.other_client = info() 
        # self.my = self.n.getP()
        self.player = Player()
        Clock.schedule_interval(self.update,0.0167)  

        # basically setting the fps ...60 fps ~ 1 frame  / 0.0167 ms ...i think i right...hoefully
        # more like we'll keep updating the file where we store player data and the data we show on screen around 60 times in a sec...yeh number ke saath thoda experiment krke dekhenge
        # kabhi koi abruptly app close bhi kr diya toh stats lose nhi hoga...we'll pickle the player object and store it in a .bin file
        # even i'll have to look it up on how to do it correctly...file handling revision
        # demn itna comments kabhi nhi likha...

    # dt is a special variable by kivy thats passed to the callback funcs initiated by schedule interval func...apne kaam ka nhi...
    def update(self,dt):                             # use this to update every value on screen ;-;
        # self.ids.id_of_widget.widget_attribute   ...for acessing the widget attributes in kv file
        self.ids.butt1.text = self.player.username

    def roll(self):
        pass



        

class main(App):
    def build(self):
        return groot()

if __name__ == '__main__':
    main().run()

# well yeh file me bas kuch aur functions and update file thoda bada hoga bas cuz player object ke bhot saare attributes honge...currency, list of acquired card objects, exp...and stuff
# game functionalities in game.py file inside player class...
