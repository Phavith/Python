#Remove the leading and trailing whitespaces at the beginning and at the end of the string
my_str = "     Hello     "

print(my_str.strip(), "World")


#Replace the words
my_str_1 = "Hello World"

print(my_str_1.replace("Hello", "Bye Bye"))


#Split
my_str_2 = "Hello, world, you, me"

print(my_str_2.split(","))