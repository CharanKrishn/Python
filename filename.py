filename = input("Input The Filename: ")
myDict = {
    "py" : "python"
    }

f_extns = filename.split(".")

print ("the extension of the file is : " + repr(f_extns[-1]))

