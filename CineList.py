#Harry's code
import json, requests, datetime
    
def findID(cine,cinemaArray):
    """In this function it takes the raw cinema list as an input and takes out the relative cinema IDs from the list, putting them into an array."""
    #adds some formatting so it can find the last ID number easily.
    for x in range(0,12):
        cine[x] = cine[x]+"'"
        #print (cine[x])
    
    for x in range (0,12):
        currentCinema = cine[x]
        #print(currentCinema)
        idString = currentCinema.find('id')
        endOfID = 0
        while endOfID < idString:
            endOfID = currentCinema.find("''")
            currentCinema = currentCinema.replace("''",'XX',1)
        idValue = currentCinema[idString+6:endOfID]
        cinemaArray[x-1][0] = idValue
    return cinemaArray

def findName(cine,cinemaArray):
    for x in range (0,12):
        currentCinema = cine[x]
        #print(currentCinema)
        nameString = currentCinema.find('name')
        endOfName = 0
        while endOfName < nameString:
            endOfName = currentCinema.find("''")
            currentCinema = currentCinema.replace("''",'XX',1)
        nameValue = currentCinema[nameString+8:endOfName]
        nameValue = ' ' + nameValue
        cinemaArray[x-1][1] = nameValue
    return cinemaArray

def findDistance(cine,cinemaArray):
    for x in range (0,12):
        currentCinema = cine[x]
        #print(currentCinema)
        distanceString = currentCinema.find('distance')
        endOfDistance = 0
        currentCinema = currentCinema.replace("'",'X',1)
        while endOfDistance < distanceString:
            endOfDistance = currentCinema.find("'")
            currentCinema = currentCinema.replace("'",'X',1)
        endOfDistance = currentCinema.find("'")            
        distanceValue = currentCinema[distanceString+10:endOfDistance]
        cinemaArray[x-1][2] = distanceValue
    return cinemaArray
    
def formatFilmList(filmList):
    filmList = filmList.replace('{"status":"ok","listings":[{','')
    filmList = filmList.replace('}]}','')
    unformattedFilmListArray = filmList.split("},{")
    noOfFilms = len(unformattedFilmListArray)
    filmListArray = [[0 for x in range(2)] for y in range(noOfFilms-1)]
    for film in range(0,noOfFilms-1):
        currentFilm = unformattedFilmListArray[film]
        currentFilm.replace('"title":','')
        startOfName = currentFilm.find('"')
        endOfName = currentFilm.find('","')
        filmName = currentFilm[startOfName+9:endOfName]
        filmListArray[film][0] = filmName
        
        startOfTime = currentFilm.find('[')
        endOfTime = currentFilm.find(']')
        filmTime = ' ' + currentFilm[startOfTime+1:endOfTime]
        filmListArray[film][1] = filmTime
    return filmListArray  

def findCinema(postcode):
    #Does a request to get the list of closest cinemas (fixed location)
    postcodeRequest = 'http://api.cinelist.co.uk/search/cinemas/postcode/{}'.format(postcode) 
    importList = requests.get(postcodeRequest).text
    #Requested data get turned to Json format (Because it broke without it)
    jsonFile = json.loads(importList)
    #Converts on the cinema attributes back to a string (get rid of some un-needed data)
    rawCine = str(jsonFile["cinemas"])
    #Gets rid of some brackets and commas so the final output is just wanted text
    rawCine = rawCine.replace("[{", "")
    rawCine = rawCine.replace("}]", "")
    rawCine = rawCine.replace("', '", "''")
    rawCine = rawCine.replace(", '", "'")
    #breaks up the big string into list of smaller strings of data about each cinema
    cine = rawCine.split("}, {")
    cinemaArray = [[0 for x in range(3)] for y in range(11)]
    cinemaArray = findID(cine,cinemaArray)
    cinemaArray = findName(cine,cinemaArray)
    cinemaArray = findDistance(cine,cinemaArray)
    
    return cinemaArray

def findCinema2(postcode):
    postcode = postcode.replace(" ","")
    try:
        cinemaArray = findCinema(postcode)
    except:
        return "Invalid postcode!"
    resp = "Here are the first 5 cinemas:\n"
    for i in range(0,5):
        resp += str(i+1) + '.' + cinemaArray[i][1][1:len(cinemaArray[i][1])+1] + ',' + cinemaArray[i][2] +' miles away\n'
    resp += 'Which would you wish to go to?'
    return resp

def cinemaDay(postcode,choice):
    postcode = postcode.replace(" ","")
    try:
        cinemaArray = findCinema(postcode)
    except:
        return "Invalid postcode!"
    if choice.isdigit()==False or (int(choice)>10) or (int(choice)<1):
        return ("Invalid choice")

    choice = int(choice)
    return "Please enter the day of the week you wish to get listings for."

def cinemaTimes(postcode,cineChoice,dayChoice):
    postcode = postcode.replace(" ","")
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    curDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    cineChoice = int(cineChoice)
    currentTime = datetime.datetime.now()
    currentDay = currentTime.strftime("%A")
    try:
        cinemaDayIndex = days.index(dayChoice)
    except ValueError:
        return "Invalid day choice!"
    currentDayIndex = curDays.index(currentDay)
    if cinemaDayIndex < currentDayIndex:
        daysDifference = (cinemaDayIndex+7)-currentDayIndex
    else:
        daysDifference = cinemaDayIndex - currentDayIndex
    cinemaArray = findCinema(postcode)
    cinemaRequest = 'http://api.cinelist.co.uk/get/times/cinema/{}?day={}'.format(cinemaArray[int(cineChoice)][0],daysDifference)
    filmList = requests.get(cinemaRequest).text
 
    filmListArray = formatFilmList(filmList)
    films = "Here are the movies and times for" + cinemaArray[cineChoice-1][1] + " on " + dayChoice + ':\n' 
    for movie in range(0,len(filmListArray)):
        films += filmListArray[movie][0] + ':'
        for time in range(1,len(filmListArray[movie])):
            films += filmListArray[movie][time].replace('"','')
        films += '\n'
    return(films)

#print(findCinema2("CV23FB"))
#print(cinemaDay("CV23FB",'2'))
#print(cinemaTimes("CV24FB",'2','thursday'))