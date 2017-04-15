import os

def run(**args):

    print "[*] In dirlister modules"
    files = os.lister(".")

    return str(files)

