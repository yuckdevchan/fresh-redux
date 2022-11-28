import subprocess
import sys

def clipboard(txt):
    cmd='echo '+txt.strip()+'|pbcopy'
    return subprocess.check_call(cmd, shell=True)

print("Welcome to Fresh Redux Lyric Generator")
name = input("Insert name of person: ")
pronoun = input("Insert pronoun of person: ")
parent = input("Insert parent of person: ")
plate = input("Insert license plate of car: ")
place = input("Where is your person going? ")
placenoun = input("Is your place a proper noun? (y, n): ")
title = input("Insert what they're going to become when they get there: ")

if placenoun == "y":
    placenoun = "the"
elif placenoun == "n":
    placenoun = ""
else:
    print("Error: Invalid Answer")
    sys.exit

lyrics = """Now, this is a story all about how
Matty E's life got flipped-turned upside down
And I'd like to take a minute
Just sit right there
I'll tell you how Matthew became the bozo of a town called Bel-Air
In Alberquerque, New Mexico born and raised
In the crackden was where Matty spent most of his days
Chillin' out, maxin', relaxin', all cool
And all shootin' some b-ball outside of the school
When a couple of guys who were up to no good
Started making trouble in his neighborhood
He got in one little fight and Stuart got scared
He said, "You're movin' with your auntie and uncle in Bel-Air"
Matty begged and pleaded with him day after day
But he packed Matty's suitcase and sent him on his way
He gave him a kiss and then he gave him his ticket
Matty put his Walkman on and said, "I might as well kick it"
First class, yo this is bad
Drinking orange juice out of a crushed coke can
Is this what the people in jail living like?
Hmm, this might be alright
But wait, I hear they're prissy, bourgeois, all that
Is this the type of place that they just send this cool cat?
I don't think so
He'll see when he gets there
Matty hopes that they're prepared for the bozo of county jail
Well, the plane landed and when he came out
There was a dude who looked like a cop standing there with my name out
Matty ain't trying to get arrested yet, he just got here
he sprang with the quickness like lightning, disappeared
he whistled for a cab and when it came near
The license plate said, "CRAZY" and it had dice in the mirror
If anything he could say that this cab was rare
But he thought "Nah, forget it, yo, holmes to Bel Air"
Matty pulled up to the house about seven or eight
And he yelled to the cabbie, "Yo holmes, smell ya later"
He looked at the prison
He was finally there
To sit in his cell as the bozo of County Jail"""

clipboard(lyrics)
print(lyrics)
