family=['mother','father','gentleman','sexy lady']
length=len(family)
print(length)
print(family[3])
family.remove('sexy lady')
print(family)
# family.remove('gantlman')
# print(family)
# 없는 원소일경우 에러

array=list(range(0,5))
print("array",array)

print("append(x):x를 마지막에 추가")
# 마지막에 추가
array.append(5)
print(array)

array=list(range(0,5))
print("insert(i,x):i자리에 x를 추가")
# 특정 자리에 추가
array.insert(3,5)
print(array)

array=list(range(0,5))
print("a+b: 두 리스트 합성")
# +연산자
result=array+[0,1,3]
print(result)

array=list(range(0,5))
print("extend(l): + 연산자와 같이 l리스트를 합성")
# 리스트 합성
array.extend([1,2,3])
print(array)

array=list(range(0,5))
print("del l[i] : l리스트의 i번째 원소 삭제")
# 특정 위치 원소 삭제
del array[0]
print(array)
