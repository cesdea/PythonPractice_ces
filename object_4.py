import object_Fridge
f=object_Fridge.Fridge()
apple=object_Fridge.Food()
elephant=object_Fridge.Food()

f.open()
f.put(apple)
f.put(elephant)
print(f.foods)