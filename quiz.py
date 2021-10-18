
class quest:
    def __init__(self,que,opt,ans):
        self.ques = que
        self.opt = opt
        self.ans = ans

que_lst = [
    quest('What is the only thing that computers understand?',['Machine Code','Low Level Languages','High Level Languages','Algorithms'],1),
    quest('A language that requires no knowledge of the hardware or instruction set of the computer is called?',['Machine Code','Low Level Language','High Level Language','An Algorithm'],3),
    quest('When writing a computer program, most programmers use...',['High Level Language','Low Level Languages','Machine Code','Algorithms'],1),
    quest('A list of instructions that enable a computer to perform a specific task is a...',['Computer Program','Algorithm','Machine Code','Binary'],1),
    quest('Before a computer can understand a program it must be...',['Translated into a high level language','Translated into its machine code','Translated into a low level language'],2),
    quest('Languages that relate to the architecture and hardware of a specific computer are known as...',['High Level Language','Low Level Languages','Simplex Languages','Complex Languages'],2),
    quest('Which of the following is not a high programming language',['Assembly','C++','Java','Python'],1),
    quest('Resolving errors in a program is known as',['Problem Solving','Refixing','Error Checking','Debugging'],4),
    quest('A language that is close to human language and which is very easy to write, debug and maintain is known as...',['Machine Code','Low Level Language','High Level Language','Algorithm'],3),
    quest('Which of the following command would not be found in an assembly language',['LOAD','STORE','ADD','SORT'],4)
]
