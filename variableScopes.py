"""
Define a couple different types of variables in terms of their scope.
"""

import wedFuncRetBellRinger

# Global Variable - 
global_var = "I am a global variable and I am accessible everywhere."
name = "David"
# I cannot use enclosing_var inside the function

def outer_function():
    # Enclosing scope variable
    enclosing_var = "I am an enclosing variable accessible to nested functions."

    def inner_function(): # Nested Function
        # Local variables
        local_var = "I am a local variable and only accessible in this function."

        """
        local_var is only available inside of the inner_function Namespace

        enclosing_var is available inside of the outer_function Namespace and the inner_function Namespace

        global_var is available everywhere in all of the namespaces created inside of this script. It would also be available inside of any script that imports the variableScopes.py
        """
result = print(result)