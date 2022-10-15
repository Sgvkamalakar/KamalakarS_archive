import math
from math import sqrt
class Rectangle:
    def __init__(s,width,height):
        s.width=width
        s.height=height
    def set_width(s,width):
       s.width=width
    def set_height(s,height):
       s.height=height
    def get_area(s):
        return s.width*s.height
    def get_perimeter(s):
        return 2*(s.width+s.height)
    def get_diagonal(s):
        return sqrt(s.width**2+s.height**2)
    def get_picture(s):
        if s.width>50 or s.height>50:
            print('Too big')
        else:
            for _ in range(s.width):
                for i in range(s.height):
                    print("*",end=" ")
                print(" ")
class Square:
  def __init__(sq,side):
    sq.side=side
  def set_side(sq,side):
    sq.side=side
  def get_area(sq):
    return sq.side**2
  def get_perimeter(sq):
    return 4*sq.side
  def get_picture(sq):
    if sq.side>50:
      print('Too big')
    else:
      for _ in range(sq.side):
        for i in range(sq.side):
          print('*',end=" ")
        print(" ")  
if __name__=="__main__":
    rect = Rectangle(5, 10)
    print('Width=',rect.width,"Height=",rect.height)
    print('Area:',rect.get_area())
    print('Perimeter:',rect.get_perimeter())
    print('Diagonal:',rect.get_diagonal())
    rect.get_picture()
    rect.set_width(3)
    print('Width=',rect.width,"Height=",rect.height)
    print('Area:',rect.get_area())
    print('Perimeter:',rect.get_perimeter())
    print('Diagonal:',rect.get_diagonal())
    rect.get_picture()
    squ=Square(4)
    print('Side=',squ.side)
    print('Area:',squ.get_area())
    print('Perimeter:',squ.get_perimeter())
    squ.get_picture()
    squ.set_side(3)
    print('Side=',squ.side)
    print('Area:',squ.get_area())
    print('Perimeter:',squ.get_perimeter())
    squ.get_picture()
