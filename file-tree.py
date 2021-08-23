import os


def make_tree (user_tree):
    os.system(user_tree)

user_path = input ("Enter Path for Tree:" )

user_tree = "tree" + " " + user_path

make_tree(user_tree)
