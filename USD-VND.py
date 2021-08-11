Rate = float(input('Nhập tỉ giá USD/VND: '))
USD = int(input('Nhập số tiền USD cần đổi: '))
VND = USD * Rate
print('Số tiền {USD} USD sau khi đổi theo tỉ giá USD/VND {Rate} là {VND} VND'.format(USD=USD,Rate=Rate,VND=VND))
