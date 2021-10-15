import kivy 
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.audio import SoundLoader
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

        # player object initiation
        self.player = Player()

        # loading all the required sounds
        self.clik_snd = SoundLoader.load('resc/sounds/click.wav')

        
        
    def acc(self):
        try:
            player_data = open('player_data.bin','rb')
            self.player = pickle.load(player_data)
            player_data.close()
            return True
        except FileNotFoundError:
            pass
            # print(';-;')
        return False
        
    def starto(self):
        Clock.schedule_interval(self.update,0.0167)
        # basically setting the fps ...60 fps ~ 1 frame  / 0.0167 ms ...i think i right...hoefully
        # more like we'll keep updating the file where we store player data and the data we show on screen around 60 times in a sec...yeh number ke saath thoda experiment krke dekhenge
        # kabhi koi abruptly app close bhi kr diya toh stats lose nhi hoga...we'll pickle the player object and store it in a .bin file
        # demn itna comments kabhi nhi likha...

    # dt is a special variable by kivy thats passed to the callback funcs initiated by schedule interval func...apne kaam ka nhi...
    def update(self,dt):                             # use this to update every value on screen ;-;
        # self.ids.id_of_widget.widget_attribute   ...for acessing the widget attributes in kv file
        # self.ids.butt1.text = self.player.username + ' ' + str(self.player.clicks)
        try:
            player_data = open('player_data.bin','wb')
            pickle.dump(self.player,player_data)
            player_data.close()
        except:
            print('missed')
        self.ids.butt2.text = self.player.username

    


    def clicked(self):
        # self.player.clicks = (self.player.clicks+1)%20
        # if self.player.clicks%2==0:
        #     self.ids.butt1.background_normal = 'resc/images/groot.png'
        #     self.ids.butt1.text = 'i am groot'
        # else:
        #     self.ids.butt1.background_normal = 'resc/images/dio.png'
        #     self.ids.butt1.text = 'dio da'
        if self.clik_snd:
            self.clik_snd.play()



        

class main(App):
    def build(self):
        return groot()

if __name__ == '__main__':
    main().run()

# well yeh file me bas kuch aur functions and update file thoda bada hoga bas cuz player object ke bhot saare attributes honge...currency, list of acquired card objects, exp...and stuff
# game functionalities in game.py file inside player class...
