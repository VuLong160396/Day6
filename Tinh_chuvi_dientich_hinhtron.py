import math
import turtle
r = int(input('nhap vao ban kinh: '))
#vẽ đường tròn bán kính đã nhập
t = turtle.Turtle()
t.hideturtle()
t.pensize(1)
t.color("red")
t.circle(r)
turtle.done()
#tính diện tích và chu vi
c = 2*math.pi*r
s = math.pi*r*r
print('chu vi của hình tròn có bán kính {r} là {c}'.format(r=r,c=c))
print('diện tích của hình tròn có bán kính {r} là {s}'.format(r=r,s=s))