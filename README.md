# A generic Python implementation for CSP(Constraint Satisfaction Problem)
The package csp contains two files: Csp.py and CspSolver.py.

The #Csp.py# is an abstract class modeling a Csp that contains all the necessary methods to a CspSolver object to solve it.

You'll have to implement these methods and then use a CspSolver object, that contains backtracking algorithms.

In the files, you have an example of an "Extremal binary matrices problems" implemented as a Csp problem (EbmCsp.py). Some math for this problem can be find in http://www-lmpa.univ-littoral.fr/publications/articles/lmpa404.pdf.

In the main.py file you have an example of how to use the solver.
