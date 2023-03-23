fruits = {'apple', 'banana', 'orange'}

print("add(): 세트에 원소를 추가")
fruits.add('mango')
print(fruits)

# 교집합 합집합
shop={'apple','microsoft','google'}
print(fruits & shop)
print(fruits | shop)

# 다중 교집합, 합집합
list_of_sets=[fruits,shop]
print(set.intersection(*list_of_sets))
print(set.union(*list_of_sets))

div=list('apple')
print(div)
div=set(div)
print(div)