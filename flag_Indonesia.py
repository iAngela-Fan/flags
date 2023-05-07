'''Indonesia Flag'''
import turtle as t
t.clear()
t.reset()
t.Pen()
t.pensize(4)
t.up()
t.goto(200,100)
t.down()
t.color('red')
t.begin_fill()
for i in range(2):
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(400)
t.end_fill()
t.up()
t.goto(200,0)
t.down()
t.color('black')
for i in range(2):
    t.right(90)
    t.forward(100)
    if i==1:
        break
    t.right(90)
    t.forward(400)
t.done()