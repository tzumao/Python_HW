for i in range(0,256):
    if chr(i).isprintable():
        print("({},{})".format(i,chr(i)))
