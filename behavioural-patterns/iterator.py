def count_to(count):
    """Iterator Implementation"""

    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # built-in iterator
    # Creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    for position, number in iterator:
        # Returns a 'generator' containing numbers in German
        yield  number

# Testing the generator
for num in count_to(3):
    print("{}".format(num))
