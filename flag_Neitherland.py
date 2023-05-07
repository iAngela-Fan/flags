def tri_flag(c1,c2,c3):
    a=[c1,c2,c3]
    for i in range(3):
       t.up()
       t.goto(200,100-200*i/3)
       t.down()
       t.color(a[i])
       t.begin_fill()
       for j in range(2):
            t.right(90)
            t.forward(200/3)
            t.right(90)
            t.forward(400)
       t.end_fill()
    
import turtle as t
t.clear()
t.reset()
t.Pen()
t.pensize(4)
tri_flag('red','white','blue')
t.done()