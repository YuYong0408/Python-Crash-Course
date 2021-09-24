# coding = UTF-8
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
# 复制列表内元素不能用friend_foods= my_foods， 这样friend_foods随my_foods 
# 变化而变化,而且互相关联一个列表
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("My friend_foods are:")
print(friend_foods)

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("My friend_foods are:")
print(friend_foods)
