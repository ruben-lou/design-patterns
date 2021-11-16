class Handler:
    """Abstract Handler"""

    def __init__(self, successor):
        # Defines who is the next handler
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)  # If handles, stop here

        # Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass')


class ConcreteHandler1(Handler):
    """Concrete Handler 1"""

    def _handle(self, request):
        if 0 < request <= 10:
            print("Request {} handled in handler 1".format(request))
            return True  # indicating that request was handled


class DefaultHandler(Handler):
    """Default Handler"""

    def _handle(self, request):
        """If there is no handler available"""

        print("End of chain, no handler for {}".format(request))
        return True

class Client:

    def __init__(self):
        # Creating handlers and using them in a sequence
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


# Creating Client
client = Client()

# Creating requests
requests = [2, 5, 30]

# Sending the requests
client.delegate(requests)
