import math
import turtle

#nhập vào màu tô, chiều dài và chiều rộng hình chữ nhật
color = input('Nhập màu hoặc mã màu:')
h = float(input('chiều dài hình chữ nhật: '))
w = float(input('chiều rộng hình chữ nhật: '))
def move(trai_phai,goc,chieu_dai):
    if trai_phai==True:
        t.rt(goc)
        t.fd(chieu_dai)
    else:
        t.lt(goc)
        t.fd(chieu_dai)

#Vẽ hình chữ nhật, tô màu theo dữ liệu đã nhập
t=turtle.Turtle()
t.hideturtle()
#thiết lậ màu tô
t.color(color)
t.fillcolor(color)
t.begin_fill
move(True,90,h)
move(True,90,w)
move(True,90,h)
move(True,90,w)
t.end_fill()
turtle.done()

#tính chu vi hình chữ nhật
c = 2*(w+h)
s = w*h

#hiển thị kết quả
print('chu vi hình chữ nhật dài {h}, rộng {w} là {c}'.format(h=h, w=w, c=c))
print('diện tích hình chữ nhật dài {h}, rộng {w} là {s}'.format(h=h, w=w, s=s))