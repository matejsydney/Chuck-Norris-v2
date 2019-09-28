
import random

#importing list must by a .py file
from jokeList import jokeDict

#picking random starts with first number and ends with the last one- converted to string

# randomJoke = str(random.randint(1,7)) - not needed all in one line of code below

jokeReturn = (jokeDict[str(random.randint(1,7))])

joke = (jokeDict[str(random.randint(1,7))])
speechText = joke + " <break time='3s'/>" + " How about another one ?"
displayText = joke + " How about another one ?"

print (speechText)
print(displayText)
