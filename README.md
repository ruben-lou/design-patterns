# Design Patterns

Design Patterns (DPs) are well-known solutions to recurring problems. This is an exploration these DPs.

DP characteristics:
- language neutral 
- dynamic
- incomplete by design to promote customisation

## Creational Patterns

Creational DPs are designed to deal with object creation. They help increase flexibility and reusability of existing code.


### Factory Method 

Provides an interface for creating objects in a superclass while allowing subclasses to alter the type of objects.

Application:
- When you don’t know beforehand the exact types and dependencies of the objects your code should work with.
- When you want to provide users of your library or framework with a way to extend its internal components.
- When you want to save system resources by reusing existing objects instead of rebuilding them each time.


### Abstract Factory 

Allows the production of related objects without specifying their concrete classes.

Application:
- When your code needs to work with various families of related products, but you don’t want it to depend on the concrete classes of those products—they might be unknown beforehand or you simply want to allow for future extensibility.


### Singleton 

Ensures that a class has only one instance, while providing a global access point to that instance.

Application:
- When a class in your program should have just a single instance available to all clients; for example, a single database object shared by different parts of the program.
- When you need stricter control over global variables.


### Builder

Constructs complex objects step by step, allowing you to produce different types and representations of an object using the same construction code.

Application:
- When you want to get rid of a “telescopic constructor”.
- When you want your code to be able to create different representations of some product (for example, stone and wooden houses)
- When you want to construct Composite trees or other complex objects.


### Prototype 

It allows you to copy existing objects without making your code dependent on their classes.

Application:
- When your code shouldn’t depend on the concrete classes of objects that you need to copy.
- When you want to reduce the number of subclasses that only differ in the way they initialize their respective objects. Somebody could have created these subclasses to be able to create objects with a specific configuration.

## Structural Patterns

Structural DPs explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.

### Decorator

Allows you to attach new behaviours to objects, by placing these objects inside special wrapper objects that contain behaviours 

Application:
- When you need to be able to assign extra behaviours to objects at runtime without breaking the code that uses these objects.
- When it’s awkward or not possible to extend an object’s behaviour using inheritance.


### Proxy

Provides a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

Application:
- When you have a heavyweight service object that wastes system resources by being always up, even though you only need it from time to time. Lazy initialization (virtual proxy).
- When you want only specific clients to be able to use the service object; for instance, when your objects are crucial parts of an operating system and clients have various launched applications (including malicious ones). Access control (protection proxy).
- When the service object is located on a remote server. Local execution of a remote service (remote proxy).
- When you want to keep a history of requests to the service object. Logging requests (logging proxy). 
- When you need to cache results of client requests and manage the life cycle of this cache, especially if results are quite large. Caching request results (caching proxy).
- When you need to be able to dismiss a heavyweight object once there are no clients that use it. Smart reference.


### Adapter

Allows objects with incompatible interfaces to collaborate.

Application:
- When you want to use some existing class, but its interface isn’t compatible with the rest of your code.
- When you want to reuse several existing subclasses that lack some common functionality that can’t be added to the superclass.


### Composite 

Composes objects into tree structures and then works with these structures as if they were individual objects.

Application:
- When you have to implement a tree-like object structure.
- When you want the client code to treat both simple and complex elements uniformly.


### Bridge

Splits a large class or a set of closely related classes into two separate hierarchies - abstraction and implementation - which can be developed independently of each other.

Application:
- When you want to divide and organise a monolithic class that has several variants of some functionality (for example, if the class can work with various database servers).
- When you need to extend a class in several orthogonal (independent) dimensions.
- When you need to be able to switch implementations at runtime.


## Behavioural Patterns

Behavioural DPs are concerned with algorithms and the assignment of responsibilities between objects.

### Observer 

Defines a subscription mechanism to notify multiple objects about any events that happen to the objects they're observing.

Application:
- When changes to the state of one object may require changing other objects, and the actual set of objects is unknown beforehand or changes dynamically.
- When some objects in your app must observe others, but only for a limited time or in specific cases.


### Visitor 

Separates algorithms from the objects on which they operate.

Application: 
- When you need to perform an operation on all elements of a complex object structure (for example, an object tree).
- When you need to clean up the business logic of auxiliary behaviours. 
- When a behaviour makes sense only in some classes of a class hierarchy, but not in others.


### Iterator 

Traverses elements of a collection without exposing its underlying representation (list, stack, tree and so on)

Application:
- When your collection has a complex data structure under the hood, but you want to hide its complexity from clients (either for convenience or security reasons).
- When you want to reduce duplication of the traversal code across your app.
- When you want your code to be able to traverse different data structures or when types of these structures are unknown beforehand.


### Strategy 

Defines a family of algorithms: puts each of them into separate classes and makes their objects interchangeable.

Application:
- When you want to use different variants of an algorithm within an object and be able to switch from one algorithm to another during runtime.
- When you have a lot of similar classes that only differ in the way they execute some behaviour.
- When you want to isolate the business logic of a class from the implementation details of algorithms that may not be as important in the context of that logic.
- When your class has a massive conditional operator that switches between different variants of the same algorithm.


### Chain of Responsibility 

Passes requests along a chain of handlers and upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

Application:
- When your program is expected to process different kinds of requests in various ways, but the exact types of requests and their sequences are unknown beforehand.
- When it’s essential to execute several handlers in a particular order.
- When the set of handlers and their order are supposed to change at runtime.


## Sources 

https://refactoring.guru/design-patterns

https://www.linkedin.com/learning/python-design-patterns-14304845/
