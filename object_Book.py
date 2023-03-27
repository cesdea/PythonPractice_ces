class Book:

    def setData(self, title, price, author):
        self.title = title
        self.price = int(price)
        self.author = author

    def printData(self):
        print('제목 : ', self.title)
        print('가격 : ', self.price)
        print('저자 : ', self.author)

    def __init__(self,title,price,author):
        self.setData(title, price, author)
        print('책 객체를 새로 만들었어요~')
    def __del__(self):
        print("책이 분실됨")
    def __repr__(self)->str:
        return self.title
    def __add__(self,other):
        return self.price+int(other.price)
    def __lt__(self, other):
        return self.price<other.price