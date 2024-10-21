newfile = open(r"C:\Users\jusju\python_repo\python_learn\python-learn-file\new_file.txt", "w")
newfile.write("I like Python\nDo you?")
newfile.close()
newfile = open(r"C:\Users\jusju\python_repo\python_learn\python-learn-file\new_file.txt", "w")
newfile.writelines(["Cisco\n", "Juniper\n", "HP\n", "Nortel\n"])
newfile.close()
newfile = open(r"C:\Users\jusju\python_repo\python_learn\python-learn-file\new_file.txt", "a")
newfile.write("This string is appended to the file")
newfile = open(r"C:\Users\jusju\python_repo\python_learn\python-learn-file\new_file.txt", "w+")
newfile.write("This string is appended to the file")
newfile.seek(0)
print(newfile.read())
newfile.close()
#Automatically close the file after the block of code
with open(r"C:\Users\jusju\python_repo\python_learn\python-learn-file\new_file.txt", "w+") as f:
    f.write("This string is appended to the file")
    
print(f.closed)    

