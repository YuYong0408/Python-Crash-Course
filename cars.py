# coding=UTF-8
# sort（） 按字母顺序排序，永久行更改， 可通过reverse = True 进行字母反向排序。

cars = ['bmw', 'adui', 'benz','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

# sorted（） 对列表进行临时排序
cars = ['bmw', 'adui', 'benz','toyota','subaru']
print(sorted(cars))
print(sorted(cars,reverse = True))
# 原列表顺序不变
print(cars)


# 列表反转
print("\n")
print(cars)
cars.reverse()
print(cars)
print(len(cars))

cars = ['bmw', 'adui', 'benz','toyota','subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
car ='bmw'
if(car == 'bmw'):
    print('Ture')
else:
    print('false')
if(car =='BMW'):
    print('Ture')
else:
    print('false')
if(car =='audi'):
    print('Ture')
else:
    print('false')

    
