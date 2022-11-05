'''f = open('def1.txt', 'r')
for line in f.readlines():
    print(line.strip())'''

f = open('def55.txt', 'w')
f.write("Hello\n")
f.write("How are you?\n")
f.close()

f = open('def55.txt', 'a')
f.write("Are you OK?\n")
