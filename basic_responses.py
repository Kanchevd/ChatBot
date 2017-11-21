#Daniel's code
from understanding_list import  * #all functions in understanding_list are meant to decode the message

def response_nomem(message):
    """Calls functions with the message one by one to see if any of them can decipher the message through keywords.Input is message as string and returns the response as a string. """
    
    message = message.lower() #code only works with lowercase

    #remove punctuation from message
    message = message.replace("!",'') 
    message = message.replace("?",'')
    message = message.replace(".",'')

    if closest_cinema(message,' ') != "Oops": #If functions can't decipher the message, they return "Oops".
        return closest_cinema(message,' ')
    
    elif emotions(message,' ') != "Oops":
        return emotions(message,'')

    elif greetings(message) != "Oops": 
        return greetings(message)

    elif randFacts(message,' ') != "Oops":
        return randFacts(message,'')
    
    elif cinemaDetails(message,' ') != "Oops":
        return cinemaDetails(message,' ')
        
    elif locInfo(message) != "Oops":
        return locInfo(message)

    elif calc(message) != "Oops":
        return calc(message)

    elif coinflip(message) != "Oops":
        return coinflip(message)

    elif features(message) != "Oops":
        return features(message)

    elif commonResp(message) != "Oops":
        return commonResp(message)
    
    elif movies(message) != "Oops":
        return movies(message)

    else:
        return "I don't understand, but hello!"

def response_mem(message,mem,user_id):
    """Tries to decipher the message through specific functions. Inputs are message, memory and user_id as string, and returns the response as a string."""
    message = message.lower()

    message = message.replace("!",'') 
    message = message.replace("?",'')
    message = message.replace(".",'')

    if closest_cinema(message,mem) !=  "Oops":
        return closest_cinema(message,mem)

    elif memory(message,user_id,mem) != "Oops":
        return memory(message,user_id,mem)

    elif emotions(message,mem) !=  "Oops":
        return emotions(message,mem)

    elif randFacts(message,mem) != "Oops":
        return randFacts(message,mem)

    elif cinemaDetails(message,mem) != "Oops":
        return cinemaDetails(message,mem)

    elif greetings(message) != "Oops":
        return greetings(message) + " Again!"

    elif locInfo(message) != "Oops":
        return locInfo(message)

    elif calc(message) != "Oops":
        return calc(message)

    elif coinflip(message) != "Oops":
        return coinflip(message)
        
    elif features(message) != "Oops":
        return features(message)

    elif commonResp(message) != "Oops":
        return commonResp(message)
    
    elif movies(message) != "Oops":
        return movies(message)

    else:
        return "I don't understand. Can you reiterate that?"