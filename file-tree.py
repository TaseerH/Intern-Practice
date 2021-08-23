import os


def make_tree (user_path):
    for item in os.listdir(user_path):
        item = os.path.join(user_path, item)
        if os.path.isfile(item):
            print("     "+os.path.basename(os.path.normpath(item)) + " is a file")
        elif os.path.isdir(item):
            print(os.path.basename(os.path.normpath(item)) + " is a dir")
            make_tree(item)
        else:
            print("Unknown!")

user_path = input ("Enter Path for Tree:" )


make_tree(user_path)
