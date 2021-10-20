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
        self.name = args[0]
        self.img_name = args[1]
        self.skill_fame = args[2]
        self.cost = args[3]

high_ranks = 7  
# higher the tier higher the rarity...like we could select top 5 to 10 langs as high tier cards 
# and rest normal cards like ruby, scala, php...bleh kon suna hai unke baare me...idk
# bhot kuch info nikalna padega...
lang_lst = [
    lang('Python','Python.jpg',60,70),
    lang('Javascript','javascript.jpg',60,70),
    lang('C++','C++.jpg',60,70),
    lang('C','C.jpg',60,70),
    lang('Java','java.jpg',60,70),
    lang('C#','C#.jpg',60,70),
    lang('R','R.jpg',60,70),
    lang('PHP','php.jpg',20,30), 
    lang('SQL','SQL.jpg',20,30),
    lang('Objective C','ObjectiveC.jpg',20,30),
    lang('Swift','Swift.jpg',20,30),
    lang('Kotlin','kotlin.jpg',20,30),
    lang('Matlab','MATLAB.jpg',20,30),
    lang('Go','go.jpg',20,30),
    lang('Rust','rust.jpg',20,30),
    lang('VBA','VBA.jpg',20,30),
    lang('Ruby','Ruby.jpg',20,30),
    lang('Scala','scala.jpg',20,30),
    lang('Ada','ada.jpg',20,30),
    lang('Visual Basic','visualbasic.jpg',20,30),
    lang('Dart','dart.jpg',20,30),
    lang('Lua','lua.jpg',20,30),
    lang('Cobol','cobol.jpg',20,30),
    lang('Groovy','groovy.jpg',20,30),
    lang('Abap','abap.jpg',20,30),
    lang('Julia','Julia.jpg',20,30),
    lang('Haskell','haskell.jpg',20,30),
    lang('Pascal','pascal.jpg',20,30)
]


skill_lst = [
    skill('Computer and technology knowledge','computerandtechnologyknowledge.jpg',0.3,150),
    skill('Digital marketing','digitalmarketing.jpg',0.4,200),
    skill('Computer hardware engineering','computerhardwareengineering.jpg',0.5,250),
    skill('UI/UX Development','UXUI dev.jpg',0.5,250),
    skill('Project Management','projectmanagement.jpg',0.5,250),
    skill('Information systems management','informationsystemsmanagement.jpg',0.5,250),
    skill('Open Source Contributions','opensourcecontributions.jpg',0.6,300),
    skill('Experimentation','experimentation1.jpg',0.6,300),
    skill('Cyber Security','cybersec.jpg',0.7,350),
    skill('Software Development','softwaredev.jpg',0.7,350),
    skill('Problem Solving','problemsolving.jpg',0.7,350),
    skill('Mathematics','mathematics.jpg',0.8,400),
    skill('Data analysis','dataanalysis.jpg',0.9,450),
    skill('Data Science','datascience2.jpg',1,500)
]
