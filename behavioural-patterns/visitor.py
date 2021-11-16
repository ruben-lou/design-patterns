class House(object):  # The class being visited

    def accept(self, visitor):
        """Interface to accept a visitor"""

        # Triggers the visiting operation
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)  # Reference to the HVAC specialist object in the house object

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)  # Reference to the electrician object in the house object

    def __str__(self):
        """Return class name when the House object is printed"""
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""

    def __str__(self):
        """Return the class name when the Visitor object is printed"""
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    """Concrete visitor: HVAC specialist"""

    def visit(self, house):
        house.work_on_hvac(self)  # Visitor has a reference to the house object


class Electrician(Visitor):
    """Concrete visitor: electrician"""

    def visit(self, house):
        house.work_on_electricity(self)  # Visitor has a reference to the house object


# Creating a HVAC specialist
hvac = HvacSpecialist()

# Creating an electrician
elec = Electrician()

# Creating house
home = House()

home.accept(hvac)
home.accept(elec)
