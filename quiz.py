
class quest:
    def __init__(self,que,opt,ans):
        self.ques = que
        self.opt = opt
        self.ans = ans

que_lst = [
    quest('first question',['opt1','opt2','opt3','opt4'],2),
    quest('second question',['opt1','opt2','opt3','opt4'],1),
    quest('third question',['opt1','opt2','opt3','opt4'],3),
    quest('fourth question',['opt1','opt2','opt3','opt4'],4),
    quest('fifth question',['opt1','opt2','opt3','opt4'],4),
    quest('sixth question',['opt1','opt2','opt3','opt4'],1)
]
