import time

class Producer:
    """Define the 'resource-intensive' object to instantiate"""

    @staticmethod
    def produce():
        print("Producer is working hard!")

    @staticmethod
    def meet():
        print("Producer has time to meet you now!")

class Proxy:
    """Define the relatively less resource-intensive proxy"""

    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if Producer is available"""

        print("Artist checking if Producer is available...")

        if self.occupied == 'No':
            # If the producer is available, create a Producer object
            self.producer = Producer()
            time.sleep(2)

            # Make the Producer meet the guest
            self.producer.meet()

        else:
            # Otherwise, don't instantiate a Producer
            time.sleep(2)
            print("Producer is busy!")

# Instantiating a Proxy
proxy = Proxy()

# Making the proxy: Artist produces until Producer is available
proxy.produce()

# Change the state to 'occupied'
proxy.occupied = 'Yes'

# Making the Producer produce
proxy.produce()
