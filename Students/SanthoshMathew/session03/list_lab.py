
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
#print fruits
fruit_new=raw_input ("what other fruit do you like to add?")
#print fruit_new
#print type(fruit_new)
fruits.append(fruit_new)
print fruits
length=len(fruits)
print length
print ("give me a number that is between 1 and", length)
num=int(raw_input(""))
print "OK no", num, "it is....and the fruit you picked is:", fruits[num-1]
# Add using "+"
fruits = ["Kiwi"]+fruits 
print fruits
fruits.insert(0,"Bananas")
print fruits
#for fruit in fruits:
#    if fruits.startswith('P'): 
#        fr=fruits[fruit]
fruits2=fruits 
print fruits2 
del fruits2[-1]
print fruits2
fruitd=raw_input("which fruit do you want to remove from the list?") 
#print fruitd
del fruits2[fruits2.index(fruitd)] 
print fruits2


        
        
    


