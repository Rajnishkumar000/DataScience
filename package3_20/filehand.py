import os
f = open("demofile.txt","a")
f = open("demofile.txt", "rt")
f = open("demofile.txt", "r")
print(f.read())
f = open("demofile.txt", "r")
print(f.readline())
f.close()


os.remove("demofile.txt")