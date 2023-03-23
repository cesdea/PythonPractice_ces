print('변수 바꾸기')
#case1
a = 10
b = 20
temp = a               # a 값을 temp에 저장   (temp = 10)
a = b                  # b 값을 a에 저장      (a = 20)
b = temp               # temp 값을 b에 저장   (b = 10)
print(a, b)
#case2(use tuple)
c = 10
d = 20
c, d = d, c                 
print(c, d)

print('튜플 함수 버전')
def magu_print(x, y, *rest):        # 마구 찍어 함수
    print(x, y, rest)
magu_print(1, 2, 3, 5, 6, 7, 9, 10)

print('튜플 비우기, 하나')
empty=()
one=5,
print(empty,one)


print('튜플 고치기')
p = (1,2,3)
q = p[:1] + (5,) + p[2:]
print(q)
r = p[:1], 5, p[2:]
print(r)


print('튜플에서 리스트, 리스트에서 튜플')
p = (1, 2, 3)
q = list(p)                  # 튜플 p로 리스트 q를 만듦
print(q)
r = tuple(q)                 # 리스트 q로 튜플 r을 만듦
print(r)