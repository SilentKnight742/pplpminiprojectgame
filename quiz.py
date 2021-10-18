
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
    quest('Which of the following command would not be found in an assembly language',['LOAD','STORE','ADD','SORT'],4),
    quest('What is the name for the software used to convert an assembly language program into machine code?',['Translator','Interpreter','Compiler','Assembler'],4),
    quest('Which of the following is not an advantage of using a low level language?',['Makes more efficient use of primary memory.','To enable the program to run on multiple platforms','To perform a task very quickly','Tailor a program to a specific piece of hardware'],2),
    quest('The two categories of low level language are...',['Machine Code and Assembly','Machine Code and Algorithms','Assembly and Algorithms','Algorithms and Binary'],1),
    quest('The high-level programming language that was developed in the mid-1970s that is now used to write applications for nearly every available platform is...',['Scratch','Bark-Bark','Tynker','C++'],4),
    quest('Software that translates and executes a high level language program one line at a time is known as a?',['Compiler','Assembler','Interpreter','Executor'],3),
    quest('Which type of translator creates an executable file of machine code from a program written in a high level language?',['Assembler','Compiler','Interpreter','Executor'],2),
    quest('The 3 main types of translators are...',['Assemblers, Compilers and Interpreters','Assemblers, Compilers and Converters','Assemblers, Scripters and Interpreters','Converters, Scripters and Interpreters'],1),
    quest('Assembly language is...',['A small business meeting','A high level language like java','Used for manufacturing automobiles','a low level machine languge'],4),
    quest('What is the smallest unit of measurement used to quantify computer data?',['a birdle','a marble','a bit','a tablespoon'],3),
    quest('What is an open source, high-level programming language designed to be easy to read and simple to implement?',['Sunmatra','Java','Blocks','Latin'],2)
]
