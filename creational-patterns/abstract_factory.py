class Dog:
    """ One of the objects to be returned """

    @staticmethod
    def speak():
        return "Woof!"

    def __str__(self):
        return "Dog"

class DogFactory:
    """Concrete Factory"""

    @staticmethod
    def get_pet():
        """Returns a Dog object"""
        return Dog()

    @staticmethod
    def get_food():
        """Returns a Dog Food object"""
        return "Dog Food!"

class PetStore:
    """PetStore houses our Abstract Factory"""

    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""

        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))

# Creating a Concrete Factory
factory = DogFactory()

# Creating a pet store housing for the Abstract Factory
shop = PetStore(factory)

# Invoking the utility method to show the details of the pet
shop.show_pet()
