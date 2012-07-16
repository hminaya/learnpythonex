from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copiando de %s a %s" % (from_file, to_file)

input = open(from_file)
indata = input.read()

print "El archivo original tiene %d bytes" % len(indata)

print "¿Existe el archivo de destino? %r" % exists(to_file)
print "Favor presionar a ENTER para continuar...."
raw_input('>')

output = open(to_file, 'w')
output.truncate()
output.write(indata)

print "Listo."

output.close()
input.close()