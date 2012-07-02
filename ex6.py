x = "Hay %d tipos de personas." % 10
binary = "binario"
do_not = "no saben binario"
y = "Los que conocen %s y los que %s" % (binary, do_not)

print x
print y

print "Dije: %r" % x
print "Tambien dije: %s" % y

hilarious = False
joke_evaluation = "Es chistozo?! %r"

print joke_evaluation % hilarious

w = "Este es el lado izquierdo de...."
e = "un string con un lado derecho."

print w + e