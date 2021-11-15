class Subject(object):  # Represents what is being 'observed'

    def __init__(self):
        self._observers = [] # reference to all the observers, a one-to-many relationship

    def attach(self, observer):
        # If the observer is not already in the observer list, append it
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        # Notify all observers in list except for the observer who is actually updating
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name  # Setting up name of core
        self._temp = 0  # Initialising the temperature of a core

    @property  # Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        self._temp = temp
        self.notify()


class TempViewer:

    @staticmethod
    def update(subject):
        print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))


# Creating the subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# Creating the observers
v1 = TempViewer()
v2 = TempViewer()

# Attaching observers to the first core
c1.attach(v1)
c1.attach(v2)

# Changing the temperature of the first core
c1.temp = 80
c1.temp = 90
