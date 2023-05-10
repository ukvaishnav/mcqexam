from createTests import mcqexam

filename = './test-1.tex'
exam = mcqexam(filename, "Test-1: Calculus I")

exam.add_question("What is the value of $\\int_0^1 x^2 dx$?")
optns = [r"$\displaystyle\frac{1}{2}$", r"$\displaystyle\frac{1}{3}$", 
         r"$\displaystyle\frac{1}{4}$", r"$\displaystyle\frac{1}{5}$"]
exam.add_options(optns)
exam.add_answer([2])
exam.add_solution(r"Solution is $\displaystyle\frac{1}{3}$")

exam.add_question("What is the value of $\\int_0^1 x^3 dx$?")
optns = [r"$\displaystyle\frac{1}{4}$", r"$\displaystyle\frac{1}{2}$", 
         r"$\displaystyle\frac{1}{3}$", r"$\displaystyle\frac{1}{5}$"]
exam.add_options(optns)
exam.add_answer([1])
exam.add_solution(r"Solution is $\displaystyle\frac{1}{4}$")

exam.add_question("What is the value of $\\int_0^1 x^4 dx$?")
optns = [r"$\displaystyle\frac{1}{5}$", r"$\displaystyle\frac{1}{3}$", 
         r"$\displaystyle\frac{1}{3}$", r"$\displaystyle\frac{1}{5}$"]
exam.add_options(optns, 2)
exam.add_answer([1,4])
exam.add_solution(r"Solution is $\displaystyle\frac{1}{5}$")

exam.add_question("What is the value of $\\int_0^1 x^5 dx$?")
optns = [r"$\displaystyle\frac{1}{5}$", r"$\displaystyle\frac{1}{2}$", 
         r"$\displaystyle\frac{1}{3}$", r"$\displaystyle\frac{1}{4}$",
         r"$\displaystyle\frac{1}{6}$"]
exam.add_options(optns)
exam.add_answer([5])
exam.add_solution(r"Solution is $\displaystyle\frac{1}{6}$")


exam.write()
