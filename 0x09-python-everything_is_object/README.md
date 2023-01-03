# python everything is object; 
Unlike in C where items were either passed by 
value or by reference, in python every variable is like a label that is
referencing an object in memory. 

We then have mutable and immutable objects which in its basic form refers to
whether or not an object can be changed while still retaining its initial
identity checked with id() or the keyword 'is'

# Some mutable objects in python are;
    - list
    - dictionaries
    - set
    - bytearray
    - user defined classes

# Some immutable objects in python;
    - int 
    - float
    - decimal
    - complex
    - bool
    - string
    - tuple
    - range
    - frozen set
    - bytes

object types like tuples are immutable but if they contain mutable objects
within them like a list, that list which is a mutable object can be changed
despite the fact that it is inside a tuple, just something to take note of.

This dir focuses on the importance of the behaviour of objects in python
based on their mutability or immutability
