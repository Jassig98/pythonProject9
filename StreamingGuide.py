# Author: Jasmine Singh
# Github Username: Jassig98
# Date: November 30, 2022
# Description:

class Movie:
    def __init__(self,title,genre,director,year):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
class StreamingService:
    catalog = dict()
    def __init__(self,name):
        self.name = name

    def add_movie(self,mov):
        self.catalog[mov.title] = mov

    def delete_movie(self,delName):
        self.catalog.pop(delName)

    def isPresent(self,movName):
        if movName in self.catalog.keys():
            return True

class StreamingGuide:
    def __init__(self):
        self.listofServices = []

    def add_streaming_service(self,service):
        self.listOfServices.append(service)

    def delete_streaming_service(self,nm):
        self.todel = -1
        for i in range(len(self.listOfServices)):
            if (self.listOfServices[i].name == nm):
                self.todel = i
        self.listOfServices.pop(self.todel)

    def where_to_watch(self,movieName):
        _1st = []
        for service in self.listOfServices:
            if(service.isPresent(movieName)):
                _1st.append(service.name)
            return _1st

