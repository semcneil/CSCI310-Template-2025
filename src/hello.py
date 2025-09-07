"""
hello.py
====================================
This is an example file with correct docstring examples

| Author: Seth McNeill
| Date: 2025 September 07
"""

class SayHello:
    """
    Base class example
    
    This class provides an example to work from
    
    Parameters
    ----------
    name : str
        The user's name
    
    Attributes
    ----------
    name : str
        The pet's name
        
    Examples
    --------
    >>> hello = SayHello("Bob")
    >>> hello.greet(', welcome!)
    Hello Bob, welcome!
    """
    
    def __init__(self, name):
        """
        Initialize a new SayHello instance.
        
        Parameters
        ----------
        name : str
            The user's name
        """
        self.name = name
   
    def greet(self, extraText):
        """
        Clamp a stat value between minimum and maximum bounds.
        
        Parameters
        ----------
        extraText : str
            Text to add after the hello username
            
        Returns
        -------
        int
            An integer as an example of returning a value
        """
        print(f'Hello {self.name}{extraText}')
        return len(self.name)


if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library
    """
    bob = SayHello('Bob')
    bobLen = bob.greet(', welcome!')
    print(bobLen)