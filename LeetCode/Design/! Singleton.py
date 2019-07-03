"""
Singleton is a most widely used design pattern. If a class has and only has one instance at every moment, we call this design as singleton. For
example, for class Mouse (not a animal mouse), we should design it in singleton.

You job is to implement a getInstance method for given class, return the same instance of this class every time you call this method.

Example
In Java:

A a = A.getInstance();
A b = A.getInstance();
"""

# For interview 
class Solution:
    # @return: The same instance of this class every time
    instance = None

    @classmethod
    def getInstance(cls):
        # write your code here
        if cls.instance is None:
            cls.instance = Solution()

        return cls.instance
    

"""
In practice, a metaclass is mostly widely used. 
Reference: https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python 

Pros:
- It's a true class
- Auto-magically covers inheritance
- Uses __metaclass__ for its proper purpose (and made me aware of it)
"""

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(BaseClass, metaclass=Singleton):
    pass




"""
Implement a thread-safe singleton. 
Reference: https://stackoverflow.com/questions/50566934/why-is-this-singleton-implementation-not-thread-safe 
"""

import functools
import threading

lock = threading.Lock()


def synchronized(lock):
    """ Synchronization decorator """
    def wrapper(f):
        @functools.wraps(f)
        def inner_wrapper(*args, **kw):
            with lock:
                return f(*args, **kw)
        return inner_wrapper
    return wrapper


class Singleton(type):
    _instances = {}

    @synchronized(lock)
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    pass

