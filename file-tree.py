import os


def make_tree (user_path):
    for (root,dirs,files) in os.walk(user_path, topdown= True):
        print (os.path.basename(os.path.normpath(root)))
        print ("    {}".format(dirs))
        print ("        {}".format(files))




user_path = input ("Enter Path for Tree:" )


make_tree(user_path)
