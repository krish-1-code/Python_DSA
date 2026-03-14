#So dictionary is a collection of key-value pairs.
#we can create a dictionary via {key:value} pairs. If the key or value is a string, we can use double quotes.
#Dictionary is ordered and changeable, but no duplicates.

animals = {"Dog": "puppy",
            "Cat": "Kitten"}

#To print one specific value for a given key:

print(animals.get("Dog"))

#To extend the dictionary, we can use the update method:

print(animals.update({"Pig": "Piglets"}))
print(animals)

#To remove a key-value pair, we can use the pop method:

#print(animals.pop("Dog"))
#print(animals)

#To delete the latest key-value pair:

print(animals.popitem())

#To print only the keys:

animal = animals.keys()
print(animal)

#We can also iterate over these keys:

for animal in animals.keys():
    print(animal)

#Same can be done for values:

for baby in animals.values():
    print(baby)

# We can do the same for both keys and values:

for animal, baby in animals.items():
    print(f"{animal} = {baby}")

var1 = animals.items()
print(var1)