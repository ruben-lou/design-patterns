class Borg:
    """The Borg design pattern"""


    _shared_data = {}  # Attribute Dictionary

    def __init__(self):
        self.__dict__ = self._shared_data

class Singleton(Borg):
    """The singleton class"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)  # Update the attribute dictionary

    def __str__(self):
        return str(self._shared_data)  # Returns the attribute dictionary

# Creating a singleton object
x = Singleton(HTTP = "Hyper Text Transfer Protocol")

# Printing the object
print(x)

# Creating another singleton object and printing it
y = Singleton(SNMP = "Simple Network Management Protocol")
print(y)
