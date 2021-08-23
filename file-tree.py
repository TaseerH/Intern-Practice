import os



def make_tree (user_path, i):
    if i == 1 :
        print ("|---->"+os.path.basename(os.path.normpath(user_path)))
    elif i == 2 :
        print ("    |---->"+os.path.basename(os.path.normpath(user_path)))
    elif i == 3 :
        print ("        |---->"+os.path.basename(os.path.normpath(user_path)))
    elif i > 3 :
        print ("            |---->"+os.path.basename(os.path.normpath(user_path)))
    else:
        print (os.path.basename(os.path.normpath(user_path)))
        print ("|")
    for item in os.listdir(user_path):
        item = os.path.join(user_path, item)
        if os.path.isfile(item):
            if i == 1:
                print("     |->"+os.path.basename(os.path.normpath(item)) + " is a file")
            elif i == 2 :
                print ("        |---->"+os.path.basename(os.path.normpath(item))+ " is a file")
            elif i > 2 :
                print ("            |---->"+os.path.basename(os.path.normpath(item))+ " is a file")
            else:
                print("|->"+os.path.basename(os.path.normpath(item)) + " is a file")
        elif os.path.isdir(item):
            i = i+1
            make_tree(item, i)
        else:
            print("Unknown!")

user_path = input ("Enter Path for Tree:" )
i = 0
make_tree(user_path, i)
