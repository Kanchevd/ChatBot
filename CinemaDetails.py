import json, requests
#-------Ben's code------
def postcodeToCoord(postcode):
    info = requests.get(("https://api.postcodes.io/postcodes/{}").format(postcode)).text
    infoJson = json.loads(info)
    resultJson = (infoJson["result"])
    longitude = resultJson["longitude"]
    latitude = resultJson["latitude"]
    return (latitude,longitude)
#-------End of ben's code-----
#-------Josh's Code-----------
def PlacesIdFinder(postcode,placeName):
    lat = postcodeToCoord(postcode)[1]
    lat = round(lat,5)
    longi = postcodeToCoord(postcode)[0]
    longi = round(longi,5)
    #requests data from google places api to get the id of the previously selected place
    requestFile = requests.get(("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius=8000&types=movie_theater&keyword={}&key=AIzaSyBdO3WJDRpu0CH4OsEX2ikCor8o2rsDJVg").format(longi,lat,placeName)).text
    #converts requested json data to a dictionary
    jsonFile = json.loads(requestFile)["results"]
    #gets the id the first matching place
    try:
        jsonID = jsonFile[0]['place_id']
    except IndexError:
        return "Cinema doesn't exist"
    
    #checks to see if there are any matching places before continuing
    if jsonID == None:
        print("There are no matching loctions in this area [GOOGLE PLACES]")
    
    #returns the ID of the **FIRST** matching place
    return(PlacesDetails(jsonID))

def PlacesDetails(placeID):
    requestFile = requests.get(("https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key=AIzaSyBdO3WJDRpu0CH4OsEX2ikCor8o2rsDJVg").format(placeID)).text
    jsonFile = json.loads(requestFile)
    jsonResult = jsonFile['result']
    
    #needs be a single print as otherwise may print some but not all
    cinemaTotal = ""
    try:
        cinemaName = (jsonResult['name']+"\n")
        cinemaTotal += cinemaName
    except:
        pass
    
    try:
        cinemaPhoneNumber = ("Cinema phone number:"+"\n"+jsonResult['international_phone_number']+"\n")
        cinemaTotal += "\n"+cinemaPhoneNumber
    except:
        pass
    
    try:
        cinemaAddress = ("Cinema address:"+"\n"+jsonResult['formatted_address']+"\n")
        cinemaTotal += "\n"+cinemaAddress
    except:
        pass
    
    try:
        cinemaWebsite = ("Cinema website:"+"\n"+jsonResult['website']+"\n")
        cinemaTotal += "\n"+cinemaWebsite
    except:
        pass
    
    try:
        openingJson = jsonResult['opening_hours']['weekday_text']
        openingHours = ("Opening times:\n")
        for item in openingJson:
            openingHours += (item + "\n")
        cinemaTotal += "\n"+openingHours
    except:
        pass
    
    try:
        cinemaReview = ("Most recent review:"+"\n"+jsonResult['reviews'][0]['author_name']+"\n")
        cinemaReview += (jsonResult['reviews'][0]['rating']+"\n")
        cinemaReview += (jsonResult['reviews'][0]['text'])
        cinemaTotal += "\n"+cinemaReview
    except:
        pass
    #Final info page to send back to the user
    return(cinemaTotal)
#gets detail on the chosen place
######################TEST DATA######################
#print(PlacesIdFinder("cv2 3fb","odeon"))