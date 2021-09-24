# coding=UTF-8
motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 末尾增加元素，指定位置插入元素
motorcycles.append('honda')
motorcycles.insert(0, 'jialing')
print(motorcycles)

# 删除元素
del motorcycles[1]
print(motorcycles)


# 弹出元素并可以被应用
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

# 根据制移除元素
motorcycles = ['honda', 'yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)

a = 'yamaha'
motorcycles.remove(a)
print (motorcycles)


