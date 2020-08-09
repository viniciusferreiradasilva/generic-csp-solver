"""Challenge 368 - Single-symbol squares."""
import numpy as np
from EbmCsp import EbmCsp
from csp.CspSolver import CspSolver
"""Implementing intermediate challenge 368 from r/dailyprogrammer using CSP."""


def generate_grid(size):
    """Generate an empty nxn sized grid filled by '.'."""
    grid = np.chararray([size, size])
    grid[:] = b'.'
    return grid

# A simple example.
grid = generate_grid(4)
csp = EbmCsp(grid, ['X', 'O'])
solver = CspSolver()
print("is solved?", solver.recursive_backtrack(csp))
print("assignment:\n", csp.assignment)
