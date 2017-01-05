import os

def run(**args):
    print "[*] In dirlister module."
    for a in args:
        dirname=args[a]
        files = os.listdir(dirname)
        return str(files)

# run like this:
#print run(**{'dirname': "."})
