#!usr/bin/python3
'''create class rectangle'''

class Rectangle:
    '''Empty class'''
    
    def __init__(self, width=0, height=0):
        '''Initialize'''
        self.width = width
        self.height = height
    
    @property
    def width(self):
        '''Getter'''
        return self.__width
    
    @width.setter
    def width(self, value):
        '''setter in width'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
    
    @property
    def height(self):
        '''Getter'''
        return self.__height
    
    @height.setter
    def height(self, value):
        '''setter in height'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''area of rectangle'''
        return self.__width * self.__height
    
    def perimeter(self):
        '''perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        '''print rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join(['#' * self.__width for i in range(self.__height)])
    
    def __repr__(self):
        '''print rectangle'''
        return "Rectangle({}, {})".format(self.__width, self.__height)
        