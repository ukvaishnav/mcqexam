import numpy as np

preamble = r"\documentclass[a4paper, 12pt]{article}"
preamble += "\n"
preamble += r"\usepackage[lmargin=2cm, rmargin=2cm, tmargin=2cm, bmargin=1cm]{geometry}"
preamble += "\n"
preamble += r"\usepackage{graphicx, amsmath, amsfonts, amssymb, tikz}"
preamble += "\n"
preamble += r"\usepackage{tabularx, intcalc, ifthen, endnotes}"
preamble += "\n"
preamble += r"\usepackage{etoolbox}"
preamble += "\n"
preamble += r"\newcounter{optncols}"
preamble += "\n\n"

class mcqexam:
    def __init__(self, fname, title) -> None:
        self.qnum = 0
        self.fname = fname
        self.questions = []
        self.options = []
        self.answers = []
        self.solutions = []
        self.title = title
    
    def add_question(self, qtext):
        '''
        This method adds question to the list of questions.
        '''
        self.qnum += 1
        temp = ""
        temp += r"\noindent\textbf{" + str(self.qnum) + ".}~"
        temp += qtext + "\n" + r"\\"
        self.questions.append(temp)
        
    def add_options(self, options, optncols=4):
        '''
        This method creates list of options given columns for options.'''
        temp = ""
        temp += r"\begin{tabularx}{0.9\linewidth}{ *{" + str(optncols) + "}{X} }"
        temp += "\n"
        j = 0
        
        for i in range(len(options)):
            j += 1 # this keeps track of column number
            temp += r"\vspace{0.1cm}"
            temp += r"(" + chr(65+i) + ")~" + options[i]
            
            if j == optncols: # this checks if option has reached last column 
                if  i < len(options)-1:
                    # and it has not reached the end of option-list
                    temp += r"\\"
                temp += "\n"
                j = 0
            else:
                temp += "&"
        
        temp += (len(options)%optncols - j - 1)*"&"
         
        temp += r"\end{tabularx}"
        temp += r"\vspace{0.1cm}"
        
        self.options.append(temp)

    def add_answer(self, atext):
        self.answers.append(atext)
    
    def add_solution(self, stext):
        self.solutions.append(stext)
    
    def write(self):
        global preamble
        data_f = open(file=self.fname, mode='w')
        data_f.write(preamble)
        data_f.write(r"\begin{document}")
        data_f.write("\n\n")
        data_f.write(r"\begin{center}\textbf{" + self.title + "}\end{center}")
        data_f.write(r"\hrule\vspace{0.5cm}")
        
        for i in range(self.qnum):
            data_f.write(self.questions[i])
            data_f.write("\n")
            data_f.write(self.options[i])
            data_f.write("\n")
            data_f.write(r"\vspace{0.1cm}")
            data_f.write("\n\n")
        
        data_f.write(r"\vspace{0.5cm}\hrule\vspace{0.1cm}")
        
        # Now we add answers
        data_f.write(r"\begin{center}\textbf{Answers}\end{center}")
        
        for i in range(self.qnum):
            data_f.write(str(i+1) + ".~")
            for j in range(len(self.answers[i])):
                data_f.write( "(" + chr(64+self.answers[i][j]) + ")~" )
            
            data_f.write(r"\qquad"+"\n")
            
        # Finally we add solutions
        
        data_f.write(r"\vspace{0.5cm}\hrule\vspace{0.1cm}")
        data_f.write(r"\begin{center}\textbf{Solutions}\end{center}")
        
        for i in range(self.qnum):
            data_f.write(r"\noindent" + str(i+1) + ".~")
            data_f.write(self.solutions[i] + r"\vspace{0.5cm}\\")
        
        data_f.write(r"\end{document}")
        data_f.close()
    
    def get_option(self, o):
        return chr(65+o)
    