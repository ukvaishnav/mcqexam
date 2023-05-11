import numpy as np

preamble = r"\documentclass[a4paper, 12pt]{article}"
preamble += "\n"
preamble += r"\usepackage[lmargin=1cm, rmargin=1cm, tmargin=2cm, bmargin=2cm]{geometry}"
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
                temp += "\n&\n"
        
        if len(options)%optncols!=0:
            temp += (optncols - len(options)%optncols - 1)*"&\n"
            
        temp += "\n"
        temp += r"\end{tabularx}"
        
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
        data_f.write(r"\begin{center}\textbf{" + self.title + r"}\end{center}")
        data_f.write("\n" + r"\hrule\vspace{0.5cm}")
        
        for i in range(self.qnum):
            data_f.write(self.questions[i])
            data_f.write("\n")
            data_f.write(self.options[i])
            data_f.write("\n")
            data_f.write(r"\vspace{0.1cm}")
            data_f.write(r"\\" + "\n\n")
        
        data_f.write(r"\vspace{0.5cm}\hrule\vspace{0.1cm}" + "\n")
        
        # Now we add answers
        data_f.write(r"\newpage\begin{center}\textbf{Answers}\end{center}" + "\n")
        anscols = 8
        data_f.write(r"\begin{tabularx}{\linewidth}{ *{"+str(anscols)+"}{X} }" + "\n")
        k = 0
        for i in range(self.qnum):
            k += 1 # changing column count
            data_f.write(str(i+1) + ".~")
            for j in range(len(self.answers[i])):
                data_f.write( "(" + chr(64+self.answers[i][j]) + ")" )
                if j!=len(self.answers[i])-1:
                    data_f.write(",")
            
            if k<anscols:
                data_f.write("\n&\n") # this changes column
            elif k==anscols and i!=self.qnum-1:
                data_f.write(r"\\" + "\n")
                k = 0
        
        if self.qnum%anscols != 0:
            data_f.write((anscols-self.qnum%anscols-1)*"&\n")
        
        data_f.write("\n" + r"\end{tabularx}" + "\n")
        
        # Finally we add solutions
        
        data_f.write("\n" + r"\vspace{0.5cm}\hrule\vspace{0.1cm}" + "\n")
        data_f.write(r"\begin{center}\textbf{Solutions}\end{center}" + "\n")
        
        for i in range(self.qnum):
            data_f.write(r"\noindent " + str(i+1) + ".~")
            data_f.write(self.solutions[i])
            data_f.write(r"\vspace{0.5cm}\\" + "\n")
        
        data_f.write("\n" + r"\end{document}" + "\n")
        data_f.close()
    