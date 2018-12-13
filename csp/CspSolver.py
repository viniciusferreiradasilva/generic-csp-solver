"""ABC representing a generic csp problem."""


class CspSolver():
    """Class implementing methods to solve generic csp problems."""

    def recursive_backtrack(self, csp):
        """Perform a recursive bt search returning True for solved csp."""
        if(csp.is_complete()):  # Checks if the assignment is complete.
            return True
        var = csp.select_unassigned_variable()  # Select an unassigned var.
        for value in csp.order_domain_value():
            csp.add_value(var, value)  # Adds the value in the variable.
            if(csp.is_valid_assignment(var)):
                if(self.recursive_backtrack(csp)):
                    return True
            else:
                csp.remove_value(var)
        csp.unassign_variable(var)
        return False
