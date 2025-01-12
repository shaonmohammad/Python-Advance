file = open("file.txt","r")
print(file.read())
file.close()

file = open("file.txt","rb") # read a file with binary mode (rb)
print(file.read())
file.close()

# Line-by-Line Reading in Python
with open("file1.txt","r") as files:
    for file in files:
        print(file.strip())

# Line by line read usning readline()
with open("file1.txt","r") as files:
    line = files.readline()
    while line:
        print(""(line))
        line = files.readline()



    
