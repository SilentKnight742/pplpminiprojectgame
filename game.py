import copy
import math
import random
import time

from cards import *
from quiz import *


class Player:
    def __init__(self):
        self.username = ''

        self.exp = 0
        self.energy = 500
        self.pp = 0
        self.fame = 0.0
        self.lvl = 1

        self.langs = {5:lang('dio da','dio.png',20,50), 2:lang('i am groot','groot.png',30,40)}
        self.lang_ind = [5,2]
        self.skills = {}
        self.skill_ind = []

        self.qz_cd = 5
        self.qz_time_left = 0
        self.qz_last_time_rec = time.time()
        # qz_time_left = qz_time_left - (time.time() - last_time_rec)
        # if qz_time_left <= 0 then quiz is ready otherwise ded
        self.dly_cd = 2
        self.dly_time_left = 0
        self.dly_last_time_rec = time.time()
        # same logic as qz_cd

    
    # yaha pe game functionalities
    # i is the id of lang card to acess it from lang_lst
    def rng(self):
        self.energy -= 300
        # if 1 == random.choices((1,2),weights=(30,70)):
        #     return random.randint(0,4)
        # else:
        #     return random.randint(5,28)
        return 0

    def lang_exists(self,i):
        return True if i in self.langs.keys() else False

    def burn(self,i):
        self.pp += lang_lst[i].card_pp

    # lvl up an already exiting card using its dup
    def lvl_up_card(self,i):
        self.langs[i].card_lvl += 1
        k = math.floor(self.langs[i].card_exp*self.langs[i].card_lvl/(self.langs[i].card_lvl-1))
        self.langs[i].card_exp += k
        self.exp += k

    def add(self,i):
        self.langs[i] = copy.deepcopy(lang_lst[i])
        self.lang_ind.append(i)
        self.exp += self.langs[i].card_exp

    def buy_skill(self,i):
        self.skills[i] = copy.deepcopy(skill_lst[i])
        self.skill_ind.append(i)
        self.fame += self.skills[i].skill_fame
        self.pp -= self.skills[i].cost

    def skill_exists(self,i):
        return True if i in self.skills.keys() else False

    def take_quiz(self):
        return que_lst[random.randint(1,49)]
    
    def quiz_reward(self):
        self.energy += math.floor(200*(1+self.fame))
    
    def dly_reward(self):
        self.energy += math.floor(1000*(1+self.fame))
        
