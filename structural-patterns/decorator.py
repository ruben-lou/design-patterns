from functools import wraps

def make_blink(function):
    """Defines the decorator"""

    # Makes the decorator transparent in terms of its name and docstring
    @wraps(function)

    # Defining the inner function
    def decorator():
        # Grabbing the return value of the function being decorated
        ret = function()

        # Adding new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator

# Applying the decorator
@make_blink
def hello_world():
    """Original Function"""

    return "Hello, World!"

# Checking the decorator result
print(hello_world())

# Checking if function name is still the same
print(hello_world.__name__)

# Checking if docstring is still the same
print(hello_world.__doc__)
