my_string = "Hello, World!"

#Print the length of my_string
print(len(my_string))

#Print "World" from my_string
print(my_string[6:12])

#Print character "H" from my_string
print(my_string[0])

#Print "HELLO, WORLD!" from my_string
print(my_string.upper())

#Print "hello, world!" from my string
print(my_string.lower())

#Print "Bye bye, World!" from my_string
print(my_string.replace ("Hello", "Bye Bye"))

#Print a splitted string, split at ","
print(my_string.split(","))

#Print "This is my world, say "Hello, World"" (using Concatenation and Escape Character)
a = "This is my world, say"
print(a + " " + my_string)
print("This is my world, say \'Hello, World!\'")

student_name = "Not a real student name"
grade = 12
#Print "my name is Not a real student name from grade 12"
print()