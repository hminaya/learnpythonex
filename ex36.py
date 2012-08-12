from sys import exit

def java():
	print "Soy un rebelde sin causa"

def php():
	print "Quiero ser rebelde, pero no voy a coger lucha con Java"

def net():
	print "Hago lo que me digan en la empresa"

def python():
	print "Consegui trabajo en Google o soy de Santiago"

def otro():
	print "Bueeeeno, ta jodon..."

def start():
	print "En que lenguaje programas y te dire quien eres..."
	print "java - php - net - python"

	lng = raw_input("dime > ")

	if lng == "java":
		java()
	elif lng == "php":
		php()
	elif lng == "net":
		net()
	elif lng == "python":
		python()
	else:
		otro()



start()