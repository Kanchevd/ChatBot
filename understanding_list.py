#Daniel's code - 100%
import random
from geopy.geocoders import *
from geopy.geocoders import Nominatim
import geopy
geolocator = Nominatim()
from CineList import *

def emotions(message,mem):
    """Takes message and last line of memory as str, returns emotional-based response if deciphered,""Oops"" otherwise. """
    lastline = mem.splitlines()[-1]
    if "angry" in message:
        return  "Here's a relaxing thought: No one else knows what's going on either!"
    elif "sad" in lastline and "yes" in message:
        return "Well, aren't you smart.."
    elif "sad" in lastline and "no" in message:
        return "Now you know!"
    elif "sad" in message:
        return "Don't be sad. Did you know that foxes adopt lonely kittens?"
    elif ("depressed" in message) or ("suicide" in message) or ("kill myself" in message):
        return "Whatever you do, you should know: We would miss you. Call 116 123"
    else:
        return "Oops"

def greetings(message):
    """Takes message as str, returns response if deciphered,""Oops"" otherwise. """
    greetings_list = ["hi", "hello" ,"hey", "what's up"] 
    r_responses = ["Hello! What's up?","What's up?","Greetings! What's up?", "Hey,how are you doing?"]
    if message in greetings_list:
        return random.choice(r_responses)    
    return "Oops"

def closest_cinema(message,mem):
    """Takes message as str, returns a message as str depending on conversation,""Oops"" otherwise. """
    lastline = mem.splitlines()[-1]

    try:
        lastline2 = mem.splitlines()[-2]  #If there is no second to last line, sets the variable as ''(same with third to last)
    except IndexError:
        lastline2 = ''
    
    try:
        lastline3 = mem.splitlines()[-3]
    except IndexError:
        lastline3 = ''

    if ("nearest" in message) or ("closest" in message):
        return "Enter your postcode"
    elif ("nearest" in lastline) or ("closest" in lastline):
        return  findCinema2(message)
    elif (("nearest" in lastline2) or ("closest" in lastline2)) and (findCinema2(lastline)!= "Invalid postcode!"):
        return  cinemaDay(lastline,message)
    elif (("nearest" in lastline3) or ("closest" in lastline3)) and (findCinema2(lastline2)!= "Invalid postcode!")  and cinemaDay(lastline2,lastline)!="Invalid choice":
        return  cinemaTimes( lastline2, lastline , message)
    else:
        return "Oops"

def locInfo(message):
    """Takes message as str, returns location details if deciphered,""Oops"" otherwise. """
    #note - this function works locally, but doesn't run on the server
    if "where is" in message:
        if message == "where is" or message == "where is ": #Avoids errors if you don't append a location
            return 'Please append a location to "where is" and try again.'
        else:
            locStr = message[9:len(message)+1]
            userLoc = locStr.split()
            try:
                location = geolocator.geocode(userLoc)
                locList = location.address.split()
                country = locList[-1]
            except AttributeError:
                return "The location " + locStr + " could not be found,sorry. Try again." 
            
            return '"' + locStr + '" is in ' + country + ".\nFull Address: " + location.address
    else:
        return "Oops"

def memory(message,user_id,mem):
    """Takes message,memory and user ID as str, returns response if deciphered(or deletes history if ordered),""Oops"" otherwise. """
    if ("text history" in message) or ("conversation history" in message):
        return "Here is what I remember:\n" + str(mem.splitlines()).replace("[",'').replace("]",'')
    elif  "delete" in message: 
        f = open('%s.txt' %user_id, 'w') #Opens and closes the memory textfile with 'w', deleting whatever's inside.
        f.close
        return "Done."
    else:
        return "Oops"


def calc(message):
    """Takes message as str, returns response if deciphered,""Oops"" otherwise. """
    if 'calculate ' in message or 'calc ' in message:
        if 'calculate ' in message: #checks which one is said
            rem = 10 #rem is used to determine how much to remove from the original message to get only the equation
        else:
            rem = 5
        try:
            eq = message[rem:len(message)+1] #new string as equation
            return(eval(eq))
        except: #if it can't calculate what follows, various types of errors occur.
            return "Enter a valid problem"

    elif '+' in message or '-' in message or '*' in message or '/' in message or '**' in message:   
        try:
            return(eval(message))
        except:
            return ("Enter a valid problem/the problem without words.")

    else:
        return "Oops"

def randFacts(message,mem):
    """Takes message as str, returns a random fact if deciphered,""Oops"" otherwise. """
    lastline = mem.splitlines()[-1]

    if 'fact' in message:
        with open("randomFacts.txt") as file: #following 2 lines open the .txt and assign each line as a list item.
            lines = [line.strip() for line in file]
        size = len(lines)
        factN = random.randint(0,size-1) #returns a random fact.
        return(lines[factN]) + "\nDid you know that?"
    elif 'fact' in lastline and ("yes" in message or "no" in message):
        if "yes" in message:
            with open("randomFacts.txt") as file:
                lines = [line.strip() for line in file]
            size = len(lines)
            factN = random.randint(0,size-1)
            return "Alright, here's another:\n" + (lines[factN])
        else:
            return "Always happy to spread useless knowledge!"

    else:
        return "Oops"

def coinflip(message):
    """Takes message as str, returns "Heads" or "Tails" if deciphered,""Oops"" otherwise. """
    if "flip a coin" in message or "coinflip" in message:
        choices = ["Tails","Heads"]
        numR = random.randint(0,1)
        return "It's " + choices[numR] + "!"
    else:
        return "Oops"

def features(message):
    """Takes message as str, returns its features if deciphered,""Oops"" otherwise. """
    if "what can you do" in message or "features" in message:
        f = open("Features.txt",'r')
        feat = f.read()
        f.close()
        return "Here are my features:\n" + feat
    else:
        return "Oops"

#print(closest_cinema("0",'Where is the nearest cinema\nCV1 5LD'))