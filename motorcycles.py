# coding=UTF-8
motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# ĩβ����Ԫ�أ�ָ��λ�ò���Ԫ��
motorcycles.append('honda')
motorcycles.insert(0, 'jialing')
print(motorcycles)

# ɾ��Ԫ��
del motorcycles[1]
print(motorcycles)


# ����Ԫ�ز����Ա�Ӧ��
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

# �������Ƴ�Ԫ��
motorcycles = ['honda', 'yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)

a = 'yamaha'
motorcycles.remove(a)
print (motorcycles)


