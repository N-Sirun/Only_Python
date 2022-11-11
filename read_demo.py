f = open("testdemo.txt", "r")
print(f.readline())
f.close()

f = open("testdemo.txt", "r+")
f.write("Some text")
f.close()