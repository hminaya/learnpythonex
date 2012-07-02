#podemos aceptar varios argumentos, como los scripts
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#aqui son fijos	
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#uno solo
def print_one(arg1):
	print "arg1: %r" % arg1

#ninguno
def print_none():
	print"I got nothin..."

print_two("Jose", "Shaw")
print_two_again("Noe", "new")
print_one(1)
print_none()