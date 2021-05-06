import random
def randInt(min= 0 , max= 5  ):
    num = random.random()
    return num
print(randInt()*20) 		    # should print a random integer between 0 to 100
print(randInt(max=50)*10) 	    # should print a random integer between 0 to 50
print(randInt(min=50)*10+50) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500)*90+50)    # should print a random integer between 50 and 500