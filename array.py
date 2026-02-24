#Array - Static Array / Dynamic Array

#static array: A contiguous block of memory with a mix size.

#C array can be an example of static array cuz once you declare the size it's permanent
# let's say int arr[5]; You can only store 5 numbers

#While looking for elements at a specific index. For eg: arr[2]. It's O[1].
#Static Arrays are mutable. We can chnage an element at a specific index.

# Let's say arr = [1,2,3,4,5]
# if we have to find an element's index. Best case can be O[1] worst case can be O[n].

#Some more limitaions of static array:
#Let's say I want to add 7 at the 2nd index of the array
#Either I have to replace 3 with 7 or I have to shift 3,4,5 which will result in 5 getting lost.
#If i have to delete a element then again I have to reverse replace all the elemenst to make a contiguous block of memory.


#List in Python is an example of dynamic array.

#Remeber how it was impossible to add new element in an static array as the memory was already allocated for only 5 elements/
#In dynamic array we can easily add a new element to the array via append method
# And delete an element via pop method.

#When we append a new element to a list some operations are constant time i.e. O[1] but some are O[n]. Why?

# - Under the hood of dynamic array it just static arrays. Whenever we append an element to a dynamic array, in background a static array is created
# The new static array copies the old static array and leaves some blank memory allocation for potential new appends. Up untill we have that empty memory
# for appending new element the operation performed is contant time or O[1], but we run out of that memory, once again a new static array has to be created
# and all the elements are copied into it which is O[n] operation/

# ##Removing last element from an array is always a O[1] operation.

# ##Inserting an element inbetween an array requires shifting of all other elements, so it is an O[n] operation.

