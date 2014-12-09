# dicts and sets lab
person_dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print person_dict
del person_dict['cake']
print person_dict
person_dict['fruit']='Mango'
print person_dict
print person_dict.keys()
print person_dict.items()
print person_dict.values()
print 'cake' in person_dict
vals=person_dict.values()
print 'Mango' in vals

num=range(0,16)
hexa = [hex(x) for x in range(0,16)]
print num,hexa
dict_num = dict(zip(num,hexa))
print dict_num    

dict_a_keys=[person_dict.keys()]
print dict_a_keys
dict_a_vals=[person_dict.values()]
print dict_a_vals
#print type(dict_a_vals)
for s in dict_a_vals:
    print s 
    #the_val=str(dict_a_vals[v]) 
#    dict_a_vals[val]=the_val.count('a')

s1=set(range(0,21)) 
print s1
#for i in s1:
#    print i, s1(i) 
letters_in_py = set("Python")
print letters_in_py
letters_in_py.add("i") 
print letters_in_py
frozen_marathon=frozenset("marathon")
print frozen_marathon
print letters_in_py.union(frozen_marathon)
print letters_in_py.intersection(frozen_marathon)