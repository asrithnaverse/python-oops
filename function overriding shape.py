class Shape:
    def area(self):
        print("Enter the sides")
class circle(Shape):
    def area(self,radius):
        print("Area of circle is: ",3.14*radius*radius)
class Rectangle(Shape):
    def area(self,length,breadth):
        print("Area of the rectangle is: ",length*breadth)
class Triangle(Shape):
    def area(self,base,height):
        print("Area of the triangle is: ",1/2*(base*height) )
cir1=circle()
cir1.area(5)
rect1=Rectangle()
rect1.area(10,5)
tri1=Triangle()
tri1.area(4,8)
shape1=Shape()
shape1.area()
