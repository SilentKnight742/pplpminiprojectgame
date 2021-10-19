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
    lang('Python','Python.jpg',20,50),
    lang('Javascript','Javascript.jpg',20,50),
    lang('C++','C++.jpg',20,50),
    lang('C','C.jpg',20,50),
    lang('Java','Java.jpg',20,50),
    lang('C#','C#.jpg',20,50),
    lang('R','R.jpg',20,50),
    lang('PHP','PHP.jpg',20,50), 
    lang('SQL','SQL.jpg',20,50),
    lang('Objective C','ObjectiveC.jpg',20,50),
    lang('Typescript','typescript.jpg',20,50),
    lang('Swift','swift.jpg',20,50),
    lang('Kotlin','Kotlin.jpg',20,50),
    lang('Matlab','Matlab.jpg',20,50),
    lang('Go','Go.jpg',20,50),
    lang('Rust','Rust.jpg',20,50),
    lang('VBA','VBA.jpg',20,50),
    lang('Ruby','Ruby.jpg',20,50),
    lang('Scala','Scala.jpg',20,50),
    lang('Ada','Ada.jpg',20,50),
    lang('Visual Basic','VisualBasic.jpg',20,50),
    lang('Dart','Dart.jpg',20,50),
    lang('Lua','Lua.jpg',20,50),
    lang('Cobol','Cobol.jpg',20,50),
    lang('Groovy','Grovy.jpg',20,50),
    lang('Abap','Abap.jpg',20,50),
    lang('Perl','Perl.jpg',20,50),
    lang('Julia','Julia.jpg',20,50),
    lang('Haskell','Haskell.jpg',20,50),
    lang('Pascal','Pascal.jpg',20,50)
]


skill_lst = [
    skill('Programming Languages','programminglanguages.jpg',0.5,100),
    skill('Data Science','datascience2.jpg',0.5,100),
    skill('Digital marketing','digitalmarketing.jpg',0.5,100),
    skill('UI/UX Development','UXUI dev.jpg',0.5,100),
    skill('Cyber Security','cybersec.jpg',0.5,100),
    skill('Project Management','projectmanagement.jpg',0.5,100),
    skill('Open Source Contributions','opensourcecontributions.jpg',0.5,100),
    skill('Software Development','softwaredev.jpg',0.5,100),
    skill('Mathematics','mathematics.jpg',0.5,100),
    skill('Problem Solving','problemsolving.jpg',0.5,100),
    skill('Coding','coding.jpg',0.5,100),
    skill('Experimentation','experimentation1.jpg',0.5,100),
    skill('Computer and technology knowledge','computerandtechnologyknowledge.jpg',0.5,100),
    skill('Computer hardware engineering','computerhardwareengineering.jpg',0.5,100),
    skill('Data analysis','dataanalysis.jpg',0.5,100),
    skill('Information systems management','informationsystemsmanagement.jpg',0.5,100)
]
