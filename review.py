#CRUD, Create, remove, update, delete (we dont do update)
shoppinglist = ["bananas", "apples", "oranges", "eggs"]
while True:
    print("-" * 20)
    print("'q' => Quit the program")
    print("'A' => Add")
    print("'B' => Delete")
    print("'C' => Display")
    print("-" * 20)
    user_input = input("Enter Option: ")

    if user_input == "q":
        print("Bye, Bye!")
        break

    elif user_input == "A":
        print("-" * 20)
        new_item = input("New item: ")
        shoppinglist.append(new_item)
        print("-" * 20)

    elif user_input == "B":
        print("-" * 20)
        remove_item = input("Item to remove: ")
        shoppinglist.remove(remove_item)
        print("-" * 20)

    elif user_input == "C":
        print("-" * 20)
        for item in (shoppinglist):
            print(item)
        print("-" * 20)