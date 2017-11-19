import json, requests
from postcodes import PostCoder
from lib import PostCodeClient

def PlacesIdFinder(long,lat,placeName):
    """requests data from google places api to get the id of the previously selected place"""
    requestFile = requests.get(("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius=8000&types=movie_theater&keyword={}&key=AIzaSyBdO3WJDRpu0CH4OsEX2ikCor8o2rsDJVg").format(long,lat,placeName)).text
    #converts requested json data to a dictionary
    jsonFile = json.loads(requestFile)["results"]
    #gets the id the first matching place
    jsonID = jsonFile[0]['place_id']
    
    #checks to see if there are any matching places before continuing
    if jsonID == None:
        print("There are no matching loctions in this area [GOOGLE PLACES]")
    
    #returns the ID of the **FIRST** matching place
    return(PlacesDetails(jsonID))

def PlacesDetails(placeID):
    requestFile = requests.get(("https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key=AIzaSyBdO3WJDRpu0CH4OsEX2ikCor8o2rsDJVg").format(placeID)).text
    jsonFile = json.loads(requestFile)
    jsonResult = jsonFile['result']
    #print (json.dumps(jsonResult, indent=4, sort_keys=True))
    
    print(jsonResult['name'])
    print(jsonResult['international_phone_number'])
    print(jsonResult['formatted_address'])
    print(jsonResult['website'])
#gets detail on the chosen place
#PlacesIdFinder(52.4068,-1.51957,"odeon")
