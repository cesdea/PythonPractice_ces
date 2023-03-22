# py`s type: number, sequence,mapping
#number

print('number')
i=5
f=0.5
c=3+4j
print('i:',type(i)) #int 정수
print('f:',type(f)) #float 실수
print('c:',type(c)) #complex 복소수


print('sequence')
s='string'
l=[0,1,2]
t=('code','computer','key')
print('s:',type(s)) #str 문자열
print('l:',type(l)) #list 리스트
print('t:',type(t)) #tuple 튜플

print('mapping')
b=True
nb=False
cb=3>=1
d={
    'one':12,
    'two':34,
    'three':56
}
se={'apple','banana'}
print('b:',type(b)) #bool 참/거짓
print('nb:',type(nb)) #bool 참/거짓
print('cb:',type(cb)) #bool 참/거짓
print('d:',type(d)) #dict 매핑(키와 값으로 이루어져있다.)
print('se:',type(se)) #set 집합
