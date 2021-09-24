squares = []
for value in range(1,11):
    square = value **2
    squares.append(square)
print(squares)

a = [1,2,3,4,5,6,7,8,9,10]
print(min(a))
print(max(a))
print(sum(a))

    
a = [value**2 for value in range(1,11)]
print(a)

b =[a for a in range(1,100001)]
print(b)

c = [value for value in range(3,31,3)]
print(c)
