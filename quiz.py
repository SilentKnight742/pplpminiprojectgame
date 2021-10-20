
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
    quest('What is an open source, high-level programming language designed to be easy to read and simple to implement?',['Sunmatra','Java','Blocks','Latin'],2),
    quest('An error in your program which prevents it from running properly is...',['Error report','Bug','Mistake','Virus'],2),
    quest('One kilobyte is approximately equal to how many memory locations?',['1000','10000','100','100000'],1),
    quest('Binary uses how many digits?',['1','4','2','8'],3),
    quest('How many bits make up one byte?',['4','8','16','32'],2),
    quest('To focus on the logic and make refinements to a program before translating it into a programming language, a programmer often creates an outline of the program\'s algorithm. What is the term for this type of outline?',['Interpreter','Sketch','Compiler','Pseudocode'],4),
    quest('Which utility software can protect our personal information or identity?',['Antivirus','Spyware Protection','Firewall','Defragmentation'],2),
    quest('Which utility program frees up space on the disk by reorganising it?',['Antivirus','Firewall','System Clean Up','Defragmentation'],4),
    quest('The letter E in binary is?',['01000001','01000101','01000010','01010101'],2),
    quest('Which generation of computer languages used the LOAD, ADD and STORE codes?',['First','Second','Third','Fourth'],2),
    quest('Which generation of computers started in the 1950s?',['First','Second','Third','Fourth'],3),
    quest('Which generation of computer languages includes the SQL(Database Search)?',['First','Second','Third','Fourth'],4),
    quest('Software that is available but has limitations is called?',['Shareware','Freeware','Open Source','Closed Source'],1),
    quest('Software that is restricted on it\'s use or modifications is called?',['Shareware','Freeware','Open Source','Closed Source'],4),
    quest('Which of the following programming language types was created first?',['procedural','machine','object oriented','assembler'],2),
    quest('Software that allows modification in all cases is called?',['Shareware','Freeware','Open Source','Closed Source'],3),
    quest('What does binary code mean?',['a coding system using the digits 0 and 1','a coding system using the digits 0 to 9','1000100100','code.org'],1),
    quest('Why is binary code used?',['harder to hack into','makes computer run faster','since it was the first code ever invented','because...why not?'],2),
    quest('Python is a clear and powerful ... oriented language',['software','snake','object','source'],3),
    quest('What is programming?',['Creating a calendar of events','A way of speaking to aliens and robots','A list of activities','Writing instructions for a digital tool'],4),
    quest('Binary numbers are usually expressed in groups of ... bit(s)',['1','2','8','10'],3)
]
