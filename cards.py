# a dictionary with key as id and value as the card object
# the id and img file name would be one of the attributes of the object of that card class

class lang:
    def __init__(self,*args):
        self.card_lvl = 1
        self.name = args[0]
        self.img_name = args[1]
        self.card_exp = args[2]
        self.card_pp = args[3]
        # self.total_power = arg[0]
        # self.atrribute1 = arg[1]
        # self.attribute2 = arg[2]
        # and so on other attributes 
        # self.


        # iske bhi kya kya stats hone chayiye player stats ka decide krne ke baad pata chale
class skill:
    def __init__(self,*args):
        self.bought = False
        self.name = args[0]
        self.img_name = args[1]
        self.skill_fame = args[2]
        self.cost = args[3]

          
# higher the tier higher the rarity...like we could select top 5 to 10 langs as high tier cards 
# and rest normal cards like ruby, scala, php...bleh kon suna hai unke baare me...idk
# bhot kuch info nikalna padega...
lang_lst = [
    lang('lang_name','dio.png',20,50)
    
    # and so on...
]


skill_lst = [
    skill('skill_name','skill_name.png',0.5,100)

    # and so on...
]
