def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20,10)

print "OR, we can use variables"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math"
cheese_and_crackers(10+15, 4+7)

print "Combine both"
cheese_and_crackers(amount_of_cheese + 13, amount_of_crackers + 11)