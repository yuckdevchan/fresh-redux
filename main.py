import sys

print("Welcome to Fresh Redux Lyric Generator")
name = input("Insert name of person: ")
pronoun = input("Insert pronoun of person: ")
parent = input("Insert parent of person: ")
parentpronoun = input("Insert parent's pronoun: ")
plate = input("Insert license plate of car: ")
place = input("Where is your person going? ")
placenoun = input("Is your place a proper noun? (y, n): ")
born = input("Where was your person born?: ")
days = input("Where did they spend most of their days: ")
title = input("Insert what they're going to become when they get there: ")
drinkglass = input("What does your person drink out of")

if placenoun == "y":
    placenoun = "the"
elif placenoun == "n":
    placenoun = ""
else:
    print("Error: Invalid Answer")
    sys.exit
    
place = placenoun + " " + place

lyrics = f"""Now, this is a story all about how
{name}'s life got flipped-turned upside down
And I'd like to take a minute
Just sit right there
I'll tell you how {name} became the {title} of a town called {place}
In {born} born and raised
In the {days} was where {name} spent most of his days
Chillin' out, maxin', relaxin', all cool
And all shootin' some b-ball outside of the school
When a couple of guys who were up to no good
Started making trouble in his neighborhood
{pronoun} got in one little fight and {parent} got scared
{pronoun} said, "You're movin' with your auntie and uncle in {place}"
{name} begged and pleaded with {parentpronoun} day after day
But he packed {name}'s suitcase and sent him on his way
He gave him a kiss and then he gave him his ticket
{name} put his Walkman on and said, "I might as well kick it"
First class, yo this is bad
Drinking orange juice out of a {drinkglass}
Is this what the people in {place} living like?
Hmm, this might be alright
But wait, I hear they're prissy, bourgeois, all that
Is this the type of place that they just send this cool cat?
I don't think so
{pronoun}'ll see when he gets there
{name} hopes that they're prepared for the {title} of {place}
Well, the plane landed and when {pronoun} came out
There was a dude who looked like a cop standing there with my name out
{name} ain't trying to get arrested yet, {pronoun} just got here
{pronoun} sprang with the quickness like lightning, disappeared
{pronoun} whistled for a cab and when it came near
The license plate said, "{plate}" and it had dice in the mirror
If anything {pronoun} could say that this cab was rare
But {pronoun} thought "Nah, forget it, yo, holmes to Bel Air"
{name} pulled up to the house about seven or eight
And he yelled to the cabbie, "Yo holmes, smell ya later"
{pronoun} looked at {place}
{pronoun} was finally there
To sit in their throne as the {title} of {place}"""

print(lyrics)
