#Daniel's code - 100%
def write_to_id(message,user_id):
    """ This function takes the user's message and ID and writes their message in a text file with the name of their ID."""
    try:
        f = open('%s.txt' %user_id, 'a')
        f.write(message + '\n')
        f.close()
    except FileNotFoundError: #If the file doesn't exist, create it
        f = open('%s.txt' %user_id, 'w')
        f.write(message + '\n')
        f.close()