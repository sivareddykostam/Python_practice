#//--------------------------------------------------------------------------------------------
#// Python list methods
#//--------------------------------------------------------------------------------------------
'''
a = [6,[7,8],9,10]
b = [1,2,3,4,5]
print(a)
print(a[1])
print([b]+[a])
print(b+a)
print([0]+b)
print(b[2:4]=[])
'''

'''
cricket = ['ground','pitch','bat','ball']
cricket.sort()
print(cricket)
'''

'''
cricket = ['ground','pitch','bat','ball']
cricket.reverse()
print(cricket)
'''


#fruits = ['banana','apple','orange','lemon']
#fruits.remove('apple')
#fruits.pop(1)
#fruits.insert(1,'grape')
#s = fruits.index('lemon')
#print(s)
#cars = ['Rolls Royce','Audi','Ferrary','Benz']
#fruits.extend(cars)
#print(fruits)


#x = fruits.count('banana')
#print(x)
#y = cars.count('Audi')
#print(y)

'''
fruits = ["banana","apple","orange","lemon"]
cars = ["Audi","BMW","Ferrary","Rolls Royce"]
print(len(fruits))
print(len(cars))
print(type(fruits))
print(type(cars))
#fruits.clear()
#print(fruits)
#cars.clear()
#prints(cars)
'''

'''
x = fruits.copy()
print(x)
y = cars.copy()
print(y)
'''


#cars = list(('Rolls Royce','BMW','Audi','Benz'))
#print(cars)

'''
a = [1,2,3,4]
a.append(5)
print(a)
'''


'''
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print('List+Tupple:',thislist)
'''

'''
thislist = ["apple", "banana", "cherry"]
[print('iteration through the list:',x) for x in thislist]
'''

'''
a=10
b=20.3
c="Vamshi"
d="Venkat"
f=[1,2,3,4]
g=('Tommy','Jerry')
e={'Venkat':'student','vamsi':'Prof','siva':'CEO'}

print('value of a:',a)

print('added value:',a+b)

print('value of b:',b)

print('float added value:',a-b)

print('mul & quo:',a*2,a%2)

print('string of c is:',c)

i=c+d
print('a+d is',i.split())

print('slicing of string:',i[2],i[-1],i[6:],3*i,len(i))

print('total list:',f)

print('added list:',f+[1,3,5])

print('list indexing:',f[3],f[0:2])

del(f[2:])
print('deleted list:',f)
'''

g=('Tommy','Jerry')
print("tuple:",g)

y=list(g)
y.remove('Tommy')
print('removed tupple:',y)




















