

class Point:

    def __init__(self,x,y):
        self.__x = x 
        self.__y =y 

    @property
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    
point1 = Point(2,3)

print(point1.get_x)

