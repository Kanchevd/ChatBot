#Daniel's code - 100%
import random
from writeToID import write_to_id 
from basic_responses import response_nomem,response_mem 

def output(message,user_id):
    """Takes the message and ID as strings and returns a message.Calls one of 2 different functions depending if it can find existing memory."""
    try:   
        f = open('%s.txt' %user_id, 'r')
        mem = f.read()
        f.close
    except FileNotFoundError: #If it doesn't find a text file with the user's ID, it sets the memory as an empty string.
        mem = ''

    if mem:    
        write_to_id(message,user_id) #Write the user's message in the memory
        return response_mem(message,mem,user_id) #Calls the main memory function with message, memory and the user's ID
    else:
        write_to_id(message,user_id)
        return response_nomem(message) #Calls the main memory-less function with only the user's message

#Bot simulation - asks user for id and message and simulates the ChatBot Locally
#test_id = input('id:')
#test_message = input('message:')
#print(output(test_message,test_id))