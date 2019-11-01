# You don't have to use these classes, but we recommend them as a good place to start!

class MongoHandler():
    pass

class WeatherGetter():
    def __init__(self, date = None):
       self.link = f"https://api.darksky.net/forecast/{self.key}/{self.lat},{self.long},{self.date}?exclude=currently,hourly,flags”
       self.date = date + “T15:00:00”  #set default time to 3pm
       self.lat = 52.52 #Coordinates for Berlin
       self.long = 13.405 #Coordinates for Berlin
       self.key = “” #insert key here
       self.weather = self.getweathersummary()
    
     def getweathersummary(self):
       r = requests.get(self.link)
       response = r.json()
       try:
           response[‘daily’][‘data’][0][‘icon’]
       except:
           return response[‘daily’][‘data’][0][‘summary’]  #if there is no icon then get summary
       else:
           return response[‘daily’][‘data’][0][‘icon’]