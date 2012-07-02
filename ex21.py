def add(a, b):
	print "ADD %d + %d" % (a,b)
	return a + b

def substract(a, b):
	print "SUBS %d - %d" % (a,b)
	return a - b

def multiply(a, b):
	print "MULT %d * %d" % (a,b)
	return a * b

def divide(a, b):
	print "DIV %d / %d" % (a, b)
	return a / b

print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
print "*Math.........\n"

age = add(25,6)
height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d " % (age, height, weight, iq)

print "\n*Extra credit"

#Sale impreso porque tiene un PRINT dentro de la funcion..
what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "Entonces: ", what, ". Hazlo a mano, #Leon...."