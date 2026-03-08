name = "krish kushwaha"
print(name)


#Tripe quotation
message = """This is what
                needed to be done"""

print(message)

#To find the length of a string

print(len(name))

#Finding and searching

print(name.rfind('k')) #to find the last occurence 
print(name.find('r')) # Good for error check as it returns -1 if the substring isn't found
print(name.index('r')) # shows an error message.


#Capitalize, lower, upper

fruit = input("Enter a fruit name")

print(fruit.capitalize())
print(fruit.lower())
print(fruit.upper())

# To count and replace

phone_num = input("Enter your phone number: ")

print(phone_num.count("-"))
print(phone_num.replace("-"," "))


# Is alpha / Is digit

age = 80
fruit = "apple"
print(age.is_integer())
print(fruit.isalpha())

# To see more methods

#print(help(str))


# TASK 1:
# Take a password. Password shouldn't be more than 12 char. No space. No digits

password = input("Enter a word with no space, no digits and less than 12 letter: ")

length = len(password)

if(length <= 12):
    counter = password.count(" ")
    if counter>0:
        okay = password.isalpha()
        if okay:
            print("Good job")
        else:
            print("Only alphabets lil bro")
    else:
        print("No spaces lil bro")
else:
    print("Less than 12 char lil bro")
#reverse



#there is no specific method in python to reverse a string, instead we can do slicing