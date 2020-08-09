"""Implementing a Extremal binary matrices csp problem."""
from csp.Csp import Csp


class EbmCsp(Csp):
    """Implementing a Extreme Binary Matrices CSP problem.

    All the generic methods makes a csp able to be solved by the CSP solver.
    """

    def __init__(self, grid, domain):
        """Object creator."""
        self.assignment = grid
        self.vars_to_assign = self.vars_to_assign()
        self.domain = domain
        super().__init__()

    # Implementing abstract methods.

    def vars_to_assign(self):
        """Create a list with all non-assigned variables."""
        return [(i, j) for i in range(len(self.assignment))
                for j in range(len(self.assignment[i]))
                if (self.assignment[(i, j)] == b'.')]

    def is_solved(self):
        """Check if the full assignment is valid."""
        for i in range(len(self.assignment)):
            for j in range(len(self.assignment[i])):
                if(not self.is_valid_assignment((i, j))):
                    return False
        return True

    def is_valid_assignment(self, point):
        """Check if the assignment is valid according to a position."""
        i = 1
        while(i <= self.max_square_size(point)):
            if(self.check_square(point, i)):
                return False
            i += 1
        return True

    def select_unassigned_variable(self):
        """Select a unassigned variable to be assigned."""
        return self.vars_to_assign.pop()

    def unassign_variable(self, var):
        """Select a unassigned variable to be assigned."""
        return self.vars_to_assign.insert(0, var)

    def order_domain_value(self):
        """Order the domain values to the problem."""
        return self.domain

    def is_complete(self):
        """Check if the assignment is complete."""
        return len(self.vars_to_assign) == 0

    def add_value(self, var, value):
        """Check if the assignment is complete."""
        self.assignment[(var)] = value

    def remove_value(self, var):
        """Check if the assignment is complete."""
        self.assignment[(var)] = b'.'

    # Implementing the problem specific methods.

    def max_square_size(self, point):
        """Return the max length of the squares for a given point."""
        mid_point = int(len(self.assignment) / 2)
        return (mid_point + min(abs(point[0] - mid_point),
                abs(point[1] - mid_point)))

    def check_square(self, point, square_size):
        """Check if has an invalid square in the assignment."""
        corner_1 = point
        i, j = point
        # up-left corner.
        corner_2 = (i, j + square_size)
        corner_3 = (i + square_size, j)
        corner_4 = (i + square_size, j + square_size)
        if(self.is_square((corner_1, corner_2, corner_3, corner_4)) and
           self.assignment[corner_1] == self.assignment[corner_2] and
           self.assignment[corner_1] == self.assignment[corner_3] and
           self.assignment[corner_1] == self.assignment[corner_4]):
            return True
        # up-right corner.
        corner_2 = (i, j - square_size)
        corner_3 = (i + square_size, j - square_size)
        corner_4 = (i + square_size, j)
        if(self.is_square((corner_1, corner_2, corner_3, corner_4)) and
           self.assignment[corner_1] == self.assignment[corner_2] and
           self.assignment[corner_1] == self.assignment[corner_3] and
           self.assignment[corner_1] == self.assignment[corner_4]):
            return True
        # down-left corner.
        corner_2 = (i - square_size, j)
        corner_3 = (i - square_size, j + square_size)
        corner_4 = (i, j + square_size)
        if(self.is_square((corner_1, corner_2, corner_3, corner_4)) and
           self.assignment[corner_1] == self.assignment[corner_2] and
           self.assignment[corner_1] == self.assignment[corner_3] and
           self.assignment[corner_1] == self.assignment[corner_4]):
            return True    # down-right corner.
        corner_2 = (i, j - square_size)
        corner_3 = (i - square_size, j - square_size)
        corner_4 = (i - square_size, j)
        if(self.is_square((corner_1, corner_2, corner_3, corner_4)) and
           self.assignment[corner_1] == self.assignment[corner_2] and
           self.assignment[corner_1] == self.assignment[corner_3] and
           self.assignment[corner_1] == self.assignment[corner_4]):
            return True
        return False

    def is_square(self, square):
        """Return if it is a valid square in the assignment grid."""
        point1, point2, point3, point4 = square
        return(self.is_valid_point(point1) and
               self.is_valid_point(point2) and
               self.is_valid_point(point3) and
               self.is_valid_point(point4))

    def is_valid_point(self, point):
        """Return if it is a valid point in the assignment grid."""
        i, j = point
        limit = len(self.assignment)
        return(i >= 0 and j >= 0 and i < limit and j < limit)


