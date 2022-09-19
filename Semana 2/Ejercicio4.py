print ("***Welcome to Bella Napoli***")
option = input("Please enter a option: \n1-Vegetarian\n2-Non Vegetarian\n->")
if option.isnumeric():
    option=int(option)
    if option == 1: 
        ingredient = input("Please enter a option: \n1-Pimiento\n2-Tofu\n->")
        if ingredient == "1":
            print = "Pimiento"
        else:
            ingredient= "Tofu"
        print (f"The pizza is vegetarian and have {ingredient}")
    elif option == 2:
        ingredient = input("Please enter a option: \n1-Pepperoni\n2-Jamon\n2-Salmon\n->")
        if ingredient == "1":
            print ("Pepperoni")
        elif ingredient == "2":
            print ("Jamon")
        else: 
            ingredient= "Salmón"
        print (f"The pizza is not vegetarian and have {ingredient}")
    else:
        print ("Invalid option")
else: 
    print ("Error")