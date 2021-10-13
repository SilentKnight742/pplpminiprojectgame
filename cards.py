# a dictionary with key as id and value as the card object
# the id and img file name would be one of the attributes of the object of that card class

class cards:
    def __init__(self,id):
        self.id = id
        # self.total_power = arg[0]
        # self.atrribute1 = arg[1]
        # self.attribute2 = arg[2]
        # and so on other attributes 

class lang(cards):
    def __init__(self,id,*arg):
        super().__init__(id)
        self.name = arg[0]
        # iske bhi kya kya stats hone chayiye player stats ka decide krne ke baad pata chale

# tools and skill cards would boost the lang card attributes ig...    dekhte hai
# class tool(cards):
#     def __init__(self,id,*arg):
#         super().__init__()
#         self.name = arg[1]

# class skill(cards):
#     def __init__(self,id,*arg):
#         super().__init__()
#         self.name = arg[1]

# higher the tier higher the rarity...like we could select top 5 to 10 langs as high tier cards 
# and rest normal cards like ruby, scala, php...bleh kon suna hai unke baare me...idk
# bhot kuch info nikalna padega...
lang_card = {
    1: lang(1,'Python'),
    2: lang(2,'C++')
    # and so on...
}

# tool_card = {
#     1: tool(),
#     2: tool()
#     # and so on...
# }

# skill_card = {
#     1: skill(),
#     2: skill()
#     # and so on...
# }
