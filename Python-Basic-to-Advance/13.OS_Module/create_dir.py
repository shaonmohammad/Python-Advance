import os

parent = os.getcwd()
child = "text.py"
path = os.path.join(parent,child)
os.mkdir(path)  # we can also send the mode for directory permission (read/write)

