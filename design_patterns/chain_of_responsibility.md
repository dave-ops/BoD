# The Chain of Responsibility Pattern 
this is a behavioral design pattern that allows you to pass requests along a chain of handlers. Each handler decides either to process the request or to pass it to the next handler in the chain. This pattern promotes loose coupling between the sender and receiver of a request.

Let's implement the Chain of Responsibility pattern in Python with a concrete example of a purchase approval system.

```python
from abc import ABC, abstractmethod

class PurchaseRequest:
    def __init__(self, amount):
        self.amount = amount

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass

class AbstractHandler(Handler):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class Manager(AbstractHandler):
    def handle(self, request):
        if request.amount <= 1000:
            return f"Manager approved purchase of ${request.amount}"
        return super().handle(request)

class Director(AbstractHandler):
    def handle(self, request):
        if request.amount <= 10000:
            return f"Director approved purchase of ${request.amount}"
        return super().handle(request)

class VicePresident(AbstractHandler):
    def handle(self, request):
        if request.amount <= 50000:
            return f"Vice President approved purchase of ${request.amount}"
        return super().handle(request)

class President(AbstractHandler):
    def handle(self, request):
        if request.amount <= 100000:
            return f"President approved purchase of ${request.amount}"
        return "Request denied. Amount exceeds company policy."

# Client code
def main():
    # Create the chain of handlers
    manager = Manager()
    director = Director()
    vice_president = VicePresident()
    president = President()

    manager.set_next(director).set_next(vice_president).set_next(president)

    # Test the chain with different purchase amounts
    for amount in [500, 5000, 20000, 75000, 150000]:
        request = PurchaseRequest(amount)
        result = manager.handle(request)
        print(f"Purchase request for ${amount}: {result}")

if __name__ == "__main__":
    main()

```



Let's break down the implementation and explain the Chain of Responsibility pattern:

1. **PurchaseRequest**: This class represents the request being passed through the chain.

2. **Handler**: This is the base interface for all handlers in the chain. It defines the `set_next` and `handle` methods.

3. **AbstractHandler**: This is an abstract base class that implements the `set_next` method and provides a default implementation for the `handle` method. It allows chaining of handlers.

4. **Concrete Handlers (Manager, Director, VicePresident, President)**: These classes implement the `handle` method to process requests within their authority. If they can't handle a request, they pass it to the next handler in the chain.

5. **Client Code**: The `main` function demonstrates how to set up the chain and use it to process different purchase requests.

Key aspects of the Chain of Responsibility pattern:

- **Decoupling**: The sender of a request (in this case, the client code) is decoupled from the receivers (the handlers). The sender doesn't need to know which handler will process the request.

- **Flexibility**: You can easily add new handlers or change the order of handlers in the chain without modifying existing code.

- **Dynamic Chain**: The chain can be constructed at runtime, allowing for flexible configurations.

- **Single Responsibility Principle**: Each handler has a single responsibility (to handle or pass on a request), promoting better organization of code.

This pattern is useful in scenarios where multiple objects may handle a request, and the exact handler is determined at runtime. It's commonly used in scenarios like logging frameworks, event handling systems, and, as shown in this example, approval processes.