#//--------------------------------------------------------------------------------------------
#// Dictionary
#//--------------------------------------------------------------------------------------------

dic = {'venkat':'student','siva':'employe','vamsi':'lecturer'}
print('total dic:',dic)
print('gets 1 item value:',dic['venkat'])
dic['venkat']='CEO'
print('changed value of venkat:',dic)

print('getting keys from dic:',dic.keys())
print('getting whole values:',dic.values())
print('getting all items:',dic.items())

del(dic['vamsi'])
print('deleting particular item:',dic)

dic['muneeb']='instructor'
print('adding item:',dic)

#print(dic.has_key('siva'))

#print('getting value of a particular item:',dic.get('muneeb'))

#dic.update({'muneeb':'guest'})
#print('updating the dic:',dic)ii = "Feel My Love"
