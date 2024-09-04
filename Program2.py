



## Problem 1 ##
#Please write a script that:
# - Asks for the user's name and then prints it twice, on two consecutive lines.


name= input("what is your name?")
print(name)
print(name)




## Problem 2 ##
#Please write a script that:
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line,
# - another between the two names and a third one at the end of the line.


newname = input("Again, what is your name?")
print("!" + newname + "!" + newname + "!")




## Problem 3 ##
#Please write a script that:
# - Asks for the user's name and address.
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630
newname = input("what is your first name? ")
namelast = input("whats ur last name? ")
address = input("gimme your street address boy ")
secondaddress = input("gimme yo city and postal code now boy ")


print("First name:" + newname)
print("last name: " + namelast)
print("Street Address: " + address)
print("City and Postal code: " + secondaddress)


## Problem 4 ##
#Please write a script that:
# - Asks for 3 words
# - Puts the words together with dashes and prints that out


zingy = input("gimme a word")
ten = input("gimme another word")
nine = input("gimme one more pls pls")


print( zingy + "-" + ten + "-" + nine)




## Problem 5 ##
#Please write a script that:
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572.
#One morning Mary woke up to an awful racket: a dragon was approaching the village.
#Only Mary could save the village's residents.

name3 = input("whats your name again?? ")
year = input("and what year where you born? ")

print ("Once upon a time, in a land far far away... ")
print(" There lived a boy named " + name3 + ". He was born in " + year)
print("One day... he was walking down the street minding his own business")
print("...And he was hit by a car!!!!")
print("He died.")
print("and thats the end of the story of " + name3)
print("RIP " + name3)


