from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "Otherwise just hit enter."

raw_input('?')

print "Opening the file...."
target = open(filename, 'w')

print "Truncating the file.. Goodbye!"
target.truncate()

print "Now, three lines please..."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file..."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Finalmente se cierra..."

target.close()
