file = open("file.txt","w")
file.write("Hello Afat!")
file.close()

file = open("file.txt","w")
file.write("Hello Tasruba!")
file.close()


# Writing multiple lines to an existing file using writelines()
s = ["First line of text.\n", "Second line of text.\n", "Third line of text.\n"]

with open("writeline.txt","w+") as file:
    file.writelines(s)
    
with open("writeline.txt","r") as file:
    print(file.read())
    

