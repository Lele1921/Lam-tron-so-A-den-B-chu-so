giatria=input('nhập số: ')
giatrib=input('làm tròn đến chữ số thứ: ')
ketqua=False
try:
    a=float(giatria)
    b=int(giatrib)
    ketqua = True
except:
    print('Định dạng đầu vào không hợp lệ')
if ketqua:
    c=round(a,b)
    print(c)