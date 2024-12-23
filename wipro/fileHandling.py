import time


def handleFile(fileName, write=False):
    if (not write):
        searchWith = str(input("search domain:")).strip()

        with open(fileName, "r") as getFile:
            for line in getFile:
                if searchWith in line:
                    print(line, end=" ")

    else:
        changedFrom = (str(input("old domain:"))).strip()
        changedTo = str(input("new domain:")).strip()

        with open(fileName, "r") as getFile:
            lines = getFile.readlines()

        with open(fileName, "w") as getFile:
            for line in lines:
                if changedFrom in line:
                    getFile.write(line.replace(changedFrom, changedTo))
                else:
                    getFile.write(line)


# handleFile("emails.txt")


def pickleHandling():
    import pickle
    import os
    # Object to be pickled
    a = ['A dummy question', 'The correct answer', 'A wrong answer']

    # File name
    fileName = "testfile"

    # Open the file in binary write mode and dump the object
    with open(fileName, 'wb') as fileObject:
        pickle.dump(a, fileObject)  # Serialize and save the list

    # Open the file in binary read mode and load the object
    with open(fileName, 'rb') as fileObject:
        b = pickle.load(fileObject)  # Deserialize and read the list

    # Print the loaded object
    print(b)
    os.rename("testfile","newTestfile")
    os.remove("newTestfile")
    # os.mkdir("makeNewDir")
    # os.chdir("ChangeToDir")
    # os.rmdir("makeNewDir")

    print(os.listdir("../"))
    print(os.path.isdir("emails.txt"))  #check it is dir
    print(os.stat("emails.txt"))
    print(os.stat("emails.txt").st_mtime)
    print(time.asctime(time.gmtime(os.stat("emails.txt").st_mtime)))
    print(os.getcwd())

# pickleHandling()


def r():
    with open("testcase.txt", "w") as getFile:
        getFile.write("[")
        for i in range(10 ** 5):
            getFile.write(f"1,")
        getFile.write("]")
r()