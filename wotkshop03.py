print('***********************************************************************')
print('**************************AREA & CUB***********************************')
print('***********************************************************************')

from area_and_volume import area_of_rectangle, area_of_circle, volume_of_rectangle, volume_of_sphere

def show_menu():
  print("1. พื้นที่สี่เหลี่ยม")
  print("2. พื้นที่วงกลม")
  print("3. ปริมาตรทรงสี่เหลี่ยม")
  print("4. ปริมาตรทรงกลม")
  print("0. ออกจากการทำงาน")

show_menu()

option = input("เลือกเมนูที่ต้องการ (1, 2, 3, 4 หรือ 0): ")

if option == "1":
  length = float(input("ป้อนความยาวของสี่เหลี่ยม: "))
  width = float(input("ป้อนความกว้างของสี่เหลี่ยม: "))
  area = area_of_rectangle(length, width)
  print("พื้นที่สี่เหลี่ยม = ", area)
elif option == "2":
  radius = float(input("ป้อนรัศมีของวงกลม: "))
  area = area_of_circle(radius)
  print("พื้นที่วงกลม = ", area)
elif option == "3":
  length = float(input("ป้อนความยาวของทรงสี่เหลี่ยม: "))
  width = float(input("ป้อนความกว้างของทรงสี่เหลี่ยม: "))
  height = float(input("ป้อนความสูงของทรงสี่เหลี่ยม: "))
  volume = volume_of_rectangle(length, width, height)
  print("ปริมาตรทรงสี่เหลี่ยม = ", volume)
elif option == "4":
  radius = float(input("ป้อนรัศมีของทรงกลม: "))
  volume = volume_of_sphere(radius)
  print("ปริมาตรทรงกลม = ", volume)
elif option == "0":
  print("ออกจากการทำงาน")
else:
  print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")