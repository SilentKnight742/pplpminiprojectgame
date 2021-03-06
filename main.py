import pickle

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager

from game import *


class groot(ScreenManager):
    def __init__(self,**kwargs):
        super(groot,self).__init__(**kwargs)  

        # player object initiation
        self.player = Player()

        # loading all the required sounds
        # self.clik_snd = SoundLoader.load('resc/sounds/click.wav')
        self.tap_snd = SoundLoader.load('resc/sounds/tap.wav')
        self.success_snd = SoundLoader.load('resc/sounds/success.wav')
        self.wrong_snd = SoundLoader.load('resc/sounds/wrong.wav')
        self.lvl_up_snd = SoundLoader.load('resc/sounds/lvl_up.wav')
        self.burn_snd = SoundLoader.load('resc/sounds/burn.wav')
        self.new_snd = SoundLoader.load('resc/sounds/new.wav')

        # temp var for traversing list of langs of player
        self.tempID = 0

        # temp var for traversing list of all skills
        self.tempID2 = 0

        # temp var for checking new card
        self.new = True
        self.newID = 0

        # temp var for current que obj
        self.que = 0
        self.correct = True
        self.tmr = 21
        self.tmr_left = self.tmr
        self.last_tmr_rec = 0

        # end of root construtor


        
    # to check if the player_data file already exists or not
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

        # end of acc func



    # the update func is for updating time, player_data file and some info displayed on screen
    def starto(self):
        Clock.schedule_interval(self.update,0.005)
        
      
        # end of starto func



    # dt is a special variable by kivy thats passed to the callback funcs initiated by schedule interval func...apne kaam ka nhi...
    def update(self,dt):                             
        # use this to update every value on screen ;-;

        # updating time for quiz and daily rewards
        t = time.time()
        if self.player.qz_time_left <= 1:
            self.ids.quiz_butt.disabled = False                                   
            self.ids.quiz_butt.text = 'Quiz'
        else:
            self.player.qz_time_left -= (t - self.player.qz_last_time_rec)
            self.player.qz_last_time_rec = t
            self.ids.quiz_butt.disabled = True
            self.ids.quiz_butt.text = str(math.floor(self.player.qz_time_left))

        if self.player.dly_time_left <= 1:
            self.ids.dly_butt.disabled = False                                   
        else:
            self.player.dly_time_left -= (t - self.player.dly_last_time_rec)
            self.player.dly_last_time_rec = t
            self.ids.dly_butt.disabled = True

 
        # updating game screen
        if gr.current == 'game_screen':
            
            # lang card view
            if len(self.player.langs)!=0:
                try:
                    k = self.player.langs[self.player.lang_ind[self.tempID]]
                    self.ids.game_lang_card_img.source = 'resc/images/' + k.img_name
                    self.ids.game_lang_card_stat.text = 'Name: ' + k.name + '\nLevel: ' + str(k.card_lvl) + '\nExp: +' + str(k.card_exp)
                    if self.tempID<=0:
                        self.ids.game_prev_butt.disabled = True
                    else:
                        self.ids.game_prev_butt.disabled = False
                    if self.tempID>=len(self.player.langs)-1:
                        self.ids.game_next_butt.disabled = True
                    else:
                        self.ids.game_next_butt.disabled = False
                except:
                    if self.tempID < 0:
                        self.tempID = 0
                    elif self.tempID >= len(self.player.lang_ind):
                        self.tempID = len(self.player.lang_ind) - 1
            else:
                self.ids.game_prev_butt.disabled = True
                self.ids.game_next_butt.disabled = True
                self.ids.game_lang_card_img.source = 'resc/images/no_card.png' 
                self.ids.game_lang_card_stat.text = 'You do not have any cards yet, \ntry rolling a new card'
            
            # roll butt
            if self.player.energy < 300:
                self.ids.roll_butt.disabled = True
            else:
                self.ids.roll_butt.disabled = False

            # player stat
            self.ids.play_stat_window.text = '[b][size=20]' + self.player.username + '[/size][/b]' + '\n\n[size=13]Level: ' + str(self.player.lvl) + '\nExp: ' +  str(self.player.exp) + '\nEnergy: ' + str(self.player.energy) + '\nProficiency: ' + str(self.player.pp) + '\nFame: x' + str(self.player.fame)  + '[/size]'                                             
            

        # updating skill screen
        if gr.current == 'skill_screen':
            try:
                k = skill_lst[self.tempID2]
                self.ids.skill_card_img.source = 'resc/images/' + k.img_name
                self.ids.skill_card_stat.text = 'Name: ' + k.name + '\nFame: ' + str(k.skill_fame) + '\nCost: ' + str(k.cost)
                if self.tempID2<=0:
                    self.ids.skill_prev_butt.disabled = True
                else:
                    self.ids.skill_prev_butt.disabled = False
                if self.tempID2>=len(skill_lst)-1:
                    self.ids.skill_next_butt.disabled = True
                else: 
                    self.ids.skill_next_butt.disabled = False
                if self.player.skill_exists(self.tempID2) or self.player.pp<k.cost:
                    self.ids.buy_skill_butt.disabled = True
                else:
                    self.ids.buy_skill_butt.disabled = False 
            except:
                if self.tempID2 < 0:
                    self.tempID2 = 0
                elif self.tempID2 >= len(skill_lst):
                    self.tempID2 = len(skill_lst) - 1         


        # updating quiz screen
        if gr.current == 'quiz_screen':
            if self.tmr_left <= 1:
                gr.current = 'result_screen'
                self.set_result()
                self.ids.quiz_timer.text = ''
            else:
                self.tmr_left -= (t-self.last_tmr_rec)
                self.last_tmr_rec = t
                if self.tmr_left < 10:
                    self.ids.quiz_timer.color = [1,0,0,1]
                else:
                    self.ids.quiz_timer.color = [1,1,1,1]
                self.ids.quiz_timer.text = str(math.floor(self.tmr_left))




        # updating player_data file
        try:
            player_data = open('player_data.bin','wb')
            pickle.dump(self.player,player_data)
            player_data.close()
        except:
            pass
            # print('missed')

        



        # end of update func
        
    

    def dly_reset(self):
        self.player.dly_time_left = self.player.dly_cd
        self.player.dly_last_time_rec = time.time()
    
    def qz_reset(self):
        self.player.qz_time_left = self.player.qz_cd
        self.player.qz_last_time_rec = time.time()



    def roll(self):
        self.newID = self.player.rng()
        # print(self.newID)
        if self.player.lang_exists(self.newID):
            self.ids.burn_butt.disabled = False
            self.ids.keep_butt.disabled = False
            self.ids.rolled_to_game.disabled = True
            self.ids.rolled_card_label.text = 'You already have this card'
        else:
            self.lvl_up_snd.play()
            self.ids.keep_butt.disabled = True
            self.ids.burn_butt.disabled = True
            self.ids.rolled_to_game.disabled = False
            self.ids.rolled_card_label.text = 'Yay! you got a new card'
            self.player.add(self.newID)
            self.player.energy -= 300
        k = lang_lst[self.newID]
        self.ids.rolled_card_img.source = 'resc/images/' + k.img_name
        self.ids.rolled_card_stat.text = 'Name: ' + k.name + '\nLevel: ' + str(k.card_lvl) + '\nExp: +' + str(k.card_exp) + '\nProficiency: ' + str(k.card_pp)


    def set_que(self):
        self.que = self.player.take_quiz()
        self.ids.que_label.text = self.que.ques
        self.ids.opt1.text = self.que.opt[0]
        self.ids.opt2.text = self.que.opt[1]
        self.ids.opt3.text = self.que.opt[2]
        self.ids.opt4.text = self.que.opt[3]
        self.last_tmr_rec = time.time()

    def set_result(self,f=-1):
        if f==1:
            self.success_snd.play()
            self.ids.result_label.text = 'Correct Answer\nYou got ' + str(math.floor(200*(1+self.player.fame))) + ' energy'
            self.ids.result_label.color = [0,1,0,1]
            self.player.quiz_reward()
        elif f==0:
            self.wrong_snd.play()
            self.ids.result_label.text = 'Wrong Answer'
            self.ids.result_label.color = [1,0,0,1]
        else:
            self.wrong_snd.play()
            self.ids.result_label.text = 'Took too much time'
            self.ids.result_label.color = [1,0,0,1]
        self.tmr_left = self.tmr


    # def clicked(self):
    #     if self.clik_snd:
            # self.clik_snd.play()
        # self.player.clicks = (self.player.clicks+1)%20
        # if self.player.clicks%2==0:
        #     self.ids.butt1.background_normal = 'resc/images/groot.png'
        #     self.ids.butt1.text = 'i am groot'
        # else:
        #     self.ids.butt1.background_normal = 'resc/images/dio.png'
        #     self.ids.butt1.text = 'dio da'

        

class main(App):
    def build(self):
        global gr
        gr = groot()
        self.icon = 'resc/images/dio.png'
        return gr

if __name__ == '__main__':
    main().run()

# well yeh file me bas kuch aur functions and update file thoda bada hoga bas cuz player object ke bhot saare attributes honge...currency, list of acquired card objects, exp...and stuff
# game functionalities in game.py file inside player class...
