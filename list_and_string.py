# 문자열 str
x = 'banana'
print(x[0])            # 0번 글자는?
print(x[2:4])          # 2번부터 4번 앞(3번)까지는?
print(x[:3])           # 처음부터 3번 앞(2번)까지는?
print(x[3:])          # 3번부터 끝까지는?

print("find(x):x가 몇번쨰 자리에 있는지")
print(x.find('n'))

y='asd '
print("rstrip():오른쪽 공백 제거")
y=y.rstrip()
print(y,len(y),' ')

z='one two three'
print("split(): 분할")
print(z.split()) # 기본 공백
print(z.split('e')) # e를 기준으로 분할

#리스트 list
array=[4,3,2,1,5]
print("sort(): 정렬")
array.sort()
print(array)

array=[4,3,2,1,5]
print("insert(i,x): i번쨰에 x를 삽입")
array.insert(0,10)
print(array)

print("pop(): 리스트의 마지막 원소를 삭제하면서 리턴")
last=array.pop()
print(array)
print(last)