# mcqexam
A simple python package which containing important functionalities to create a simple MCQ questionaire.

To use this simply import mcqexam from createTests.py

```
from createTests import mcqexam
```
Define TeX filename which will be generated and the name of the test.

``` 
filename = "test-1.tex"
testname = "Test-1: Calculus-I"
```
Now simply initialize mcqexam with these parameters.

```
exam = mcqexam(filename, testname)
```
You are now ready to add questions, answers and solutions to your test.
```
exam.add_question("What is the value of $\\int_0^1 x^2 dx$?")
optns = [r"$\displaystyle\frac{1}{2}$", r"$\displaystyle\frac{1}{3}$", 
         r"$\displaystyle\frac{1}{4}$", r"$\displaystyle\frac{1}{5}$"]
exam.add_options(optns)
exam.add_answer([2])
exam.add_solution(r"Solution is $\displaystyle\frac{1}{3}$")
```
At this point note that answers are added as a list of numbers starting 
from 1 (not 0). This is done so that we can have more than one correct
options for the test. Along with this ``add_options`` command has another
option which you can use to put options in certain number of columns. 
Default number of columns is 4, but it can be changed (presumbly) to any
number.
```
exam.add_question("What is the value of $\\int_0^1 x^4 dx$?")
optns = [r"$\displaystyle\frac{1}{5}$", r"$\displaystyle\frac{1}{3}$", 
         r"$\displaystyle\frac{1}{3}$", r"$\displaystyle\frac{1}{5}$"]
exam.add_options(optns, 2)
exam.add_answer([1,4])
exam.add_solution(r"Solution is $\displaystyle\frac{1}{5}$")
```
You can also have number of options different which are not divisible 
by column number for the options.
```
exam.add_question("What is the value of $\\int_0^1 x^5 dx$?")
optns = [r"$\displaystyle\frac{1}{5}$", r"$\displaystyle\frac{1}{2}$", 
         r"$\displaystyle\frac{1}{3}$", r"$\displaystyle\frac{1}{4}$",
         r"$\displaystyle\frac{1}{6}$"]
exam.add_options(optns)
exam.add_answer([5])
exam.add_solution(r"Solution is $\displaystyle\frac{1}{6}$")
```

You can look at the output in the ``test-1.pdf``.
