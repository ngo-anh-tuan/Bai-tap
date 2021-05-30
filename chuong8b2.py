import math

def giai_pt_bac_nhat(a, b):
   if a == 0:
       if b == 0:
           return "Phương trình có vô số nghiệm"
       return "Phương trình vô nghiệm"
   return "Phương trình có 1 nghiệm duy nhất: \nx = {}".format(-b / a)
  
def giai_pt_bac_hai(a, b, c):
   if a == 0:
       return giai_pt_bac_nhat(b, c)
   delta = b * b - 4 * a * c
   if delta > 0:
       x1 = float((-b + math.sqrt(delta)) / (2 * a))
       x2 = float((-b - math.sqrt(delta)) / (2 * a))
       return "Phương trình có 2 nghiệm phân biệt là: \nx1 = {} \nx2 = {}".format(x1, x2)
   if delta == 0:
       x = -b / (2 * a)
       return "Phương trình có nghiệm kép: \nx1 = x2 = {}".format(x)
   return "Phương trình vô nghiệm"

try:
   #Nhap bac cua phuong trinh
   Bac = input('Nhap bậc của phương trình: ')
   #TH 1: Giai phuong trinh bac nhat
   if Bac == '1':
      a, b = map(float, input('Nhập hệ số a, b: ').split())
       #Goi ham giai phuong trinh bac nhat
      print(giai_pt_bac_nhat(a, b))
   #TH 2: Giai phuong trinh bac hai
   elif Bac == '2':
       a, b, c = map(float, input('Nhập hệ số a, b, c: ').split())
       print(giai_pt_bac_hai(a, b, c))
   else:
       print("Vui lòng chọn lại bậc là 1 hoặc 2")
except:
   print("Số liệu nhập vào không hợp lệ!")
