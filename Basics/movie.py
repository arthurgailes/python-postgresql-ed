# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:54:41 2017

@author: agail
"""

class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "<Movie: {}>".format(self.name)
    
    def json(self):
        return {
                'name': self.name,
                'genre': self.genre,
                'watched': self.watched
        }
        
    @classmethod
    def from_json(cls, json_data):  # {'name': '...', 'genre': '...', 'watched' = True}
        return Movie(**json_data) #reads the data as parameters specified at the top.