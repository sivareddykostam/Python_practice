#//--------------------------------------------------------------------------------------------
#// Python Regular_Expressions Method
#//--------------------------------------------------------------------------------------------

'''
import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
'''
      
'''
import re

#Return a list containing every occurrence of "ai":

txt = "feel my love"
x = re.findall("l", txt)
print(x)
'''

'''
import re

txt = "India is a Beautiful Country"

#Check if "worst" is in the string:

x = re.findall("worst", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
'''

'''
import re

txt = "India is a Democratic Country"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 
'''

'''
import re

txt = "welcome to my world"
x = re.search("country", txt)
print(x)
'''

'''
import re

#Split the string at every white-space character:

txt = "The rain in Spain"
file = "world health organisation"
x = re.split("\s", txt)
y = re.split("\s",file,1)
print(x)
print(y)
'''

'''
import re

#Replace all white-space characters with the digit "9":

txt = "Game Of Thrones"
file = "Lord Of The Rings"
x = re.sub("\s", "_", txt)
y = re.sub("\s","_",file,2)
print(x)
print(y)
'''


import re

line = "This is Venkatesh and my work is to verify the SoC work level Ip's work the help oh UVM "
#replace= 'IP'
sz=re.sub("Ip's","IP",line)
print(sz)







