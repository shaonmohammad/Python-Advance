import os
def get_current_directory():
    print(os.getcwd())

print("This is current working directory...")
get_current_directory()

print("After chnage the directory...")
os.chdir("../")

get_current_directory()
