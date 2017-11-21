#Harry's code
import json, requests

def movieInfo(movieName):
    movieNameFormatted = movieName.replace(' ', '+')
    movieRequest = 'http://www.omdbapi.com/?i=tt3896198&apikey=445c9448&t={}&type=movie&r=json'.format(movieNameFormatted)
    movie = requests.get(movieRequest).text
    movieJson = json.loads(movie) 
    
    try:
        genre = movieJson["Genre"]
    except:
        genre = ''
        
    try:
        plot = movieJson["Plot"]
    except:
        plot = ''
    
    try:
        runtime = movieJson["Runtime"]
    except:
        runtime = ''
        
    try:
        website = movieJson["Website"]
    except:
        website = ''
        
    try:
        ratings = movieJson["imdbRating"]
    except:
        ratings = "N/A"
    
    try:
        numberOfRatings = movieJson["imdbVotes"]
    except:
        numberOfRatings = ''
        
    if ratings != "N/A":
        if float(ratings) < 5:
            review = "This movie is not recommended as it scored {} on IMDB from {} reviews.".format(ratings,numberOfRatings)
        elif 5 <= float(ratings) < 8:
            review = "This movie is recommended as it scored {} on IMDB from {} reviews.".format(ratings,numberOfRatings)
        elif float(ratings) > 8:
            review = "This movie is a 'must see' as it scored {} on IMDB from {} reviews.".format(ratings,numberOfRatings)
    else:
        review = "N/A"
        
    movieInfo = "Title = {} \nGenre - {} \nPlot - {} \nRuntime - {} \nWebsite - {} \nReview - {} \n".format(movieName,genre,plot,runtime,website,review)
    return movieInfo
