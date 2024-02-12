#a list of items

my_list = ["apple, banana, orange"]
#print (my_list)

#datatype string
anotherlist = ["string", 12, "This is my second list", 345, True, False]
#print (anotherlist)
#not correct

#for loop
#thislist = ["apple", "banana", "cherry"]
#for x in thislist:
#print(x)

momlist = ["flour", "eggs", "milk"]
for x in momlist:
  print(x)

whatyougot = ["flour", "eggs", "dog"]

for i in whatyougot:
  if i not in momlist:
    print("no")
  else:
    print("yes")

whatyougot.append("sugar")
print("After append", whatyougot)
whatyougot.remove("flour")
print("After remove", whatyougot)