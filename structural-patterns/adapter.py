class Korean:
    """Korean speaker"""

    def __init__(self):
        self.name = "Korean"

    @staticmethod
    def speak_korean():
        return "An-neyong"

class British:
    """English speaker"""

    def __init__(self):
        self.name = "British"

    @staticmethod
    def speak_english():
        return "Hello"

class Adapter:
    """Changes the generic method name to the individualised method name"""

    def __init__(self, object, **adapted_method):
        """Changing the method name"""

        self._object = object

        # Adding a new dictionary item that establishes mapping
        # ie speak() to speak_korean()
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of the attributes"""

        return getattr(self._object, attr)

# List to store speaker objects
objects = []

# Creating a Korean object
korean = Korean()

# Creating a British object
british = British()

# Appending the objects to the objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))
