# Author: Jasmine Singh
# Github Username: Jassig98
# Date: November 30, 2022
# Description: A program in which there is a streaming guide with a list of streaming services, and a streaming service with a dictionary of movies. It can  be used to determine which streaming services have a desired movie.

class Movie:
    """movie object"""
    def __init__(self,title,genre,director,year):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
    def get_title(self):
        return self.title
    def get_genre(self):
        return self.genre
    def get_director(self):
        return self.director
    def get_year(self):
        return self.year

class StreamingService:
    def __init__(self,name):
        self.name = name
        self.catalog = dict()
    def get_name(self):
        return self.name
    def get_catalog(self):
        return self.catalog
    def add_movie(self,mov):
        self.catalog[mov.get_title()] = mov
    def delete_movie(self,title):
        if title in self.catalog.keys():
            del self.catalog[title]

class StreamingGuide:
    def __init__(self):
        self.listofServices = []

    def add_streaming_service(self,service):
        self.listOfServices.append(service)

    def delete_streaming_service(self,nm):
        for ss in self.listOfServices:
            if(ss.get_name() == name):
                self.listOfServices.remove(ss)

    def where_to_watch(self,title):
        _1=[]

        for ss in self.listOfServices:
            if(title in ss.get_catalog().keys()):
                _1.append(ss.get_name() + " ("+str(ss.get_catalog())
[title].get_year())+"}"
        if (len(1) == 0):
            return none
        else:
            return 1
