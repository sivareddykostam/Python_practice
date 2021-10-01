#//--------------------------------------------------------------------------------------------
#// Python Functions Method
#//--------------------------------------------------------------------------------------------

'''
def my_function():
  print("Hello World")

my_function()
'''

'''
def my_function(name):

  print(name + "Mirafra")

my_function("Manipal")
'''

'''
def my_function(name1,name2):
  print(name1 + " " + name2)

my_function("Siva","Reddy")
'''

'''
def my_function(a,b):
  print(a+b)

my_function(2,3)
'''

'''
def my_function(*name):
  print("The youngest child is " +name[2])

my_function("kostam","siva","reddy")
'''

'''
def my_function(child1,child2,child3):
  print("The Youngest Child is "+child3)

my_function(child1="Vamshi",child2="Venkat",child3="Siva")
'''

'''
def my_function(**name):
  print("Microsoft CEO is "+name["name1"])

my_function(name1="Satya Nadendla",name2="Sundar Pichai")
'''

'''
def my_function(country = "India"):
  print("I am From "+ country)

my_function("Italy")
my_function("America")
my_function()
'''

'''
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple","banana","orange"]
my_function(fruits)
'''

'''
def my_function(x):
  return 5*x

print(my_function(3))
print(my_function(5))
print(my_function(6))
'''

'''
def func(a,b,*r):
  if(a>b):
    c=a*b
    return(print("True with %s"%(r)))
  else:
    return(print("False",r))

x=func(1,2,[3,5,6])
print(x)
'''

#Function Definition :
def function_with_default_arg(name="Jasmine",number=3):
      print(name+"'s","number is",number);

#Function Call :
function_with_default_arg("Paul");







