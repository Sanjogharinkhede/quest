

def handleFile(fileName,write=False):
        if(not write):
            searchWith=str(input("search domain:")).strip()

            with open(fileName,"r") as getFile:
                for line in getFile:
                    if searchWith in line:
                        print(line, end=" ")

        else:
            changedFrom = (str(input("old domain:"))).strip()
            changedTo = str(input("new domain:")).strip()

            with open(fileName, "r") as getFile:
                lines = getFile.readlines()

            with open(fileName,"w") as getFile:
                for line in lines:
                    if changedFrom in line:
                        getFile.write(line.replace(changedFrom,changedTo))
                    else:
                        getFile.write(line)

handleFile("emails.txt",True)