#testing shapes with turtle

from turtle import *
color('red','yellow')
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()