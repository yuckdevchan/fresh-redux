import sys

print("Welcome to Fresh Redux Lyric Generator")
name = input("Insert name of person: ")
pronoun = input("Insert pronoun of person: (eg. he, she, they) ")
parent = input("Insert parent of person: ")
parentpronoun = input("Insert parent's pronoun: (eg. he, she, they) ")
plate = input("Insert license plate of car: ")
place = input("Where is your person going? ")
placenoun = input("Is your place a proper noun? (y, n): ")
print("What are people like there? Give 2 adjectives.")
people1 = input("1. ")
people2 = input("2. ")
born = input("Where was your person born?: ")
days = input("Where did they spend most of their days: ")
title = input("Insert what they're going to become when they get there: ")
drinkglass = input("What does your person drink out of? ")
wear = input("What does your person wear? ")

if pronoun == "he":
  possesive = "his"
  thirdperson = "him"
elif pronoun == "she":
  possesive = "her"
  thirdperson = "her"
else:
  possesive = "their"
  thirdperson = "them"

if parentpronoun == "he":
  possesive = "his"
  thirdperson = "him"
elif parentpronoun == "she":
  possesive = "her"
  thirdperson = "her"
elif parentpronoun == "they":
  possesive = "their"
  thirdperson = "them"
else:
  possesive = "their"
  thirdperson = "them"

if placenoun == "y":
  placenoun = "the"
elif placenoun == "n":
  placenoun = ""
else:
  print("Error: Invalid Answer")
  sys.exit

place = placenoun + " " + place

lyrics = f"""--- LYRICS ---

Now, this is a story all about how
{name}'s life got flipped-turned upside down
And I'd like to take a minute
Just sit right there
I'll tell you how {name} became the {title} of a place called {place}
In {born} born and raised
In {days} was where {name} spent most of his days
Chillin' out, maxin', relaxin', all cool
And all shootin' some b-ball outside of the school
When a couple of guys who were up to no good
Started making trouble in {possesive} neighborhood
{pronoun} got in one little fight and {parent} got scared
{parentpronoun} said, "You're movin' with your auntie and uncle in {place}"
{name} begged and pleaded with {thirdperson} day after day
But {parentpronoun} packed {name}'s suitcase and sent {thirdperson} on {possesive} way
{parentpronoun} gave {thirdperson} a kiss and then he gave {thirdperson} {possesive} ticket
{name} put {possesive} {wear} on and said, "I might as well kick it"
First class, yo this is bad
Drinking orange juice out of a {drinkglass}
Is this what the people in {place} living like?
Hmm, this might be alright
But wait, I hear they're {people1}, {people2}, all that
Is this the type of place that they just send this {title}?
I don't think so
{pronoun}'ll see when he gets there
{name} hopes that they're prepared for the {title} of {place}
Well, the plane landed and when {pronoun} came out
There was a dude who looked like a cop standing there with {possesive} name out
{name} ain't trying to get arrested yet, {pronoun} just got here
{pronoun} sprang with the quickness like lightning, disappeared
{pronoun} whistled for a cab and when it came near
The license plate said, "{plate}" and it had dice in the mirror
If anything {pronoun} could say that this cab was rare
But {pronoun} thought "Nah, forget it, yo, holmes to {place}"
{name} pulled up to {place} about seven or eight
And he yelled to the cabbie, "Yo driver, you're {people1}"
{pronoun} looked at {place}
{pronoun} was finally there
To sit in {possesive} throne as the {title} of {place}"""

print(lyrics)
