"""ABC representing a generic csp problem."""
from abc import ABC, abstractmethod


class Csp(ABC):
    """ABC representing a generic CSP problem.

    All the generic methods makes a csp able to be solved by the csp solver.
    """

    def __init__(self):
        """Object creator."""
        ABC.__init__(self)

    @abstractmethod
    def is_solved(self):
        """Check if the csp is solved."""
        pass

    @abstractmethod
    def is_valid_assignment(self, var):
        """Check if the value assigned to var is valid."""
        pass

    @abstractmethod
    def select_unassigned_variable(self):
        """Select the next unassigned var to be assigned."""
        pass

    @abstractmethod
    def unassign_variable(self, var):
        """Return back the var to the set of unassigned vars."""
        pass

    @abstractmethod
    def order_domain_value(self):
        """Order the domain values to the problem."""
        pass

    @abstractmethod
    def is_complete(self):
        """Check if the assignment is complete."""
        pass

    @abstractmethod
    def add_value(self, var, value):
        """Check if the assignment is complete."""
        pass

    @abstractmethod
    def remove_value(self, var):
        """Check if the assignment is complete."""
        pass
