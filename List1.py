#In python there are 4 collections:
# List Set Tuple Dictionary 
#List- It's ordered/changeable and duplicates are allowed
#Tuple is just like list, it's just unchangeable

pet = ["Dog","Cat","Hamster","Fish"]

#Just like string, we can perform indexing on list:

print(pet[::-1]) #[start:End:Step]

#Lists are also iterable:
for animal in pet:
    print(animal)

#Methods to use on list

length = len(pet)
print(length)

#To see all the methods we have 
#print(dir(pet))
#print(help(pet))

#To check if an item is in list or not/ also finding the index of an specific element

print("turtle" in pet)
print(pet.index("Dog"))
print(pet.__getitem__(2)) #to check what element is on that specific index

#Append, Insert, clear, copy, pop, count, reverse, sort

pet.append("Turtle")
print(pet)

pet.remove("Cat")
print(pet)

pet.insert(3,"Bunny")
print(pet)

pet.count("Dog")
print(pet)

pet.reverse()
print(pet)

pet.sort()
print(pet)

pet.pop()
print(pet)

pets = pet.copy()

pet.clear()
print(pet)

print(pets)