from turtle import *
speed(10)
bgcolor('sky blue')
color('red', 'yellow')
begin_fill()
while True:
    forward(100)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
