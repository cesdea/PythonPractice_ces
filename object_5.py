import object_Book
# b=object_Book.Book()
# b.setData('아임 히어로','300','마키')
# b.printData()

print("__init__: 함수를 생성할때 변수 값을 설정")
b=object_Book.Book('아임 빌런','0','아치')
b.printData()
# del b
# b.printData() 이미 사라진 클래스
print("__del__: 함수를 삭제할때 나오는 값을 설정")
del b

print("__repr__: 함수를 출력할때 나오는 값을 설정")
b=object_Book.Book('아임 빌런','0','아치')
print(b)

print("__add__(x): 더하는 메소드")
a=object_Book.Book('아임 히어로','500','아치')
print(a.__add__(b))

print("__lt__(x): 비교하는 메소드")
print(a.__lt__(b))