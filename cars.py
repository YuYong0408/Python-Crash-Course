# coding=UTF-8
# sort���� ����ĸ˳�����������и��ģ� ��ͨ��reverse = True ������ĸ��������

cars = ['bmw', 'adui', 'benz','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

# sorted���� ���б������ʱ����
cars = ['bmw', 'adui', 'benz','toyota','subaru']
print(sorted(cars))
print(sorted(cars,reverse = True))
# ԭ�б�˳�򲻱�
print(cars)


# �б�ת
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

    
